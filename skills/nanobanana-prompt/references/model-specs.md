# Nano Banana 官方能力与参数

Last verified: 2026-07-10

本文件只记录 Google 官方 Gemini API 能力。第三方平台（Higgsfield、fal.ai 等）的参数和限制不属于 Google 原生 API；只有用户明确指定平台时才现场核对。

## Official Sources

- Image generation: https://ai.google.dev/gemini-api/docs/image-generation
- Gemini 3 Pro Image: https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image
- Gemini 3.1 Flash Image: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image

## Stable Model IDs

| 产品名 | Stable model ID | 适合 |
|---|---|---|
| Nano Banana Pro | `gemini-3-pro-image` | 专业资产、复杂指令、高保真编辑、文字、Search Grounding |
| Nano Banana 2 | `gemini-3.1-flash-image` | 速度、批量、视频输入、Image Search Grounding、极端比例 |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | 最低延迟/成本，能力与分辨率更受限 |
| Nano Banana（旧） | `gemini-2.5-flash-image` | 旧工作流兼容 |

默认不要再写旧的 `*-preview` ID。用户问特定预览版或迁移兼容时再核对。

## Aspect Ratios

### Gemini 3 Pro Image

官方支持 10 个比例：

`1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9`

### Gemini 3.1 Flash Image

官方支持 14 个比例：

`1:1` `1:4` `1:8` `2:3` `3:2` `3:4` `4:1` `4:3` `4:5` `5:4` `8:1` `9:16` `16:9` `21:9`

`1:4`、`1:8`、`4:1`、`8:1` 是 Flash 能力，不要写成 Pro 的合法比例。

## Image Size

| 模型 | 支持 |
|---|---|
| Pro | `1K` `2K` `4K` |
| Flash | `512`/0.5K、`1K`、`2K`、`4K` |
| Flash Lite | `1K` |

- `K` 必须大写；小写值会被拒绝。
- Gemini 3 图像模型无输入图时默认 `1K`、`1:1`；有输入图时默认匹配输入图尺寸/比例。
- 本技能可按用户制作习惯建议 `2K`，但要标为建议，而不是 API 默认。

## Reference Images

Gemini 3 图像模型最多可混合 14 张参考图。分类能力是“总数 14 内的高保真用途”，不要把各类别简单相加成另一个总数。

| 模型 | 对象高保真 | 角色一致性 | 风格参考 | 总输入参考 |
|---|---:|---:|---:|---:|
| Pro | 最多 6 个对象图 | 最多 5 个角色图 | 最多 3 个风格参考 | 最多 14 张 |
| Flash | 最多 10 个对象图 | 最多 4 个角色图 | 官方表未单列 | 最多 14 张 |
| Flash Lite | 最多 14 个对象图 | 未提供 | 未提供 | 最多 14 张 |

官方限制说明还写到 Pro 在高保真输入上以 5 张表现最佳、总计可达 14 张。实际工作应优先少量、互补、职责清晰的参考，而不是为了碰上限而堆图。

## Current Capabilities

- Pro 与 Flash：图像生成和编辑、最高 4K、文字渲染、对话式多轮编辑、Thinking。
- Pro：Google Search Grounding，适合专业资产和需要事实校验的可视化。
- Flash：Google Web + Image Search Grounding、视频到图像、速度与批量优势。
- 所有生成图片包含 SynthID 水印。
- 图片生成支持中文等多种语言；英文并不是 API 硬要求。

## Text Rendering Guidance

- Google 官方建议先确定文字内容，再请求生成包含这些文字的图像。
- 指定精确文案、字体气质、字号层级、位置、颜色和整体设计。
- 模型仍可能出错；不能承诺 100% 拼写或排版准确。

## Prompting Guidance

- 复杂场景可以拆成步骤，先背景，再主体，再关键元素。
- 使用摄影/电影语言控制构图，但不要把焦距、光圈或视角当严格模拟保证。
- 优先用语义正向描述，例如 `an empty street`；精确编辑中可以直接写 `do not change any other elements`。
- 通过小步多轮编辑迭代，不要把所有修复一次塞进超长提示词。

## API Surface

当前 Google 推荐用 Interactions API 访问最新功能；图像输出配置位于 `response_format` 的图像项中，例如 `aspect_ratio` 和 `image_size`。用户只要提示词时不要输出 API 配置。

不要在 Google 原生 API 建议中编造：

- `negative_prompt`
- `seed`
- `cfg_scale`
- `sampler`
- `steps`

第三方平台可能提供同名字段，但那是平台能力，必须单独标注并现场核对。
