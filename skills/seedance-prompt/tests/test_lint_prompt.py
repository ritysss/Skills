from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lint_prompt import lint_text  # noqa: E402


def single_prompt(
    *,
    camera: str = (
        "中近景，人物位于画面中央偏右，前景为虚化雨滴，背景为湿润街面；"
        "85mm中长焦，眼平机位，摄影机缓慢横移，云台稳定，焦点锁定眼睛。"
    ),
) -> str:
    return f"""[主体] 黑色短发女性穿黑色风衣，站在雨后的街口，起始时双脚稳定落地并正对街道。
[动作] 她停住脚步，右手压住领口，随后缓慢回头并与镜头对视。
[镜头] {camera}
[风格] 写实电影感，冷蓝环境光，35mm胶片质感，自然颗粒。
[约束] 人物面孔稳定，脚位保持同一地面接触点，动作连贯，白平衡稳定。
[音频] 无BGM，保留雨声、远处车流声和衣料摩擦声。
"""


def timed_prompt(*, second_start: str = "0:04", final_end: str = "0:13.9") -> str:
    return f"""【分镜】
镜头1 [0:00-0:04]：中景，手端起咖啡；35mm广角，固定机位，焦点锁定杯子。
镜头2 [{second_start}-0:08]：中近景，人物走向窗边；50mm标准镜头，平稳跟拍，焦点锁定人物。
镜头3 [0:08-{final_end}]：特写，咖啡杯放上窗台；85mm中长焦，三脚架稳定，焦点转到雨滴。

【跨镜头一致性】
白色陶瓷杯、木窗台、曝光和白平衡跨镜头保持一致。

【音频】
无BGM，保留杯子轻放声、室内底噪和窗外细雨声。
"""


def sequential_prompt() -> str:
    return """【分镜】
镜头1：远景，人物推门进入厨房；35mm广角，固定机位。
镜头2：中近景，人物端起咖啡看向窗外；50mm标准镜头，缓慢侧移。
镜头3：特写，杯底落在木窗台；85mm中长焦，焦点锁定杯底接触点。
转场：镜头之间直接硬切。

【音频】
无BGM，保留门轴声、脚步声、杯子轻放声和室内底噪。
"""


def ref_prompt() -> str:
    return """[主体] @图片1锁定人物身份、面孔、服装与街机厅物理场景；女孩站在街机前，手指停在按钮上。
[动作] 她保持脚位不动，手指轻压按钮，随后缓慢抬眼。
[镜头] @图片1锁定首帧构图、原始透视和眼平机位；中近景，人物位于画面中央，摄影机缓慢后退约10%，焦点锁定眼睛。
[风格] 写实电影感，冷白屏幕光，细腻颗粒。
[约束] 面部结构稳定，动作连贯，街机按键与手指接触稳定，白平衡稳定。
[音频] 无BGM，保留街机厅底噪和按键声。
"""


class PromptLintTests(unittest.TestCase):
    def codes(self, text: str, **kwargs) -> set[str]:
        return {issue.code for issue in lint_text(text, **kwargs).issues}

    def test_valid_single_passes(self) -> None:
        self.assertTrue(lint_text(single_prompt()).ok)

    def test_single_uses_no_outer_wrapper(self) -> None:
        self.assertFalse(any(label in single_prompt() for label in ("【基础设定】", "【提示词】")))

    def test_style_35mm_is_not_a_second_lens(self) -> None:
        self.assertNotIn("OPTICS001", self.codes(single_prompt()))

    def test_single_timed_words_do_not_make_multishot_contract(self) -> None:
        prompt = single_prompt().replace(
            "她停住脚步，右手压住领口，随后缓慢回头并与镜头对视。",
            "第1秒停住，第3秒压住领口，第5秒缓慢回头并与镜头对视。",
        )
        self.assertNotIn("CONTRACT001", self.codes(prompt))

    def test_valid_timed_prompt_passes(self) -> None:
        self.assertTrue(lint_text(timed_prompt()).ok)

    def test_valid_sequential_prompt_passes(self) -> None:
        self.assertTrue(lint_text(sequential_prompt()).ok)

    def test_cross_shot_continuity_is_optional(self) -> None:
        prompt = timed_prompt().replace(
            "\n【跨镜头一致性】\n白色陶瓷杯、木窗台、曝光和白平衡跨镜头保持一致。\n",
            "",
        )
        self.assertTrue(lint_text(prompt).ok)

    def test_mixed_timed_and_untimed_shots_are_rejected(self) -> None:
        prompt = timed_prompt().replace("镜头2 [0:04-0:08]：", "镜头2：")
        self.assertIn("CONTRACT003", self.codes(prompt))

    def test_different_lenses_across_shots_are_valid(self) -> None:
        self.assertNotIn("OPTICS001", self.codes(timed_prompt()))

    def test_cross_shot_optics_rejects_conflicting_lens(self) -> None:
        prompt = timed_prompt().replace(
            "白色陶瓷杯、木窗台、曝光和白平衡跨镜头保持一致。",
            "全段保持35mm镜头关系；白色陶瓷杯、木窗台、曝光和白平衡跨镜头保持一致。",
        )
        self.assertIn("OPTICS004", self.codes(prompt))

    def test_unresolved_or_is_rejected(self) -> None:
        prompt = single_prompt().replace("右手压住领口", "右膝或左手先触地")
        self.assertIn("ALT001", self.codes(prompt))

    def test_negative_exclusion_list_is_not_an_alternative(self) -> None:
        prompt = single_prompt().replace(
            "人物面孔稳定",
            "不新增推拉、摇镜或快速变焦，人物面孔稳定",
        )
        self.assertNotIn("ALT001", self.codes(prompt))

    def test_ab_variant_is_rejected(self) -> None:
        prompt = single_prompt().replace("随后缓慢回头", "随后执行方案A/B")
        self.assertIn("ALT001", self.codes(prompt))

    def test_contract_mixing_is_rejected(self) -> None:
        prompt = single_prompt() + "\n【分镜】\n镜头1：中景，固定机位。\n【音频】\n无BGM。"
        self.assertIn("CONTRACT001", self.codes(prompt))

    def test_missing_audio_is_rejected(self) -> None:
        prompt = single_prompt().replace("[音频] 无BGM，保留雨声、远处车流声和衣料摩擦声。", "")
        self.assertIn("AUDIO001", self.codes(prompt))

    def test_wrong_field_order_is_rejected(self) -> None:
        prompt = single_prompt().replace("[主体]", "[临时]").replace("[动作]", "[主体]").replace("[临时]", "[动作]")
        self.assertIn("CONTRACT003", self.codes(prompt))

    def test_duplicate_field_is_rejected(self) -> None:
        prompt = single_prompt().replace("[动作]", "[主体] 重复主体。\n[动作]")
        self.assertIn("CONTRACT003", self.codes(prompt))

    def test_legacy_single_wrapper_is_rejected(self) -> None:
        prompt = "【基础设定】\n雨夜街口。\n\n【提示词】\n" + single_prompt()
        self.assertIn("CONTRACT001", self.codes(prompt))

    def test_legacy_global_lock_is_rejected(self) -> None:
        prompt = timed_prompt().replace("【跨镜头一致性】", "【全局锁】")
        self.assertIn("CONTRACT001", self.codes(prompt))

    def test_conflicting_lenses_inside_one_shot_are_rejected(self) -> None:
        prompt = single_prompt(camera="中近景，24mm广角起步，随后35mm镜头，眼平固定机位。")
        self.assertIn("OPTICS001", self.codes(prompt))

    def test_lens_plus_single_fov_is_valid(self) -> None:
        prompt = single_prompt(camera="中近景，35mm广角/约63度视场，眼平固定机位，焦点锁定眼睛。")
        self.assertNotIn("OPTICS001", self.codes(prompt))
        self.assertNotIn("OPTICS002", self.codes(prompt))

    def test_numeric_optics_outside_camera_field_is_rejected(self) -> None:
        prompt = single_prompt().replace("黑色风衣", "黑色风衣，采用24mm镜头关系")
        self.assertIn("OWNER001", self.codes(prompt))

    def test_inline_reference_roles_pass(self) -> None:
        self.assertTrue(lint_text(ref_prompt()).ok)

    def test_unscoped_reference_use_is_rejected(self) -> None:
        prompt = ref_prompt().replace("她保持脚位不动", "她先看向@图片2，再保持脚位不动")
        self.assertIn("REF003", self.codes(prompt))

    def test_all_documented_examples_pass_linter(self) -> None:
        examples = (ROOT / "references" / "examples.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```text\n(.*?)\n```", examples, re.DOTALL)
        self.assertGreaterEqual(len(blocks), 7)
        for index, block in enumerate(blocks, start=1):
            result = lint_text(block)
            self.assertTrue(result.ok, f"example {index}: {result.issues}")

    def test_available_reference_boundary_is_exact(self) -> None:
        self.assertIn("REF005", self.codes(ref_prompt(), available_refs={"@图片3"}))

    def test_timeline_overlap_is_rejected(self) -> None:
        self.assertIn("TIME005", self.codes(timed_prompt(second_start="0:03.5")))

    def test_timeline_gap_is_rejected(self) -> None:
        self.assertIn("TIME005", self.codes(timed_prompt(second_start="0:04.5")))

    def test_duration_tolerance_accepts_13_9_for_14_seconds(self) -> None:
        self.assertNotIn("TIME006", self.codes(timed_prompt(final_end="0:13.9"), duration=14))

    def test_duration_mismatch_is_rejected(self) -> None:
        self.assertIn("TIME006", self.codes(timed_prompt(final_end="0:12.5"), duration=14))

    def test_sequential_shot_numbering_is_checked(self) -> None:
        prompt = sequential_prompt().replace("镜头2：", "镜头3：", 1)
        self.assertIn("TIME004", self.codes(prompt))

    def test_authority_catches_35mm_replaced_by_24mm(self) -> None:
        authority = "[镜头] 35mm写实电影镜头感，焦点锁定人物。\n[风格] 35mm胶片质感。"
        prompt = single_prompt(camera="中近景，24mm广角，眼平固定机位，焦点锁定眼睛。")
        self.assertIn("AUTH002", self.codes(prompt, authority_texts=[authority]))

    def test_no_invent_optics_rejects_unsourced_number(self) -> None:
        self.assertIn("OPTICS003", self.codes(single_prompt(), no_invent_optics=True))

    def test_rejected_take_must_be_absent_from_final_prompt(self) -> None:
        prompt = ref_prompt().replace(
            "[约束]",
            "[约束] @视频2锁定人物身份会污染当前版本；",
        )
        self.assertIn("CANON001", self.codes(prompt, rejected_refs={"@视频2"}))

    def test_inline_reanchor_is_accepted(self) -> None:
        prompt = ref_prompt().replace(
            "@图片1锁定首帧构图、原始透视和眼平机位",
            "@图片2作为本次第0帧、起始构图和起始接触状态的重锚",
        )
        codes = self.codes(prompt, require_reanchor="@图片2")
        self.assertNotIn("CANON002", codes)

    def test_missing_reanchor_is_rejected(self) -> None:
        self.assertIn("CANON002", self.codes(ref_prompt(), require_reanchor="@图片2"))


if __name__ == "__main__":
    unittest.main()
