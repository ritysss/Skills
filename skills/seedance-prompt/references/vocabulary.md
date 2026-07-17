# Seedance 2.0 Vocabulary

Use this reference only when choosing precise production language.

## Lens And Focal Length Language

Treat focal length as prompt guidance, not guaranteed camera metadata.

Authority comes before this vocabulary. Use the tables and defaults only for optical facts that the user and accepted sources leave unspecified. Never replace an explicit focal length or FOV with a table default. If a visual reference owns composition/camera but gives no numeric optics, inherit its visible perspective and lens relationship without guessing a number. If a source gives only focal length, do not derive a numeric FOV from the rough-equivalence table.

`35mm胶片颗粒` and `35mm胶片质感` describe texture/medium, not lens focal length. Keep them in style language and never use them to override `[镜头]` optics.

| Lens language | Use for | Effect |
|---|---|---|
| `14mm / 18mm 超广角` | huge spaces, action, subjective movement | exaggerated space, stronger distortion risk |
| `24mm 广角` | street, action, environment-heavy cinematic shots | strong depth and spatial energy |
| `35mm 广角中景` | balanced people + environment | natural cinematic perspective |
| `50mm 标准镜头` | calm narrative, product/person balance | close to human-eye feeling |
| `85mm 中长焦` | portraits, emotion, premium close-ups | background compression, shallow depth |
| `135mm 长焦` | distance, isolation, luxury compression | strong compression, narrow frame |
| `微距镜头` | product detail, texture, droplets, skin/material | extreme detail and shallow focus |
| `变形宽银幕镜头` | cinematic spectacle | oval bokeh, horizontal flare, wide-screen feel |

Defaults only when no accepted optical authority exists:

- People in environment: `35mm`
- Face/emotion: `85mm`
- Product detail: `微距镜头` or `85mm`
- Big scene reveal: `24mm`
- Premium compressed image: `85mm` or `135mm`

## FOV Language

Use FOV only when the shot needs stricter optical control. Pair it with familiar lens language so the prompt stays readable.

| FOV language | Rough lens feel | Use for |
|---|---|---|
| `约107度视场` | 14-16mm ultra-wide | huge interior, architectural scale, extreme spatial energy |
| `约84度视场` | 20-24mm wide | establishing, group blocking, action in readable space |
| `约63度视场` | 28-35mm wide-normal | people in environment, natural cinematic movement |
| `约47度视场` | 40-50mm normal | neutral narrative, dialogue, calm product/person balance |
| `约29度视场` | 75-85mm portrait | emotional medium close-up, subject separation |
| `约18度视场` | 100-135mm portrait/tele | identity-preserving close portrait, compressed background |
| `约12度视场` | 180-200mm tele | hands, objects, detail within a wider situation |
| `约8度视场` | 300mm+ super-tele | distant observation, broadcast/hidden-camera feeling |

Use one FOV per shot or per timed segment. For multi-shot prompts, state the FOV inside each timed shot and keep it stable within that segment.

## Camera Movement

Write camera movement with:

`movement + speed + subject lock + stability`

Reliable movement terms:

- `固定机位，三脚架稳定`
- `缓慢推进`
- `缓慢拉远`
- `平稳横移跟拍`
- `平稳左摇 / 平稳右摇`
- `缓慢上摇 / 缓慢下摇`
- `缓慢上升 / 缓慢下降`
- `环绕跟拍`
- `云台平稳跟拍`
- `手持跟拍，轻微真实晃动`
- `焦点转移`

Risk guidance:

- Prefer `缓慢`, `平稳`, `匀速`.
- Use `快速`, `剧烈`, `FPV`, `甩镜`, or `子弹时间` only when the user explicitly wants high energy.
- Avoid combining fast camera, complex body motion, text, and detailed faces in one short shot.
- When timing matters, specify short beat windows such as `0:00-0:03缓慢推进` or `第4秒停住`.
- When position matters, specify small movement amounts such as `只推进约10%`, `横移半个身位`, or `保持同一脚位`.
- Give the move a reason: reveal new information, follow subject motion, change emotional distance, redirect attention, or land a transition.
- Match units to the motion. Use linear distance/speed for a dolly or vehicle, degrees or screen travel for a pan/tilt, and duration for a rack focus. Do not describe angular camera motion in `km/h`.

### Camera Regime And Settle Phrases

- `三脚架锁定，表演承担节奏；如需移动，只执行一次缓慢推进，平缓起步，平缓收住。`
- `摄影机随操作者呼吸轻微起伏，并随主体重心小幅调整构图，幅度克制。`
- `云台或轨道沿主体的单一路径平稳跟随，地平线稳定，主体位置始终可读。`
- `主体动作结束后摄影机收住在反应表情、接触点或揭示物上，并停留一拍。`
- `对白期间正面稳住说话者，只在换人、动作或反应间隙重新构图。`
- `同一时刻只执行一个主运镜；长镜头按顺序完成各阶段，并在每个阶段末收住。`
- `碰撞瞬间只发生一次轻微机身反馈，随后恢复稳定。`

## Cut Precision And Vocabulary

- One continuous shot: use the compact six-field contract and explicitly keep the camera continuous when accidental cuts are likely.
- Ordered cuts without timecodes: use `镜头1：...`, `镜头2：...` when order matters but exact seconds do not.
- Timed cuts: use `镜头1 [0:00-0:04]：...` only when a beat must land on a clock.
- Freestyle B-roll: leave angle selection open only when the user explicitly accepts model-selected coverage.

Useful transition terms:

- `HARD CUT`: direct state change with no blend
- `MATCH CUT`: preserve a matched shape, action, direction, or composition across the cut
- `INSERT CUT`: isolate a story-critical hand, prop, screen, or detail
- `REVERSE CUT`: return to the opposite eyeline or response angle
- `SMASH CUT`: abrupt contrast in scale, sound, or state
- `WHIP CUT`: cut through directional motion blur when explicitly requested

Do not add exact timing thresholds for these transitions unless the current provider or accepted test result establishes them.

## Camera Recipes

Treat these as optional combinations, not universal rules.

### Distant Observation

Combine a long or super-tele perspective with one foreground occluder and atmospheric depth. Keep the camera anchored at distance and preserve one operator axis. Change the occluder only across deliberate cuts.

### Sports Broadcast Search

Use distant tele compression, restrained handheld correction, and a focus/operator behavior that appears to find and hold the action. Keep the movement readable rather than adding decorative shake.

### Detail-On-Wide

Place a wide camera close and low beside a small foreground object so that the object enlarges while the background remains readable. Use this for product, weapon, footwear, or environmental inserts when the relationship between detail and space matters.

### Intimate Wide

Place a controlled wide perspective near a face while keeping the subject centered and the environment legible. Use only when mild spatial exaggeration supports intimacy; avoid it when identity preservation requires portrait compression.

### Tele Compressed Atmosphere

With an accepted long-lens perspective, describe haze, dust, rain, or heat shimmer as layers between camera and subject. Do not invent a tele value if the reference already owns the visible perspective.

## Shot Size

- `远景`: establishes place and scale
- `全景`: full body and environment
- `中景`: upper body or subject with clear surroundings
- `中近景`: chest-up with some environment
- `近景`: face/upper body emphasis
- `特写`: face/object detail
- `大特写`: eyes, mouth, logo, small detail
- `微距`: texture, liquid, material surface

## Light And Color

Light terms:

- `柔和环境光`
- `左侧45度窗光`
- `黄金时刻光线`
- `侧逆光`
- `逆光剪影`
- `伦勃朗光`
- `蝶光 / 派拉蒙光`
- `低调光，高对比阴影`
- `体积光穿透尘埃粒子`
- `霓虹反射`
- `干净棚拍光`

Color terms:

- `低饱和青绿色调`
- `暖金色夕阳色调`
- `冷蓝阴影与暖橙高光`
- `银灰与深蓝商业色调`
- `黑金高反差`
- `自然肤色还原`
- `白平衡稳定`
- `色彩基调一致`

Color-as-material examples:

- `红色霓虹只落在湿地反光和人物侧脸边缘`
- `冷蓝环境光留在阴影区域，暖橙高光只打在金属边缘`
- `银灰车身反射深蓝城市灯带，品牌标识保持清晰`
- `白色棚拍光均匀覆盖产品表面，阴影柔和落在右后方`

Use Kelvin language when color continuity matters:

- `3200K暖钨丝灯`
- `4000K中性室内光`
- `5600K日光白平衡`
- `8500K冷蓝夜景`

## Style And Texture

Choose one main anchor:

- `写实电影感，35mm胶片质感，自然颗粒，柔和高光溢出`
- `数字电影感，干净画面，精确色彩还原`
- `高端商业广告质感，产品级锐度，干净色彩科学，低噪点`
- `纪录片质感，自然光，轻微手持纹理`
- `日系动画风格，明亮色彩，干净线条`
- `赛博朋克夜景，霓虹光，潮湿街道反射`
- `90年代港风复古，黄绿色调，浓重胶片颗粒，变形镜头光晕`

Do not stack multiple unrelated anchors.

## Physical Detail Terms

Use when material behavior matters:

- `真实物理`
- `重力`
- `动量`
- `碰撞`
- `布料物理，衣物随风自然摆动`
- `发丝物理，头发随风自然飘动`
- `水花飞溅，湿润反射`
- `烟雾扩散，粒子飘散`
- `金属反射，表面质感清晰`

Measurable physical language, used only when the estimate helps composition or physics:

- `雾气浓度约30%，15米深处开始明显遮挡背景`
- `前景遮挡占画面约20%，主体仍然清晰可读`
- `衣料跟随人物转身延迟半拍摆动`
- `脚底影子与地面接触点连接，方向与主光一致`
- `水滴沿发梢向下滑落，湿润高光连续`
- `尘埃粒子只在逆光光束内可见`

Measurements are prompt anchors, not guaranteed simulation parameters. Do not add percentages, meters, Kelvin values, or speeds merely to make the prompt sound technical.

For emotion, use body behavior instead of labels:

- `眼神下压，停顿半秒后抬眼`
- `下颌收紧，吞咽一次`
- `右手指节用力发白`
- `肩膀上提后慢慢放松`
- `呼吸变浅，胸口轻微起伏`

## Audio Terms

Always write audio.

No fixed audio:

- `无BGM，保留自然环境声。`
- `无BGM，静音处理，动作节奏由画面运动承担。`

Environment:

- `雨声、远处车流声、霓虹灯电流低鸣`
- `室内空调底噪、杯子轻碰桌面的声音`
- `脚步声、衣料摩擦声、轻微呼吸声`

Action SFX:

- `低频冲击声`
- `金属摩擦声`
- `水花飞溅声`
- `镜头节拍点轻微呼吸感`

Audio reference:

- `@音频1 作为节奏参考，动作贴合主拍点。`
- `@音频1 作为对白参考，单一说话者口型尽量同步。`

## Positive Anchors

Use positive wording:

| Need | Write |
|---|---|
| clear image | `焦点清晰，细节锐利，纹理稳定` |
| stable face | `面部特征清晰，五官结构稳定，自然人体比例` |
| no shake | `画面平稳，云台稳定，运动流畅` |
| no style drift | `风格锁定，色彩基调一致，视觉连贯` |
| no flicker | `白平衡锁定，光线连续，无色温跳变` |
| no deformation | `自然比例，结构准确，边缘线条稳定` |
| subject stays framed | `构图锁定，主体保持画面中心/三分线位置` |
