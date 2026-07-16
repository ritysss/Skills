# NanoBanana Pro 提示词示例库

每个示例包含：分析 + 英文提示词 + 中文说明 + 参数建议。只借结构，不把其中的镜头、分辨率或本地小样本结果当成所有任务的默认值。

---

## 1. 电影感人像

**测试能力**：写实摄影模板 + Subject + Style + 胶片质感

【分析】
写实摄影类型，选用 Photorealistic 模板。以人像为核心，Kodak Portra 400 作为单一风格锚点，85mm 人像镜头 + 伦勃朗光营造电影氛围。

【Prompt】
A 25-year-old East Asian woman with shoulder-length black hair sits in a dimly lit jazz bar, resting her chin on one hand while the other cradles a half-finished glass of whiskey. The camera captures her from a three-quarter angle at medium close-up range, shot on an 85mm portrait lens with an f/1.8 aperture creating a creamy bokeh of amber bar lights behind her. A single warm spotlight above casts Rembrandt lighting on her face, highlighting her contemplative expression. The scene is bathed in deep amber and shadow tones. Shot on Kodak Portra 400 with visible natural grain, cinematic mood, shallow depth of field.

【中文说明】
一位年轻亚洲女性坐在昏暗爵士酒吧里，单手托腮，另一手拿着威士忌。85mm 人像镜头 + 伦勃朗光 + Portra 400 胶片质感，电影感氛围。

【参数建议】
- 宽高比：16:9
- 分辨率：4K

【可调整方向】
- 把灯光改为 blue hour 冷色调增加忧郁感
- 换成 Cinestill 800T 胶片获得霓虹光晕效果
- 改为 over-the-shoulder 过肩视角增加叙事感

---

## 2. 产品图 + 文字渲染

**测试能力**：产品摄影模板 + Text rendering

【分析】
产品摄影 + 文字渲染复合需求。用 Product Mockup 模板为主体，Text Rendering 模板处理文字。文字用双引号包裹并指定字体。

【Prompt】
A high-resolution, studio-lit product photograph of a pair of pristine white leather sneakers placed on a polished concrete pedestal against a seamless light gray gradient background. The shoes are positioned at a dynamic 45-degree angle with the left shoe slightly overlapping the right, revealing the textured sole pattern. Lighting is a classic three-point setup with a soft key light from the upper left, a subtle fill from the right, and a rim light separating the shoes from the background. Ultra-realistic, sharp focus on the stitching and material texture. Above the sneakers, bold white text reads "AIR STEP 2026" in a clean geometric sans-serif typeface, with smaller text below reading "Engineered for comfort" in light gray italics.

【中文说明】
白色运动鞋产品图，水泥底座上，灰色渐变背景。三点布光，干净现代。顶部有品牌文字 "AIR STEP 2026" 和副标题。

【参数建议】
- 宽高比：1:1
- 分辨率：4K

【可调整方向】
- 换成悬浮产品构图（floating product）增加动感
- 背景改为生活场景（contextual lifestyle）
- 去掉文字做纯产品图

---

## 3. 电影海报排版

**测试能力**：Text Rendering + 暗调氛围 + 版面分区 + 多层文字

【分析】
海报设计需要精确的文字渲染和版面控制。标题和副标题用双引号包裹，明确空间分区。选择 neo-noir 暗调风格测试冷色控制。

【Prompt】
A cinematic vertical movie poster for a neo-noir thriller. The upper two-thirds depict a lone figure in a long dark trench coat standing at the end of a rain-soaked Tokyo alley at night, seen from behind in a low-angle full-body shot. Neon signs in magenta and cyan reflect off the wet asphalt in long streaks, and dense steam rises from a manhole grate, partially obscuring the figure's legs. The lower third is reserved for typography: the title "NEON GHOST" in large, weathered metallic chrome block letters with a subtle cyan glow along the edges, centered horizontally. Beneath it, the tagline "Every light casts a shadow" in thin white uppercase sans-serif letters with wide tracking. The overall palette is deep midnight blue and electric magenta with desaturated midtones. A horizontal anamorphic lens flare streaks across the upper portion. Fine film grain overlay, high contrast, dramatic volumetric lighting from the neon signs above.

【中文说明】
Neo-noir 电影海报。上 2/3 是雨夜东京小巷中的风衣人物背影，品红+青色霓虹灯倒映在湿沥青上。下 1/3 排版区：标题 "NEON GHOST"（铬金属质感+青色发光）+ 副标题。深蓝与品红霓虹对比。

【参数建议】
- 宽高比：2:3
- 分辨率：4K

【本地样本记录】（2026-03-12 Higgsfield，4 张；不代表稳定命中率）
- 文字渲染：该批次标题和副标题 4/4 拼写正确，金属质感到位
- 版面分区：上 2/3 + 下 1/3 严格遵守
- 暗调氛围：深蓝+品红霓虹精准还原
- 意外收获：模型自动补充了电影信用块（导演/演员/上映日期）
- 注意：标题文字可能泄漏到场景霓虹招牌中

【可调整方向】
- 改为横版 16:9 做网站 Hero Banner
- 增加更多排版元素（导演名、上映日期）
- 换色调为全冷色调增加孤独感

---

## 4. 角色一致性系列

**测试能力**：Photorealistic 模板 + 角色锚定 + 场景切换

【分析】
角色一致性关键：锚定描述段落完全一致，只改变场景和动作。统一 Fuji Pro 400H 风格锚点。

【Prompt — 场景 A：咖啡店】
A 30-year-old woman with wavy auburn hair past her shoulders, light freckles across the bridge of her nose, wearing a cream cable-knit sweater and small gold hoop earrings. She sits at a wooden cafe table near a rain-streaked window, both hands wrapped around a ceramic latte cup, smiling gently downward. Shot from medium close-up at eye level, 50mm standard lens, f/2.8 shallow depth of field blurring the rainy street outside. Soft overcast natural light from the window, warm interior tones. Fuji Pro 400H film look, pastel and muted color palette.

【Prompt — 场景 B：书店】
A 30-year-old woman with wavy auburn hair past her shoulders, light freckles across the bridge of her nose, wearing a cream cable-knit sweater and small gold hoop earrings. She stands in a narrow bookshop aisle, pulling a hardcover book from a high shelf, looking up with curious eyes. Shot from a low three-quarter angle at medium shot range, 35mm wide-angle lens, f/4 moderate depth of field showing rows of colorful book spines receding behind her. Warm tungsten overhead lighting mixed with daylight from a skylight above. Fuji Pro 400H film look, pastel and muted color palette.

【中文说明】
同一角色（波浪红发、雀斑、奶油色毛衣、金色耳环）在两个场景。角色描述段完全一致，只改动作/场景/构图。Fuji Pro 400H 统一风格。

【参数建议】
- 宽高比：3:2
- 分辨率：2K
- 参考图：建议 4-5 张角色参考（正面/45度/侧面/全身）

【可调整方向】
- 增加第三个场景（雨中街头）测试一致性
- 换衣服但保持面部特征描述不变
- 用 4K 分辨率获取更高保真度

---

## 5. 城市风光

**测试能力**：Photorealistic 模板 + Composition + Setting + 氛围

【分析】
风景类，侧重构图和氛围。24mm 广角 + 深景深覆盖全景，蓝色时刻作为时间锚点。

【Prompt】
A sweeping aerial view of Tokyo's Shibuya district at blue hour, captured from a high vantage point looking down at the iconic scramble crossing. Thousands of pedestrians create streaks of motion blur against the glowing crosswalk lines. The surrounding buildings are wrapped in massive LED billboards casting rainbow reflections on the wet pavement below. The sky transitions from deep indigo at the top to a warm amber glow at the horizon where the last light fades. Shot with a 24mm wide-angle lens, f/11 deep depth of field keeping everything sharp from foreground to infinity. Long exposure look with silky motion trails, cool blue dominant palette with warm neon accents, ultra-sharp digital medium format quality.

【中文说明】
东京涩谷十字路口蓝色时刻俯瞰。行人运动模糊、LED 广告牌彩色反射、雨后湿润路面。24mm 广角 + 长曝光效果，冷蓝主调 + 暖霓虹点缀。

【参数建议】
- 宽高比：16:9
- 分辨率：4K

---

## 6. 社交媒体竖版图

**测试能力**：9:16 平台适配 + Photorealistic 模板

【分析】
抖音/Reels 竖版比例，旅行摄影风格。Kodak Gold 200 暖色调 + 逆光作为视觉亮点。

【Prompt】
A tall vertical composition of a young man in a vintage olive military jacket and faded blue jeans, walking toward the camera down a narrow cobblestone alley in Lisbon. Colorful tiled facades in azulejo blue and terracotta rise on both sides, draped with laundry lines overhead. He carries a worn leather messenger bag slung across his chest, looking slightly off-camera to the right with a relaxed half-smile. Morning sunlight streams in from behind, creating a warm backlit halo around his silhouette and long shadows stretching toward the lens. Shot at 35mm, f/2.8 shallow depth of field, Kodak Gold 200 warmth with natural film grain, nostalgic travel photography aesthetic.

【中文说明】
里斯本小巷中走来的年轻男子竖版图。两侧彩色瓷砖墙面 + 晾衣绳。逆光晨光 + Kodak Gold 200 暖色调，旅行摄影美学。

【参数建议】
- 宽高比：9:16
- 分辨率：2K

---

## 7. 美食摄影

**测试能力**：Photorealistic 模板 + Lighting + Material + 俯拍

【分析】
美食平铺俯拍，鸟瞰视角。重点在光线方向、食材质感和构图留白。

【Prompt】
An overhead bird's-eye view flat-lay of a rustic breakfast spread on a weathered oak farmhouse table. Center frame: a cast-iron skillet with two sunny-side-up eggs, crispy bacon strips, and a sprig of fresh rosemary. Surrounding it in an organic arrangement: a small ceramic bowl of mixed berries, a wooden board with sliced sourdough bread, a glass jar of honey with a wooden dipper, and a steaming cup of black coffee in a speckled stoneware mug. Soft diffused morning light enters from the upper left, casting gentle shadows to the bottom right and highlighting the glossy egg yolks and the steam rising from the coffee. Warm earth tones, clean food photography styling with intentional negative space in the lower right corner, sharp focus on textures throughout.

【中文说明】
乡村早餐俯拍平铺。铸铁锅煎蛋培根居中，周围有浆果、酸面包、蜂蜜、黑咖啡。柔和晨光从左上打入，温暖大地色调，专业美食摄影构图。

【参数建议】
- 宽高比：1:1
- 分辨率：4K

---

## 8. 品牌名片设计

**测试能力**：Text Rendering + Minimalist 模板 + 极简设计

【分析】
极简设计 + 精确文字渲染。多处文字均用引号包裹，指定字体风格和位置。

【Prompt】
A minimalist business card mockup lying flat on a sheet of textured cream cotton paper. The card is horizontal with rounded corners and a matte white finish. On the left half, the name "RITY STUDIO" is printed in small, elegant black serif letters with generous letter-spacing, and below it in lighter gray text "Creative Director" in the same serif typeface. On the right half, aligned to the right edge, three lines of contact information in a clean monospace typeface. A small geometric logo mark — a single continuous line forming an abstract "R" — sits in the upper left corner of the card in matte gold foil. The overall composition is ultra-clean with ample white space. Soft overhead studio lighting with minimal shadows, captured from a slight overhead angle on a digital medium format camera.

【中文说明】
极简品牌名片。白色圆角卡片在奶油色棉纸上。左侧 "RITY STUDIO" + 职位（衬线体），右侧联系信息（等宽体），左上角金色抽象 R logo。大量留白，极简美学。

【参数建议】
- 宽高比：3:2
- 分辨率：4K

---

## 9. 3D 等距悬浮岛

**测试能力**：非写实风格切换 + 文字渲染 + 多元素空间布局

【分析】
完全脱离摄影范式，测试 3D 渲染风格。用 "isometric 3D render" + "stylized feature-animation quality" 作为风格锚点。

【Prompt】
An isometric 3D render of a tiny floating island shaped like a perfect cube of earth and rock, hovering against a clean soft gradient sky transitioning from pale peach at the bottom to light lavender at the top. On top of the island sits a miniature Japanese convenience store with warm interior light glowing through its glass front doors, a striped awning in red and white, and a small illuminated sign reading "24H" above the entrance. Beside the store, a single cherry blossom tree in full bloom leans gently to the right, with a few pink petals drifting off into the empty sky. A tiny vending machine glows blue on the left side. The edges of the floating island reveal cross-section layers of dark soil, lighter clay, and rough stone at the bottom. Soft ambient occlusion shadows, miniature tilt-shift depth of field, pastel and muted color palette, clean studio lighting from above, stylized feature-animation-quality subsurface scattering on the cherry blossoms, toy-like scale.

【中文说明】
等距 3D 悬浮岛。方块形岛屿上有迷你日本便利店（暖黄灯光+红白遮阳棚+"24H"招牌）、樱花树（花瓣飘落）、蓝色自动售货机。岛屿截面露出地质分层。粉蜡笔天空渐变，动画长片质感玩具风。

【参数建议】
- 宽高比：1:1
- 分辨率：4K

【本地样本记录】（2026-03-12 Higgsfield，3 张；不代表稳定命中率）
- 风格切换：零写实残留，纯 3D 渲染
- "24H" 文字：3/3 清晰正确
- 地质分层：3/3 完美（表土→黏土→岩石）
- 樱花飘落：3/3 花瓣在空中自然飘散
- 额外细节：模型自动补充了屋顶空调外机等便利店常识元素

【可调整方向】
- 换成拉面店/书店等不同业态
- 改为夜景版（霓虹灯+星空）
- 增加更多岛屿元素（路灯、邮筒、猫）

---

## 10. 多主体空间叙事

**测试能力**：多角色动作区分 + 前中后景分层 + 冷暖混合光 + 超宽比例

【分析】
最高难度测试。4 个独立角色各有不同动作，精确的左中右空间分配，前景碗筷→中景三人→背景厨师的深度层次。Fuji Pro 400H 作为风格锚点，冷暖双色温灯光。

【Prompt】
A wide-angle interior photograph of a tiny eight-seat ramen counter restaurant in Tokyo late at night, shot from a low angle at one end of the L-shaped wooden counter looking down its length. In the nearest foreground at the bottom of the frame, a pair of wooden chopsticks rests across a half-finished bowl of tonkotsu ramen, steam still curling upward from the milky broth. Three customers sit along the counter in the midground, each isolated in their own world: on the left stool, an elderly man in a gray cardigan reads a folded evening newspaper while his ramen cools untouched beside him; on the center stool, a young woman in a black turtleneck holds her phone horizontally above her bowl, photographing the perfect chashu arrangement; on the right stool, a middle-aged salaryman in a wrinkled navy suit has loosened his tie and leans forward over his bowl, slurping noodles with both hands on chopsticks. Behind the counter in the background, the chef — a stocky man in a white headband and stained white jacket — stands with his back half-turned, ladling broth from a massive steel stockpot, clouds of steam billowing up into the warm overhead pendant lights. The entire scene is bathed in a mix of warm tungsten pendants above and cool blue-white fluorescent tubes along the back kitchen wall, creating a split warm-cool tone. Shot on a 28mm lens at f/2.8, shallow focus on the center customer with the foreground bowl and background chef falling into gentle softness. Fuji Pro 400H film look with muted pastel tones and lifted shadows, quiet contemplative mood.

【中文说明】
深夜东京 8 座拉面店。前景半碗拉面+筷子，中景三个客人（左：灰开衫老人读报 / 中：黑高领女生拍照 / 右：深蓝西装上班族吃面），背景厨师白头带舀汤。暖黄吊灯+冷蓝荧光灯双色温，28mm 广角，Fuji Pro 400H 柔和色调。

【参数建议】
- 宽高比：21:9（超宽电影比例，容纳横向多人）
- 分辨率：4K

【本地样本记录】（2026-03-12 Higgsfield，4 张；不代表稳定命中率）
- 4 角色动作：4/4 全部正确区分（读报/拍照/吃面/舀汤）
- 空间位置：左中右三人排列正确
- 前中后景：碗筷→三人→厨师 层次清晰
- 冷暖双色温：暖黄吊灯+冷蓝荧光灯精准分区
- 弱项：选择性焦点未执行（三个角色同样清晰）

【可调整方向】
- 减少到 2 个角色提高每人的细节精度
- 改为正面视角（站在厨师角度拍客人）
- 换成寿司店/居酒屋等不同业态

---

## 11. 双图融合：主体 + 构图参考

**测试能力**：多图参考 + 语义桥接 + 构图移植模式

【分析】
双图融合任务。图 1 提供主体（人物/场景细节），图 2 提供目标构图/机位。选用 Image Editing 模板（Template 6），以"构图移植"融合模式处理。关键：保留图 1 全部主体细节，仅改变机位和景别以匹配图 2。

【Prompt】
Using the provided reference image 1 as the primary subject source, reframe the entire scene to match the camera angle and composition shown in reference image 2. Maintain every detail from image 1 — the subject's appearance, clothing, expression, skin texture, the environment's color palette, all props, and the overall lighting atmosphere — while adopting the overhead rear three-quarter perspective, the wider shot framing, and the spatial depth arrangement visible in image 2. The camera now looks down from behind and above the subject at approximately 45 degrees, revealing more of the surrounding environment in the foreground and middle ground. Keep the same warm teal-and-amber color grading, the soft diffused interior lighting, and all architectural details intact. Shot on a 24mm wide-angle lens, f/4 moderate depth of field, cinematic film still quality with subtle grain.

【中文说明】
将图 1 的完整场景（保持所有细节不变）重新构图为图 2 所示的高角度后方俯拍视角。主体外貌、服装、环境、色调、光影全部保留，只改变机位——从后上方 45 度俯拍，用 24mm 广角展现更多环境。

【参数建议】
- 宽高比：16:9（匹配新的宽视角）
- 分辨率：2K
- 参考图：2 张（图 1 = 主体+环境源，图 2 = 构图/机位参考）

【可调整方向】
- 调整俯拍角度（改为 60 度更垂直的鸟瞰）
- 改为正面低角度仰拍（保持同一场景）
- 增加景深效果（f/1.8 虚化背景突出主体）

---

## 12. 三图融合：主体 + 风格 + 光影

**测试能力**：三图语义桥接 + 纹理置换模式 + 光影移植模式

【分析】
三图融合任务。图 1 提供主体人物，图 2 提供目标艺术风格，图 3 提供光影氛围。组合使用"纹理置换"（A主体+B风格）和"光影移植"（+C氛围）两种融合模式。冲突优先级：主体（图1）> 风格（图2）> 光影（图3）。

【Prompt】
A portrait of the exact person shown in reference image 1 — same facial features, hairstyle, skin tone, and build — rendered in the artistic visual style drawn from reference image 2, with its distinctive color treatment, texture quality, and tonal character applied across the entire frame. Place this subject in an environment lit to match the dramatic lighting atmosphere from reference image 3, adopting its light direction, shadow density, contrast ratio, and color temperature. The subject faces the camera at three-quarter angle, medium close-up framing at 85mm focal length. The style rendering from image 2 MUST be applied uniformly — affecting skin texture, fabric rendering, and background treatment equally. The lighting from image 3 MUST preserve its directional quality and shadow characteristics. NEVER blend conflicting styles; image 2's aesthetic takes full precedence over any default rendering.

【中文说明】
三图融合：保持图 1 人物的所有面部和体态特征，套用图 2 的艺术风格/色彩处理到全画面，再用图 3 的光影氛围（光线方向、阴影密度、色温）统一整个场景。85mm 人像镜头，四分之三侧面。

【参数建议】
- 宽高比：3:2
- 分辨率：4K
- 参考图：3 张（图 1 = 角色参考，图 2 = 风格参考，图 3 = 光影参考）

【可调整方向】
- 只用图 1 + 图 2（去掉光影参考，用自然光）
- 改为全身构图展现更多服装和姿态
- 加强图 3 光影的戏剧性（"极端明暗对比 chiaroscuro"）

---

## 场景速查表

| 场景类型 | 推荐宽高比 | 推荐分辨率 | 官方模板 | 关键焦点 | 实测 |
|---------|-----------|-----------|---------|---------|------|
| 电影感人像 | `16:9` / `21:9` | `2K` / `4K` | Photorealistic | 胶片 + 灯光 + 情绪 | 有本地样本 |
| 产品图 | `1:1` / `4:5` | `4K` | Product Mockup | 材质 + 灯光 + 背景 | |
| 海报排版 | `2:3` / `3:4` | `2K` / `4K` | Text Rendering | 版面结构 + 文字 | 有本地样本 |
| 角色系列 | `3:2` / `4:3` | `2K` | Photorealistic | 描述一致性 + 参考图 | |
| 城市风光 | `16:9` / `21:9` | `4K` | Photorealistic | 构图 + 氛围 + 色调 | |
| 社交媒体竖图 | `9:16` / `4:5` | `2K` | Photorealistic | 竖版构图 + 平台适配 | |
| 美食摄影 | `1:1` / `4:5` | `2K` / `4K` | Photorealistic | 材质 + 光线 + 微距 | 有本地样本 |
| 品牌设计 | `3:2` / `1:1` | `4K` | Text Rendering + Minimalist | 文字 + 排版 + 留白 | |
| 3D 等距渲染 | `1:1` | `2K` / `4K` | — (自定义风格锚点) | 风格切换 + 空间布局 | 有本地样本 |
| 多主体叙事 | `21:9` / `16:9` | `2K` / `4K` | Photorealistic | 角色区分 + 空间分层 | 有本地样本 |
| 贴纸/插画 | `1:1` | `2K` | Stylized/Stickers | 风格 + 干净可抠图背景 | |
| 风格迁移 | 同原图 | `2K` | Style Transfer | 保留构图 + 改风格 | |
| 局部编辑 | 同原图 | `2K` | Image Editing | 精确描述修改区域 | |
