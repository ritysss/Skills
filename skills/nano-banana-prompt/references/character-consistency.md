# 角色一致性工作流

在多张图片中保持同一角色外观一致，是 Nano Banana Pro 的核心应用场景之一。

---

## Pro 模型参考图限制

| 类型 | 最大数量 | 用途 |
|------|---------|------|
| 角色图（Character） | **5 张** | 保持人物外观一致 |
| 对象图（Object） | **6 张** | 保持物品外观一致（高保真度） |
| 总计 | **14 张** | 硬上限 |

对比 Flash：角色图 ≤4 张，对象图 ≤10 张，总计 ≤14 张。

---

## 360° 角色表制作

角色一致性的基础是一组高质量的角色参考图（Character Sheet）。

### 推荐角度组合

| 组合 | 角度 | 适用 |
|------|------|------|
| 基础组（2-3 张） | 正面 / 45° 侧面 / 全身 | 简单场景，角色特征明确 |
| 标准组（4-5 张） | 正面 / 左45° / 右45° / 90°侧面 / 全身 | 多数场景（Pro 角色图上限 5 张） |

### 角色表生成提示词模板

如果需要从零创建角色参考，可用以下提示词生成角色表：

> "Character reference sheet of [角色描述], showing front view, 45-degree view, and side profile, all on a clean white background with consistent studio lighting. The character has [具体特征]. Full body shown in the bottom row, upper body portraits in the top row. Clean, detailed, reference sheet style."

---

## 参考图质量建议

| 要求 | 说明 |
|------|------|
| 光线一致 | 所有参考图使用相似的光线条件 |
| 背景简洁 | 纯色或简单背景，避免杂乱元素干扰模型识别 |
| 主体清晰 | 无运动模糊、无遮挡、面部清晰可见 |
| 格式 | JPEG / PNG / WebP |

**注意**：官方文档未明确给出参考图的最低/最优分辨率要求。建议使用尽可能高清的图片。

---

## 提示词一致性锚定

**核心原则：在所有图片的提示词中，使用完全相同的角色描述段落。**

### 锚定词规则

1. **选定后不要改变**：决定了 "emerald eyes" 就不要在其他图里用 "green eyes"
2. **具体优于模糊**：用 "wavy auburn hair past her shoulders" 而非 "red hair"
3. **完整描述**：每个提示词都包含完整的角色描述，不要省略

### 锚定模板

在每个提示词的开头，保持完全一致的角色描述块：

```
A [年龄]-year-old [性别] with [发型发色], [面部特征], wearing [服装详细描述] and [配饰].
```

示例：
```
A 30-year-old woman with wavy auburn hair past her shoulders, light freckles across the bridge of her nose, wearing a cream cable-knit sweater and small gold hoop earrings.
```

这段描述在每个场景的提示词中**原封不动复用**，只改变后续的动作、场景、构图部分。

---

## 多角色场景

当画面中有多个角色时：

1. **分别定义**：每个角色有独立的完整描述段落
2. **空间定位**：明确每个角色在画面中的位置（"on the left" / "in the center" / "background right"）
3. **互动描述**：描述角色之间的关系和互动

示例：
> "On the left, a 30-year-old woman with wavy auburn hair... On the right, a 35-year-old man with close-cropped black hair and a trimmed beard, wearing a charcoal wool coat... They face each other across a small cafe table, both leaning forward slightly in conversation."

---

## 常见失败模式

| 问题 | 原因 | 修复 |
|------|------|------|
| 角色面部不一致 | 参考图角度不够 | 增加参考图角度覆盖（Pro 最多 5 张角色图） |
| 发色/发型漂移 | 描述词不一致 | 检查所有提示词中发型描述是否逐字相同 |
| 服装变化 | 描述中省略了服装 | 每个提示词都包含完整服装描述 |
| 体型变化 | 未描述体型 | 在角色描述中加入体型信息 |
| 配饰丢失 | 配饰描述被后续内容权重压过 | 将配饰放在角色描述的显著位置（靠前） |
| 参考图间风格差异 | 参考图拍摄条件不一致 | 重新准备光线和背景一致的参考图 |

---

## 工作流总结

1. **准备参考图**：2-5 张多角度、光线一致、高清的角色照片（Pro 角色图上限 5 张）
2. **撰写锚定描述**：一段完整、具体、不可变的角色描述文字
3. **复用到每个场景**：每个新提示词的开头复制完整锚定描述
4. **只改变场景部分**：动作、环境、构图、光线可以变，角色描述不变
5. **保持风格锚点**：所有图使用相同的胶片/风格参考（如 "Fuji Pro 400H film look"）
