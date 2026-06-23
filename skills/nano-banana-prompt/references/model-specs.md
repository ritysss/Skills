# Nano Banana Pro 硬参数表

所有参数来自 Google 官方文档，不包含推测值。

## 模型标识

| 名称 | API 模型 ID | 定位 |
|------|------------|------|
| Nano Banana Pro | `gemini-3-pro-image` | 专业资产 / 高保真 / 文字渲染 |
| Nano Banana 2 (Flash) | `gemini-3.1-flash-image` | 速度 / 高容量 / 可控思考 |
| Nano Banana (旧版) | `gemini-2.5-flash-image` | 速度 / 低延迟 |

## 宽高比

常用比例以当前官方文档或当前 provider 为准。Flash 额外支持极端比例；Pro 工作流默认优先选择常见生产比例。

| 宽高比 | 方向 | 推荐用途 |
|--------|------|---------|
| `1:1` | 方形 | 产品图、头像、Instagram、电商主图 |
| `2:3` | 竖版 | 杂志封面、人像摄影、Pinterest |
| `3:2` | 横版 | 经典摄影比例、桌面壁纸 |
| `3:4` | 竖版 | 书籍封面、竖版海报 |
| `4:3` | 横版 | 传统显示器、PPT 配图 |
| `4:5` | 竖版 | Instagram 竖版、小红书封面 |
| `5:4` | 横版 | 大幅印刷 |
| `9:16` | 竖版 | 抖音/Reels/手机壁纸 |
| `16:9` | 横版 | 电影感、YouTube 封面、宽屏 |
| `21:9` | 超宽 | 电影级宽银幕、网站 Hero 图 |

Flash 额外可用的极端比例包括：`1:4`、`4:1`、`1:8`、`8:1`。只有在当前 provider 明确支持时才推荐这些比例。

**常用推荐**：
- 社交媒体竖版：`9:16`（抖音/Reels）或 `4:5`（小红书/Instagram）
- 电影感横版：`16:9` 或 `21:9`
- 产品方图：`1:1`
- 海报竖版：`2:3` 或 `3:4`

## 分辨率

| 值 | 适用场景 | 注意事项 |
|------|---------|---------|
| `1K` | 快速测试、概念验证 | 大写 K |
| `2K` | 日常使用、社交媒体（推荐默认） | 大写 K |
| `4K` | 精细需求、印刷品、产品特写 | 大写 K |
| `512` | 快速草稿、缩略图 | Flash/当前 provider 支持时使用，无 K 后缀 |

**关键警告**：K **必须大写**。小写 `2k` / `4k` 会被 API 拒绝。`512` 是唯一不带 K 的值，且不要当作 Pro 默认分辨率。

## 响应模式

| 值 | 用途 |
|------|------|
| `["IMAGE"]` | 纯图输出（推荐默认） |
| `["TEXT", "IMAGE"]` | 图 + 文字解释 |

## 参考图规格（Pro 专属）

| 类型 | 最大数量 | 用途 |
|------|---------|------|
| 对象图（Object） | 6 张 | 保持物品外观一致（高保真度） |
| 角色图（Character） | 5 张 | 保持人物外观一致 |
| **总计** | **14 张** | 硬上限 |

### 参考图质量建议（非官方硬性要求）
- 光线均匀，避免过曝/欠曝
- 主体清晰，无运动模糊
- 背景简洁，避免杂乱
- 多张参考图之间光线风格尽量一致
- 格式：JPEG / PNG / WebP（来自 Files API 支持列表）

## 思考配置（仅 Flash 可用）

**重要：`thinking_config` 仅适用于 `gemini-3.1-flash-image`（Flash），不适用于 Pro。**

```python
# 仅 Flash
thinking_config=types.ThinkingConfig(
    thinking_level="High",    # "minimal" 或 "High"
    include_thoughts=True     # 返回思考过程
)
```

- Flash + High thinking 适合文字渲染和复杂构图
- 思考 tokens 无论 includeThoughts 是否为 true 都会计费
- Pro 默认启用思考，无法调整

## 图片编辑端点（fal.ai）

fal.ai 提供独立的图片编辑端点：

| 参数 | 说明 |
|------|------|
| 端点 | `fal-ai/nano-banana-pro/edit` |
| `image_urls` | 参考图像 URL 列表，**最多 14 张** |
| `seed` | 随机种子（**仅 fal.ai 平台支持**，Google 原生 API 不支持） |
| `safety_tolerance` | 内容审核级别（1=最严格，6=最宽松） |

**注意**：Higgsfield 等消费者平台基于此 API，图片上传能力对应 `image_urls` 参数的 14 张限制。

## Nano Banana 2（Gemini 3.1 Flash Image）

Nano Banana 2 / Gemini 3.1 Flash Image 适合快速迭代和批量测试：

| 对比 | Pro | Nano Banana 2 (Flash) |
|------|-----|----------------------|
| 速度 | 基准 | 更适合高容量快速迭代 |
| 成本 | 以当前官方价格/当前 provider 为准 | 以当前官方价格/当前 provider 为准 |
| 新增比例/尺寸 | 常用比例，`1K`/`2K`/`4K` | `4:1` `1:4` `8:1` `1:8`，并支持 `512` |
| 定位 | 最终成品 | 快速迭代、批量测试 |

## 严格禁止的参数

以下参数在 Google 原生 API 中**不存在**：

| 参数 | 状态 |
|------|------|
| `negative_prompt` | ❌ 不存在 |
| `cfg_scale` | ❌ 不存在 |
| `sampler` | ❌ 不存在 |
| `steps` | ❌ 不存在 |

## Google Search Grounding

提示中可使用 `google_search` 工具启用搜索接地，引用真实世界信息（地标/人物/品牌），减少事实性幻觉。

```python
tools=[{"google_search": {}}]
```

## SynthID 水印

所有生成的图片自动嵌入 SynthID 不可见水印。

## Pro vs Flash 选择指南

| | Pro | Flash |
|---|---|---|
| 模型 ID | `gemini-3-pro-image` | `gemini-3.1-flash-image` |
| 质量 | 最高保真 | 良好 |
| 速度 | 较慢 | 快 |
| 文字渲染 | 优秀 | 良好（配合 High thinking 更优） |
| 思考可控 | ❌ 不可调 | ✅ minimal / High |
| 对象参考图 | ≤6 张 | ≤10 张 |
| 角色参考图 | ≤5 张 | ≤4 张 |
| 推荐场景 | 最终成品、专业资产、精细需求 | 快速迭代、批量测试、需要控制思考等级 |
