# Nano Banana Pro 故障排查

常见失败模式、原因诊断和修复方法。

---

## 快速诊断表

| 问题 | 常见原因 | 修复方法 |
|------|---------|---------|
| **文字渲染错误/乱码** | 未用双引号包裹文字；未指定字体风格 | 双引号包裹所有画面文字 + 指定字体风格/大小/位置/颜色 |
| **风格漂移/不统一** | 堆叠了多个矛盾风格 | 选单一风格锚点（如 "Kodak Portra 400"），删除其他风格 |
| **角色不一致** | 参考图不足；不同提示词中角色描述有差异 | 增加参考图 + 统一所有提示词中的角色锚定描述（逐字一致） |
| **构图偏差** | 镜头/角度描述模糊 | 明确指定焦距（"85mm"）、角度（"low three-quarter angle"）、景别（"medium close-up"） |
| **画面杂乱** | 描述了太多细节导致歧义 | 简化主体，减少背景描述，主体描述放最前面 |
| **分辨率异常低** | 使用了小写 "4k" | 改为大写 "4K"（K 必须大写） |
| **矛盾元素同时出现** | 提示词中自相矛盾 | 检查每个维度只选一个方向 |
| **背景抢主体** | 背景描述过于详细 | 将主体描述放最前面（排序=权重），简化背景 |
| **色调不对** | 胶片/色彩描述冲突 | 选一个胶片参考 + 一个色调方向 |
| **人物表情不对** | 描述太抽象 | 用具体动作替代抽象情绪（"resting chin on hand, gazing downward" 而非 "looking sad"） |
| **排除元素仍出现** | 误用了 negative prompt 思路 | 不存在 negative_prompt，用语义正向替代（见词库） |
| **API 报参数错误** | 使用了不存在的参数 | 检查是否误用了 seed/cfg_scale/sampler/steps/negative_prompt |

---

## 实测验证：提示词控制力等级表（2026-03-12 Higgsfield 实测）

基于 5 个极限测试、13 张实际出图的一手数据。

### 控制力排序（从强到弱）

| 等级 | 控制维度 | 有效性 | 实测证据 |
|------|---------|--------|---------|
| 🟢 S | **风格锚点**（胶片/渲染风格） | ★★★★★ | Portra 400 / Pro 400H / "isometric 3D render" 每次精准命中，色彩科学高度一致 |
| 🟢 S | **光线方向 + 色温** | ★★★★★ | golden hour 侧光、neon magenta+cyan、tungsten+fluorescent 冷暖分区——全部精准执行 |
| 🟢 S | **文字渲染**（双引号包裹） | ★★★★★ | "NEON GHOST" + "Every light casts a shadow" 在 4 张图中拼写 100% 正确，字体样式到位 |
| 🟢 S | **色彩调性** | ★★★★★ | 暖琥珀/冷蓝霓虹/粉蜡笔 三种极端色调全部精确还原 |
| 🟢 S | **风格切换** | ★★★★★ | 写实摄影 ↔ 3D 渲染 零交叉污染，干净切换 |
| 🟡 A | **多角色动作分配** | ★★★★☆ | 4 人（读报/拍照/吃面/做菜）各做不同事能清晰区分，偶有细微动作归属偏差 |
| 🟡 A | **材质渲染** | ★★★★☆ | 蜂蜜透光、无花果籽粒、面包气孔极好；"做旧/氧化"程度偏弱，倾向渲染为较新状态 |
| 🟡 A | **版面空间分区** | ★★★★☆ | "上 2/3 画面 + 下 1/3 文字"基本遵守；精确比例偶有 ±10% 偏差 |
| 🟡 A | **镜头焦距** | ★★★★☆ | 28mm 广角畸变、85mm 背景压缩 均正确；但不如光线控制精确 |
| 🟡 B | **构图角度** | ★★★☆☆ | 模型有"美学偏置"——会自动修正到它认为更好看的角度。俯拍食物 → 自动改为 45° 斜俯 |
| 🔴 C | **微动作 / 微表情** | ★★★☆☆ | 手部姿态、嘴唇开合、视线方向命中率约 50%。大动作（读报/吃面）好，微动作（手搭包带/嘴唇微张）弱 |
| 🔴 C | **选择性焦点** | ★★☆☆☆ | 多主体时无法精确指定"谁清晰谁模糊"，模型倾向让所有主要人物保持清晰 |

### 写作策略建议

- **字数预算优先分配给 🟢 S 级维度**——风格锚点、光线、色彩这些写越详细越好
- **🟡 A 级正常描述**——镜头/构图/材质正常写即可
- **🔴 C 级简写或省略**——微表情、精确焦点分配写了也大概率被忽略，不如把字数省出来
- **对抗美学偏置**：需要精确视角时，用强化措辞（"strictly 90-degree overhead, camera pointing straight down"）而非普通描述（"overhead view"）

---

## 详细排查指南

### 文字渲染问题

Nano Banana Pro 的文字渲染能力强大，但对格式要求严格。

**检查清单**：
- [ ] 文字是否用英文双引号包裹？（`"SUMMER SALE"` ✅ / `SUMMER SALE` ❌）
- [ ] 是否指定了字体风格？（sans-serif / serif / handwritten / monospace）
- [ ] 是否指定了文字大小？（bold / large / small / headline-sized）
- [ ] 是否指定了位置？（centered at top / bottom-left / overlaid on...）
- [ ] 是否指定了颜色？（white / black / gold / ...）
- [ ] 如果效果仍不理想，考虑用 Flash + High thinking 替代（仅在当前 provider 支持时）

**修复模板**：
> `...the bold [颜色] text "[文字内容]" in a [大小] [字体风格] typeface, [位置描述]...`

### 风格漂移

当生成的图片风格不稳定或偏离预期。

**常见冲突组合**：
- ❌ "Kodak Portra 400 warm tones" + "Fuji Velvia saturated colors"
- ❌ "soft diffused light" + "harsh dramatic shadows"
- ❌ "vintage film grain" + "ultra-sharp digital medium format"
- ❌ "minimalist clean" + "maximalist detailed ornate"

**修复原则**：选一个风格锚点，删除所有与之矛盾的描述。

### 构图问题

画面布局不符合预期。

**诊断**：
- 镜头描述是否明确？模糊的 "close-up" 不如 "85mm medium close-up from a low three-quarter angle"
- 是否指定了景深？没有景深描述时模型会自行决定
- 多元素场景是否指定了空间关系？（"on the left" / "in the background" / "occupying the upper third"）

### 角色一致性失败

多张图中同一角色外观不同。

**诊断**：
1. 比较所有提示词中的角色描述段落——是否逐字相同？
2. 参考图是否足够？（Pro: 角色图最多 5 张，对象图最多 6 张）
3. 参考图之间光线是否一致？
4. 是否混用了近义词？（"emerald eyes" vs "green eyes"）

详见 `references/character-consistency.md`。

### 排除元素仍出现

**核心原因**：Nano Banana Pro 不支持 negative_prompt 参数。

**修复**：参考 `references/prompt-vocabulary.md` 中的语义负向替代表，将"不要X"转为正向描述。

例：
- ❌ 思路：写 "no blur, no noise, no distortion"
- ✅ 做法：写 "tack-sharp focus across the frame, clean noise-free image, optically corrected"

---

## 预防性最佳实践

1. **从简单开始**：先用最少描述生成基础版，再通过迭代编辑添加细节
2. **一次测一个变量**：修改提示词时只改一个维度，观察效果
3. **遵循五段叙事法**：Subject → Composition → Action → Setting → Style 的顺序自然避免大部分问题
4. **用语义正向替代**：永远不要写 "no..." "avoid..." "don't..."，转为正向描述
5. **利用迭代编辑**：80% 满意时修改优于重新生成
6. **保存有效提示词**：好的提示词是可复用的资产
7. **只用官方参数**：不要猜测 seed/cfg_scale 等不存在的参数
