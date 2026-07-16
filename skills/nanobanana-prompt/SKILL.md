---
name: nanobanana-prompt
description: >-
  为 Google Nano Banana 图像模型编写可直接复制的高质量提示词，默认面向 Nano Banana Pro（Gemini 3 Pro Image），并在速度、批量、视频输入或 Image Search Grounding 更重要时提示 Nano Banana 2（Gemini 3.1 Flash Image）。当用户提到 Nano Banana、Gemini 生图、AI 出图提示词、海报/产品图/角色一致性/多参考图/带文字图片，或在未指定平台时泛称“帮我写出图提示词”，使用此技能。仅输出提示词和必要参数建议，不直接生成图片；若用户要求实际出图，先用本技能优化提示词，再交给已配置的生成工具。
---

# Nano Banana Prompt

把用户的创意、参考图意图或编辑要求，转换为一条模型可执行、可迭代、可直接复制的提示词。默认用英文提示词以便跨界面复用；用户提供的中文文案、品牌拼写、数字和标点必须原样保留。

## Scope

- 默认目标：`gemini-3-pro-image`（Nano Banana Pro），适合专业资产、复杂指令、文字和高保真编辑。
- 若用户强调速度、批量、超长/超窄比例、视频输入或 Google Image Search Grounding，可建议 `gemini-3.1-flash-image`（Nano Banana 2）。
- 本技能写提示词，不调用 API，不擅自生成图片，不输出未经请求的 API JSON。
- 用户明确要求“用 nano banana 出图”时，先完成提示词，再把它交给已配置的 Nano Banana 生成命令；不要跳过提示词步骤。

## Source Of Truth

- 模型 ID、比例、分辨率、参考图和能力边界：先读 `references/model-specs.md`。
- 用户问“最新/现在/当前”或 API 细节：现场核对 Google 官方 Image Generation 和模型页面。
- 摄影与视觉词汇：按需读 `references/prompt-vocabulary.md`，不要为了显得专业而堆镜头参数。
- 相似场景：按需读 `references/examples.md`，只借结构，不机械复制。
- 角色系列：读 `references/character-consistency.md`。
- 失败修复：读 `references/troubleshooting.md`。

把“官方事实”“本地小样本观察”“写作启发式”分开表达。不要把单次平台实测写成 Gemini 的稳定机制。

## Task Routing

先判断任务类型，可组合使用：

1. **Generate**：从文本生成新图。
2. **Edit**：修改已有图，重点是修改边界与保留项。
3. **Multi-reference**：多图分别提供身份、对象、构图、风格、光影或场景。
4. **Text/layout**：海报、菜单、信息图、界面、标牌等文字与版式任务。
5. **Consistency**：同一角色、产品或场景跨图保持一致。
6. **Grounded visual**：天气、数据、地点或近期事实会影响画面；只在生成面明确支持时建议 Search Grounding。

## Internal Brief

写提示词前在内部整理，不默认展示：

- **Deliverable**：资产类型、用途、受众。
- **Hero**：第一视觉主体是什么。
- **Composition**：景别、机位、主体位置、前中后景、留白。
- **Look**：媒介、灯光、色彩、材质、氛围。
- **Literal content**：必须逐字出现的文字、数字、品牌、符号。
- **Constraint ledger**：`Must include` / `Must change` / `Must preserve` / `Must exclude`。
- **Reference map**：每张图只承担一个主要职责，并说明如何组合、哪些内容不能迁移。

## Prompt Architecture

简单任务用一段自然语言；复杂任务用短段落或轻量标签。不要强迫所有任务套同一语法。

推荐顺序：

1. 最终资产与用途。
2. 主体与可见特征。
3. 构图、动作和空间关系。
4. 环境、时间与光线。
5. 视觉媒介、色彩和材质。
6. 精确文字与版面。
7. 保留项、排除项和其他约束。

### 写作原则

- 用完整、具体、可见的描述；不要只给关键词串。
- 先说明视觉层级，再补装饰细节。复杂场景最好只有一个 hero，其余为 supporting detail。
- 镜头/焦距词只用来表达透视、景别或景深感，不把它们当精确物理模拟保证。
- 不堆 `masterpiece`、`best quality`、`8K` 等空泛质量词；描述真正需要看见的材质、边缘、纹理和版式。
- 语义正向描述适合表达理想状态，例如 `an empty pedestrian street`；但精确限制可以直接写 `no extra text`、`do not alter the logo`。不存在 `negative_prompt` API 字段，不等于自然语言里不能出现否定句。
- 关键约束用清晰句子表达一次。不要依赖 CAPS、重复十遍或“提示词靠前就一定权重更高”这类未经证实的机制。

## Edit Contract

编辑任务优先使用：

```text
Edit the base image to <target result>.
Change only: <smallest requested delta>.
Preserve: <identity, geometry, layout, camera, text, logo, colors, lighting, shadows, surrounding objects>.
Do not alter: <specific collateral changes that would break the result>.
```

- 结果已接近目标时写 delta edit，不要重写整张图。
- 每次迭代都重复最关键的 preserve 项，避免身份、产品结构、构图或文案漂移。
- 一次只修一个问题簇：构图、光线、文字、身份或材质。

## Multi-Reference Contract

多图时写进可复制提示词：

```text
Reference roles: Image 1 is <primary identity/base>. Image 2 provides <style only>. Image 3 provides <composition only>. Create <target>. Preserve <invariants>. Do not import <unwanted subjects/text/layout> from the secondary references.
```

- 禁止只写“融合这些图”。
- 用户最新文字意图优先，其次是 base/identity/object，再其次是 composition/style/lighting。
- 参考图顺序与输出比例遵循用户所在工具的真实上传和参数设置；不要宣称“第一张天然权重最高”或“最后一张决定比例”。
- 参考图上限和高保真类别限制以 `references/model-specs.md` 为准；总数上限与分类能力不要相加误读。

## Exact Text And Layout

- 先确认文字内容，再生成图；复杂文案最好先由用户确认最终 copy。
- 每段精确文字用直引号包裹，并原样保留语言、大小写、数字、标点和品牌拼写。
- 为文字指定角色、位置、字号层级、字体气质、颜色、对比度和留白。
- 不需要其他文字时写 `no other text`。
- 信息图、菜单、UI 先定义阅读顺序和信息结构，再定义风格；语义错误的漂亮图仍然是失败。

## Character And Object Consistency

- 为人物或产品写一个稳定的 identity block，跨场景复用同一组特征词。
- 参考图分别覆盖正面、侧面、全身、材质或关键几何，不要上传大量重复角度。
- 服装是否锁定要明确；只锁脸时，不要让服装描述意外成为永久身份特征。
- 参考图提供视觉证据，文字负责声明哪些证据必须保留、哪些可以变化。

## Model And Parameter Advice

仅在用户需要时给出，放在提示词代码块之外：

- 默认制作偏好：Nano Banana Pro、`2K`；比例按用途，未指定且明显是影视画面时用 `16:9`。
- 快速探索/批量：Nano Banana 2，可先 `1K`，选定方向再升 `2K`/`4K`。
- 用户指定比例、分辨率或平台时，优先遵循用户值。
- API 默认值与本技能的制作偏好不是一回事；准确默认值见 `references/model-specs.md`。
- 不提供 `seed`、`cfg_scale`、`sampler`、`steps` 或 `negative_prompt` 等 Google 原生 API 未定义字段。

## Quality Gate

交付前静默检查：

- 一个清晰 hero 与可读视觉层级。
- 景别、机位、动作、场景、光线、媒介和比例不冲突。
- 精确文字逐字保留并有版式位置。
- 每张参考图有单一主职责，且写明不能迁移的内容。
- 编辑任务同时包含 delta 和 preserve。
- 没有把本地实测概率、图序、CAPS 或相机参数写成模型保证。
- 代码块中只有用户要复制的提示词，没有分析、参数或 JSON。

## Output Format

默认只给一个最优版本：

````markdown
[Prompt]
```text
<copy-ready English prompt only>
```

[中文说明]
<1-3 句说明关键取舍>

[参数建议]
- Model: <仅在有帮助时>
- Aspect ratio: <ratio>
- Resolution: <1K / 2K / 4K>
- References: <角色与数量建议，仅在需要时>
````

- 用户只要 prompt 时，省略说明和参数。
- 用户要求中文 prompt 时直接用中文，不要为了英文而改写原文案。
- 用户明确要多个方向时才提供多个版本。
- 参数与说明永远放在代码块外，保证一键复制干净。

## Reference Index

| 文件 | 用途 |
|---|---|
| `references/model-specs.md` | 当前官方模型、比例、分辨率、参考图和能力边界 |
| `references/prompt-vocabulary.md` | 精准视觉术语与语义替代 |
| `references/examples.md` | 按资产类型参考结构 |
| `references/character-consistency.md` | 角色/对象系列一致性 |
| `references/troubleshooting.md` | 失败诊断与最小修复 |
