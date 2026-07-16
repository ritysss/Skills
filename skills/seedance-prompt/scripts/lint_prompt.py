#!/usr/bin/env python3
"""Deterministic lint checks for final Seedance prompt text."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


REF_RE = re.compile(r"@(图片|视频|音频)(\d+)")
LENS_RE = re.compile(r"(?<!\d)(\d{1,3}(?:\.\d+)?)\s*mm(?![A-Za-z])", re.IGNORECASE)
FOV_RE = re.compile(r"(?:约\s*)?(\d{1,3}(?:\.\d+)?)\s*(?:°|度)\s*视场")
FORMAT_RE = re.compile(
    r"(?:Super\s*)?\d{1,3}(?:\.\d+)?\s*mm\s*(?:胶片|画幅|传感器|film)",
    re.IGNORECASE,
)
SHOT_RE = re.compile(
    r"^镜头\s*(\d+)(?:\s*\[([^\]]+)\])?\s*[：:]",
    re.MULTILINE,
)
FIELD_RE = re.compile(r"^\[([^\]]+)\]\s*", re.MULTILINE)
REQUIRED_FIELDS = ("主体", "动作", "镜头", "风格", "约束", "音频")
OPTIONAL_FIELDS = ("终帧",)
ROLE_PREDICATE_RE = re.compile(
    r"作为|仅参考|只参考|参考|只控制|控制|锁定|沿用|继承|提供|优先|用于|不控制|不作为|"
    r"一致|服从|采用|按照|承担|为权威|定义|决定"
)
NEGATIVE_CONTROL_RE = re.compile(
    r"不新增|不使用|不出现|不复制|不控制|不采用|不允许|不提前|不改变|不重演|不重复|"
    r"不引入|不附加|没有|(?:^|[,，])\s*无|禁止|避免|删除|排除|不得|不作为|"
    r"不(?!确定|知道|清楚|决定|选择|同意|明白)[\u4e00-\u9fff]{1,6}"
)
BRANCH_RE = re.compile(
    r"或者|二选一|可选|(?<!不可)或|(?:方案\s*)?[A-Za-z]\s*[/／-]\s*(?:方案\s*)?[A-Za-z]",
    re.IGNORECASE,
)
FIXED_BRANCH_PHRASES = ("不可或缺", "或多或少", "或者说")

ROLE_CATEGORIES = {
    "identity": re.compile(r"面孔|脸部|人脸|五官|身份|人物外观|发型|体型|妆容"),
    "costume": re.compile(r"人物外观|角色外观|服装|装备|造型|衣物|饰品|武器|道具"),
    "composition": re.compile(
        r"首帧|尾帧|第0帧|起始构图|构图|景别|画面位置|空间层次|负空间|接触|轴线|"
        r"起始状态|当前状态|结尾状态|结束状态|连续性"
    ),
    "action": re.compile(r"动作|运动|路径|时序|blocking|受力|姿势|表演", re.IGNORECASE),
    "camera": re.compile(r"相机|摄影机|运镜|镜头运动|镜头关系|焦点|焦段|视场|机位|方向|速度|节奏"),
    "scene": re.compile(r"场景|环境|空间|地点|光线|光色|曝光|色温|白平衡|尺度"),
    "style": re.compile(r"风格|质感|色彩|颗粒|材质"),
    "audio": re.compile(r"音频|声音|对白|节拍|环境声|BGM", re.IGNORECASE),
}


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    line: int | None = None


@dataclass
class Result:
    issues: list[Issue]

    @property
    def errors(self) -> list[Issue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def ok(self) -> bool:
        return not self.errors


def _clean_text(text: str) -> str:
    return "\n".join(
        line for line in text.replace("\r\n", "\n").splitlines() if not line.strip().startswith("```")
    ).strip()


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, max(0, offset)) + 1


def _sections(text: str) -> dict[str, tuple[str, int]]:
    matches = list(re.finditer(r"^【([^】]+)】\s*$", text, re.MULTILINE))
    result: dict[str, tuple[str, int]] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1).strip()] = (text[start:end].strip(), start)
    return result


def _fields(prompt_section: str, base_offset: int) -> dict[str, tuple[str, int]]:
    matches = list(FIELD_RE.finditer(prompt_section))
    result: dict[str, tuple[str, int]] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(prompt_section)
        result[match.group(1).strip()] = (prompt_section[start:end].strip(), base_offset + start)
    return result


def _add(
    issues: list[Issue],
    code: str,
    message: str,
    text: str,
    offset: int | None = None,
    severity: str = "error",
) -> None:
    issues.append(Issue(severity, code, message, _line_number(text, offset) if offset is not None else None))


def _clauses(text: str) -> Iterable[tuple[str, int]]:
    start = 0
    for match in re.finditer(r"[。；;！!？?\n]", text):
        if match.start() > start:
            yield text[start:match.start()], start
        start = match.end()
    if start < len(text):
        yield text[start:], start


def _lint_branches(text: str, issues: list[Issue], allow_variants: bool) -> None:
    if allow_variants:
        return
    for clause, offset in _clauses(text):
        scrubbed = clause
        for phrase in FIXED_BRANCH_PHRASES:
            scrubbed = scrubbed.replace(phrase, "")
        match = BRANCH_RE.search(scrubbed)
        if not match:
            continue
        prefix = scrubbed[: match.start()]
        if NEGATIVE_CONTROL_RE.search(prefix):
            continue
        _add(
            issues,
            "ALT001",
            f"未决分支：{clause.strip()[:90]}",
            text,
            offset + match.start(),
        )


def _lint_contract(
    text: str,
    sections: dict[str, tuple[str, int]],
    issues: list[Issue],
) -> tuple[str | None, dict[str, tuple[str, int]]]:
    field_matches = list(FIELD_RE.finditer(text))
    field_names = [match.group(1).strip() for match in field_matches]
    has_single = bool(field_matches)
    has_multishot = "分镜" in sections
    fields: dict[str, tuple[str, int]] = {}

    if has_single and has_multishot:
        _add(issues, "CONTRACT001", "单镜头六字段与多镜头分镜合同被混用。", text)
        return "mixed", fields
    if not has_single and not has_multishot:
        _add(issues, "CONTRACT002", "未识别到单镜头六字段或【分镜】合同。", text)
        return None, fields

    if has_single:
        mode = "single"
        fields = _fields(text, 0)
        if sections:
            names = "、".join(f"【{name}】" for name in sections)
            _add(
                issues,
                "CONTRACT001",
                f"单镜头只输出六字段，不应包含外层章节：{names}。",
                text,
            )
        for name in REQUIRED_FIELDS:
            if name not in fields or not fields[name][0]:
                code = "AUDIO001" if name == "音频" else "CONTRACT002"
                _add(issues, code, f"单镜头合同缺少非空[{name}]。", text)
        duplicates = sorted({name for name in field_names if field_names.count(name) > 1})
        if duplicates:
            _add(issues, "CONTRACT003", f"单镜头字段重复：{duplicates}。", text)
        unexpected = [name for name in field_names if name not in REQUIRED_FIELDS + OPTIONAL_FIELDS]
        if unexpected:
            _add(issues, "CONTRACT003", f"单镜头包含未定义字段：{unexpected}。", text)
        expected_order = list(REQUIRED_FIELDS)
        if "终帧" in field_names:
            expected_order.append("终帧")
        if not duplicates and not unexpected and field_names != expected_order:
            _add(
                issues,
                "CONTRACT003",
                f"单镜头字段顺序应为{expected_order}，实际为{field_names}。",
                text,
            )
        return mode, fields

    allowed_sections = {"分镜", "跨镜头一致性", "音频"}
    unexpected_sections = [name for name in sections if name not in allowed_sections]
    if unexpected_sections:
        _add(
            issues,
            "CONTRACT001",
            f"多镜头合同包含旧版或未定义章节：{unexpected_sections}。",
            text,
        )
    for name in ("分镜", "音频"):
        if name not in sections or not sections[name][0]:
            code = "AUDIO001" if name == "音频" else "CONTRACT002"
            _add(issues, code, f"多镜头合同缺少非空【{name}】。", text)
    if "分镜" not in sections:
        return None, fields
    storyboard, storyboard_offset = sections["分镜"]
    shots = list(SHOT_RE.finditer(storyboard))
    if not shots:
        _add(issues, "CONTRACT002", "【分镜】内缺少“镜头N：”条目。", text, storyboard_offset)
        return "sequential", fields
    numbers = [int(match.group(1)) for match in shots]
    expected_numbers = list(range(1, len(shots) + 1))
    if numbers != expected_numbers:
        _add(
            issues,
            "TIME004",
            f"镜头编号不连续：{numbers}。",
            text,
            storyboard_offset + shots[0].start(),
        )
    timed_flags = [bool(match.group(2)) for match in shots]
    if any(timed_flags) and not all(timed_flags):
        _add(
            issues,
            "CONTRACT003",
            "同一【分镜】不能混用带时间码与不带时间码的镜头条目。",
            text,
            storyboard_offset,
        )
        return "mixed", fields
    mode = "timed" if all(timed_flags) else "sequential"
    return mode, fields


def _lint_single_ownership(
    text: str,
    fields: dict[str, tuple[str, int]],
    issues: list[Issue],
) -> None:
    if "镜头" not in fields:
        return
    for name, (field_text, field_offset) in fields.items():
        if name in {"镜头", "终帧"}:
            continue
        lenses, fovs = _optical_values(field_text)
        if lenses or fovs:
            _add(
                issues,
                "OWNER001",
                f"[{name}]包含数字焦段/FOV；光学事实应只写入[镜头]。",
                text,
                field_offset,
            )


def _optical_values(text: str) -> tuple[set[float], set[float]]:
    scrubbed = FORMAT_RE.sub("", text)
    lenses = {float(match.group(1)) for match in LENS_RE.finditer(scrubbed)}
    fovs = {float(match.group(1)) for match in FOV_RE.finditer(scrubbed)}
    return lenses, fovs


def _has_explicit_zoom_path(text: str, values: set[float]) -> bool:
    if len(values) != 2:
        return False
    first, second = sorted(values)
    pattern = re.compile(
        rf"从\s*{first:g}\s*mm[^。；\n]{{0,30}}(?:变焦|焦段)[^。；\n]{{0,20}}(?:至|到)\s*{second:g}\s*mm",
        re.IGNORECASE,
    )
    reverse = re.compile(
        rf"从\s*{second:g}\s*mm[^。；\n]{{0,30}}(?:变焦|焦段)[^。；\n]{{0,20}}(?:至|到)\s*{first:g}\s*mm",
        re.IGNORECASE,
    )
    return bool(pattern.search(text) or reverse.search(text))


def _shot_chunks(
    mode: str | None,
    sections: dict[str, tuple[str, int]],
    fields: dict[str, tuple[str, int]],
) -> list[tuple[str, str, int]]:
    chunks: list[tuple[str, str, int]] = []
    if mode == "single" and "镜头" in fields:
        camera, offset = fields["镜头"]
        chunks.append(("single", camera, offset))
    elif mode in {"sequential", "timed"} and "分镜" in sections:
        storyboard, base_offset = sections["分镜"]
        matches = list(SHOT_RE.finditer(storyboard))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(storyboard)
            chunks.append((f"镜头{match.group(1)}", storyboard[match.start():end], base_offset + match.start()))
        if "跨镜头一致性" in sections and sections["跨镜头一致性"][0]:
            continuity_text, continuity_offset = sections["跨镜头一致性"]
            chunks.append(("跨镜头一致性", continuity_text, continuity_offset))
    return chunks


def _lint_optics(
    text: str,
    chunks: Sequence[tuple[str, str, int]],
    issues: list[Issue],
    authority_texts: Sequence[str],
    no_invent_optics: bool,
) -> None:
    prompt_lenses: set[float] = set()
    prompt_fovs: set[float] = set()
    continuity_lenses: set[float] = set()
    continuity_fovs: set[float] = set()
    per_chunk_values: list[tuple[str, set[float], set[float], int]] = []
    for name, chunk, offset in chunks:
        lenses, fovs = _optical_values(chunk)
        prompt_lenses.update(lenses)
        prompt_fovs.update(fovs)
        per_chunk_values.append((name, lenses, fovs, offset))
        if name == "跨镜头一致性":
            continuity_lenses = lenses
            continuity_fovs = fovs
        if len(lenses) > 1 and not _has_explicit_zoom_path(chunk, lenses):
            _add(
                issues,
                "OPTICS001",
                f"{name}含多个不同焦段：{sorted(lenses)}。",
                text,
                offset,
            )
        if len(fovs) > 1:
            _add(
                issues,
                "OPTICS002",
                f"{name}含多个不同FOV：{sorted(fovs)}。",
                text,
                offset,
            )

    if len(continuity_lenses) == 1:
        expected = next(iter(continuity_lenses))
        for name, lenses, _fovs, offset in per_chunk_values:
            if name != "跨镜头一致性" and any(value != expected for value in lenses):
                _add(
                    issues,
                    "OPTICS004",
                    f"{name}焦段{sorted(lenses)}与跨镜头{expected:g}mm光学约束冲突。",
                    text,
                    offset,
                )
    if len(continuity_fovs) == 1:
        expected = next(iter(continuity_fovs))
        for name, _lenses, fovs, offset in per_chunk_values:
            if name != "跨镜头一致性" and any(value != expected for value in fovs):
                _add(
                    issues,
                    "OPTICS004",
                    f"{name} FOV {sorted(fovs)}与跨镜头约{expected:g}度视场约束冲突。",
                    text,
                    offset,
                )

    if no_invent_optics and (prompt_lenses or prompt_fovs):
        _add(
            issues,
            "OPTICS003",
            "当前任务未授权数字焦段/FOV，但输出自行加入了数字光学值。",
            text,
        )

    authority_lenses: set[float] = set()
    authority_fovs: set[float] = set()
    optics_context = re.compile(r"镜头|焦段|视场|广角|长焦|透视|相机|摄影机|机位")
    for authority in authority_texts:
        scrubbed = FORMAT_RE.sub("", authority)
        for match in LENS_RE.finditer(scrubbed):
            window = scrubbed[max(0, match.start() - 30): min(len(scrubbed), match.end() + 30)]
            if optics_context.search(window):
                authority_lenses.add(float(match.group(1)))
        authority_fovs.update(float(match.group(1)) for match in FOV_RE.finditer(scrubbed))

    if len(authority_lenses) == 1:
        expected = next(iter(authority_lenses))
        if not prompt_lenses:
            _add(issues, "AUTH001", f"来源明确规定{expected:g}mm，但输出镜头语言未保留。", text)
        wrong = sorted(value for value in prompt_lenses if value != expected)
        if wrong:
            _add(
                issues,
                "AUTH002",
                f"来源规定{expected:g}mm，输出引入了未授权焦段{wrong}。",
                text,
            )
        if not authority_fovs and prompt_fovs:
            _add(
                issues,
                "AUTH003",
                "来源只规定焦段，输出又自行推导了数字FOV。",
                text,
            )
    elif len(authority_lenses) > 1:
        _add(
            issues,
            "AUTH004",
            f"authority 中存在多个焦段{sorted(authority_lenses)}，需先人工确定各镜头归属。",
            text,
            severity="warning",
        )

    if len(authority_fovs) == 1:
        expected = next(iter(authority_fovs))
        if not prompt_fovs:
            _add(issues, "AUTH001", f"来源明确规定约{expected:g}度视场，但输出未保留。", text)
        wrong = sorted(value for value in prompt_fovs if value != expected)
        if wrong:
            _add(
                issues,
                "AUTH002",
                f"来源规定约{expected:g}度视场，输出引入了未授权FOV{wrong}。",
                text,
            )
        if not authority_lenses and prompt_lenses:
            _add(
                issues,
                "AUTH003",
                "来源只规定FOV，输出又自行补写了数字焦段。",
                text,
            )


def _role_categories(text: str) -> set[str]:
    return {name for name, pattern in ROLE_CATEGORIES.items() if pattern.search(text)}


def _lint_references(
    text: str,
    issues: list[Issue],
    available_refs: set[str],
    rejected_refs: set[str],
    require_reanchor: str | None,
) -> None:
    all_refs = {match.group(0) for match in REF_RE.finditer(text)}
    for match in REF_RE.finditer(text):
        if int(match.group(2)) == 0:
            _add(issues, "REF001", f"非法引用标签{match.group(0)}。", text, match.start())
    if not all_refs:
        return
    ref_clauses: dict[str, list[tuple[str, int]]] = {ref: [] for ref in all_refs}
    for clause, clause_offset in _clauses(text):
        refs = {match.group(0) for match in REF_RE.finditer(clause)}
        for ref in refs:
            ref_clauses[ref].append((clause, clause_offset))
            roles = _role_categories(clause)
            if not ROLE_PREDICATE_RE.search(clause) or not roles:
                _add(
                    issues,
                    "REF003",
                    f"{ref}在当前语句中缺少明确的用途谓词或职责范围。",
                    text,
                    clause_offset,
                )

    if available_refs:
        for ref in sorted(all_refs - available_refs):
            _add(issues, "REF005", f"Prompt使用了未列为已上传的{ref}。", text)

    for ref in sorted(rejected_refs):
        if ref in all_refs:
            clause_offset = ref_clauses[ref][0][1] if ref_clauses[ref] else None
            _add(issues, "CANON001", f"被拒绝的{ref}不应进入最终 Prompt。", text, clause_offset)

    if require_reanchor:
        clauses = ref_clauses.get(require_reanchor, [])
        anchored = any(
            re.search(r"重锚|第0帧|首帧|起始构图|起始接触", clause)
            for clause, _offset in clauses
        )
        if not anchored:
            _add(
                issues,
                "CANON002",
                f"链式延长要求用{require_reanchor}重锚，但内联引用未赋予重锚/首帧职责。",
                text,
            )


def _parse_timestamp(value: str) -> float:
    value = value.strip()
    parts = value.split(":")
    if len(parts) == 1:
        return float(parts[0])
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    raise ValueError(value)


def _parse_range(value: str) -> tuple[float, float] | None:
    normalized = value.replace("—", "-").replace("–", "-").replace("~", "-").replace("至", "-")
    match = re.fullmatch(r"\s*([0-9:.]+)\s*-\s*([0-9:.]+)\s*", normalized)
    if match:
        return _parse_timestamp(match.group(1)), _parse_timestamp(match.group(2))
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*秒\s*", normalized)
    if match:
        return float(match.group(1)), float(match.group(2))
    return None


def _lint_timing(
    text: str,
    sections: dict[str, tuple[str, int]],
    issues: list[Issue],
    duration: float | None,
) -> None:
    if "分镜" not in sections:
        return
    storyboard, base_offset = sections["分镜"]
    matches = list(SHOT_RE.finditer(storyboard))
    if not matches:
        return
    parsed: list[tuple[int, float, float, int]] = []
    for match in matches:
        interval_text = match.group(2)
        if interval_text is None:
            continue
        interval = _parse_range(interval_text)
        if interval is None:
            _add(
                issues,
                "TIME001",
                f"镜头{match.group(1)}时间段无法解析：{interval_text}。",
                text,
                base_offset + match.start(),
            )
            continue
        start, end = interval
        if end <= start:
            _add(
                issues,
                "TIME002",
                f"镜头{match.group(1)}结束时间不大于开始时间。",
                text,
                base_offset + match.start(),
            )
        parsed.append((int(match.group(1)), start, end, base_offset + match.start()))
    if not parsed:
        return
    if abs(parsed[0][1]) > 0.05:
        _add(issues, "TIME003", "第一个镜头未从0秒开始。", text, parsed[0][3])
    for previous, current in zip(parsed, parsed[1:]):
        delta = current[1] - previous[2]
        if delta < -0.05:
            _add(
                issues,
                "TIME005",
                f"镜头{previous[0]}与镜头{current[0]}重叠{abs(delta):g}秒。",
                text,
                current[3],
            )
        elif delta > 0.05:
            _add(
                issues,
                "TIME005",
                f"镜头{previous[0]}与镜头{current[0]}之间断裂{delta:g}秒。",
                text,
                current[3],
            )
    if duration is not None:
        if abs(parsed[-1][2] - duration) > 0.15:
            _add(
                issues,
                "TIME006",
                f"最后镜头结束于{parsed[-1][2]:g}秒，与目标{duration:g}秒不符。",
                text,
                parsed[-1][3],
            )


def lint_text(
    text: str,
    *,
    duration: float | None = None,
    authority_texts: Sequence[str] = (),
    available_refs: Iterable[str] = (),
    allow_variants: bool = False,
    no_invent_optics: bool = False,
    rejected_refs: Iterable[str] = (),
    require_reanchor: str | None = None,
    max_chars: int | None = None,
) -> Result:
    text = _clean_text(text)
    issues: list[Issue] = []
    sections = _sections(text)
    mode, fields = _lint_contract(text, sections, issues)
    _lint_branches(text, issues, allow_variants)
    if mode == "single":
        _lint_single_ownership(text, fields, issues)
    chunks = _shot_chunks(mode, sections, fields)
    _lint_optics(text, chunks, issues, authority_texts, no_invent_optics)
    _lint_references(
        text,
        issues,
        set(available_refs),
        set(rejected_refs),
        require_reanchor,
    )
    if mode == "timed":
        _lint_timing(text, sections, issues, duration)
    if max_chars is not None and len(text) > max_chars:
        _add(issues, "LENGTH001", f"Prompt长度{len(text)}超过上限{max_chars}。", text)
    unique = list(dict.fromkeys(issues))
    return Result(unique)


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lint a final Seedance prompt.")
    parser.add_argument("files", nargs="+", help="Prompt file(s); use - for stdin")
    parser.add_argument("--duration", type=float, help="Expected total duration in seconds")
    parser.add_argument("--authority", action="append", default=[], help="Accepted authority source file")
    parser.add_argument("--available-ref", action="append", default=[], help="Actually uploaded ref tag")
    parser.add_argument("--rejected-ref", action="append", default=[], help="Rejected ref tag")
    parser.add_argument("--require-reanchor", help="Ref tag that must own re-anchoring")
    parser.add_argument("--no-invent-optics", action="store_true", help="Reject numeric lens/FOV")
    parser.add_argument("--allow-variants", action="store_true", help="Allow explicit alternatives")
    parser.add_argument("--max-chars", type=int, help="Maximum prompt characters")
    parser.add_argument("--format", choices=("human", "json"), default="human")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    try:
        authority_texts = [_read(path) for path in args.authority]
        results = []
        failed = False
        for path in args.files:
            result = lint_text(
                _read(path),
                duration=args.duration,
                authority_texts=authority_texts,
                available_refs=args.available_ref,
                allow_variants=args.allow_variants,
                no_invent_optics=args.no_invent_optics,
                rejected_refs=args.rejected_ref,
                require_reanchor=args.require_reanchor,
                max_chars=args.max_chars,
            )
            results.append({"file": path, "ok": result.ok, "issues": [asdict(issue) for issue in result.issues]})
            failed = failed or bool(result.errors) or (args.strict and bool(result.issues))
        if args.format == "json":
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            for item in results:
                if not item["issues"]:
                    print(f"PASS {item['file']}")
                    continue
                for issue in item["issues"]:
                    location = f":{issue['line']}" if issue["line"] else ""
                    print(
                        f"{issue['severity'].upper()} {item['file']}{location} "
                        f"{issue['code']} {issue['message']}"
                    )
        return 1 if failed else 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"lint_prompt: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
