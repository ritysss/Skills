# Director Control Reference

Read this when a Seedance prompt needs strict character anchoring, screen positioning, pose locks, gaze direction, two-character blocking, camera compatibility, or final-frame control.

## Write The Visible

Convert intent into visible instructions before writing the prompt.

| Abstract intent | Visible control |
|---|---|
| `紧张` | `人物停住，肩膀绷紧，右手握紧门框，视线固定在画面右侧，呼吸变浅。` |
| `高级感` | `干净构图，主体与背景分离，柔和侧光，低噪点，材质反射清晰，色彩不过饱和。` |
| `速度感` | `低机位跟拍，背景产生受控运动模糊，主体轮廓清晰，衣料和发丝顺着运动方向摆动。` |
| `危险感` | `前景遮挡占画面约20%，角色站在阴影边缘，远处红色警示光反射在湿地上。` |

If a sentence cannot be seen in the frame, turn it into posture, gaze, hand action, light, color, camera distance, timing, or material behavior.

## Prompt Isolation

Each generation block should stand alone.

- Do not depend on scene numbers, previous paragraphs, or `延续上一段` as the only continuity instruction.
- Restate the visible start state, accepted reference roles, and end state when continuity matters.
- If the previous clip is the authority, describe its final visible state and name it as `@视频1` or the approved handoff frame.
- Remove unused characters, props, locations, and tags from the current prompt.
- In a multi-shot prompt, mention a tag only in the shot where that person, object, or control role is active. A true cross-shot identity or scene authority may instead be declared once in `【跨镜头一致性】`.

## First-Frame Completeness

Before writing camera motion, make sure the opening frame can be reconstructed without relying on hidden context:

- who or what is visible and in what state
- subject screen position, depth, scale, orientation, and gaze
- foreground, midground, background, and negative space
- body/object contact points and story-critical prop state
- camera axis, height, and inherited perspective
- visible light source and direction when it affects the composition

Put physical start state in `[主体]`. Put screen geometry, shot size, optics, and camera axis in `[镜头]`. The first frame should not be an empty setup unless the requested action deliberately reveals the subject later.

## Control Hierarchy

Resolve conflicts in this order unless the user says otherwise:

1. Identity/face/body silhouette
2. Costume/product/prop
3. Environment and light
4. Composition and screen position
5. Subject action
6. Camera movement
7. Style and texture
8. Audio and text

Resolve the hierarchy inside the field that owns the disputed fact. Explicit user/source optical and camera facts remain authoritative within `[镜头]`; a style-only reference does not acquire control of lens, FOV, angle, axis, or movement.

## Composition And Optics Ownership

For the compact single-shot contract:

- `[主体]` owns the physical scene, visible subject identity/state, orientation, gaze, wardrobe/props, environment, and starting contact state.
- `[动作]` owns changes over time: performance, contact order, prop transitions, physics, and terminal action state.
- `[镜头]` owns the complete screen representation: starting shot size, subject screen position/depth/scale, foreground-midground-background layering, negative space, inherited optics or one chosen lens/FOV, angle/height/axis, movement, speed, stabilization, focus, and necessary ending shot size.

Do not repeat the same physical or camera fact across fields. A fact may be restated in `[约束]` only when it repairs a known failure.

Before choosing camera language, make an internal authority ledger for focal length, FOV, perspective, angle/height/axis, movement direction/speed, focus, stability, and camera phase:

- Copy every explicit accepted value or direction unchanged into the owning shot.
- If a visual reference owns camera geometry but states no numeric optics, write that its original perspective and lens relationship are inherited; do not guess `24mm`, `35mm`, or a numeric FOV.
- Choose one stable value only for a fact left unspecified by all accepted authorities.
- Resolve conflicting accepted sources to one declared priority before output. Do not compromise by including both values.
- Treat `35mm胶片颗粒/胶片质感` as texture, not focal length. It belongs to style and cannot override an optical lens value.

## Camera Motivation

Every camera move should reveal information, follow subject movement, change emotional distance, redirect attention, or land a transition. If it does none of these, simplify to a locked camera.

Good:

- `摄影机因人物抬眼而缓慢推进到中近景，焦点从手部转到眼睛。`
- `摄影机横移半个身位以露出此前被人物遮挡的门口。`

Avoid adding a push, orbit, pan, and rack focus only to make the shot feel more cinematic.

## Shot Precision Ladder

Choose the least rigid mode that still protects the intended edit:

1. One continuous shot: one field stack; the camera does not add cuts.
2. Ordered cuts without timecodes: `镜头1：...` / `镜头2：...` when order matters but exact seconds do not.
3. Timed cuts: `镜头1 [0:00-0:04]：...` only when action, dialogue, music, or reveal timing must land on a clock.
4. Freestyle B-roll: allow model-selected angles only when the user explicitly accepts that variability.

Use `HARD CUT`, `MATCH CUT`, `INSERT CUT`, `REVERSE CUT`, `SMASH CUT`, or `WHIP CUT` only when the transition type matters. Do not claim exact renderer thresholds for a cut or whip without provider-specific evidence.

## Screen Map

Use screen geometry as a strong compositional anchor:

- `左三分之一 / 中央 / 右三分之一`
- `前景 / 中景 / 背景`
- `上三分之一 / 下三分之一`
- `x=30% / x=50% / x=70%` when precision helps
- `脚位接近 y=88%` or `主体占画面高度约45%` when ground contact or scale matters

Treat percentages as prompt anchors, not exact guarantees. Combine them with normal film language.

## Character Anchor Content

For difficult character shots, distribute the anchor across `[主体]` and `[镜头]` instead of creating another output block.

Template:

```text
[主体] @图片1锁定角色A的面部、发型、服装、体型比例和轮廓；角色A身体朝向画面右侧，视线看向角色B，双脚踩在同一地面接触点，右手握住门框，情绪紧张克制。
[镜头] 中景，角色A固定在画面左三分之一、前景中心约x=30%，角色B位于右侧中景，中间保留负空间；继承@图片1可见的原始透视与镜头关系，眼平固定轴线。
```

Include only details that matter for the current shot.

## Spatial Relationship Locks

For two or more characters, specify:

- screen side: who stays left, center, or right
- depth layer: foreground, midground, or background
- distance: close, medium, far, or separated by an object/negative space
- eyeline: who looks at whom
- screen direction: facing screen-left or screen-right
- crossing rule: whether characters may cross the center line
- occlusion rule: whether one may block the other
- negative space: what empty space remains visible

Example:

```text
角色A保持左侧前景，角色B保持右侧中景深处，两人不交换画面位置，不跨过画面中央竖线；角色A面向画面右侧看向角色B，角色B面向画面左侧看向角色A，中间保留清晰负空间。
```

## State Locks

Position alone is not enough. Lock the visible state:

- emotion and facial expression
- posture and body orientation
- costume/hair/wet-dry state/injury or makeup
- story-critical prop holder, grip/support point, orientation, contact state, and final location
- gaze direction
- body tension
- allowed micro-motions

Example:

```text
人物保持疲惫但警觉的表情，肩膀紧绷，右手始终握住黑色手提包，视线从门把手转向画面右侧人物；只允许眼神、呼吸、发丝和衣料轻微运动。
```

## Grounding And Contact Points

Use contact points to prevent drifting:

- `双脚踩在同一湿地反光位置`
- `背部贴住墙面`
- `左手压在桌面`
- `右手握住栏杆`
- `膝盖接触地面`
- `影子与脚部连接，方向与主光一致`

When a character must stay still:

```text
人物身体保持原位，双脚不离开地面接触点，只有眼神、呼吸、发丝和衣料发生轻微变化。
```

## Motion Layers

Separate four motion layers:

1. Subject motion: character/object movement
2. Internal motion: expression, breathing, hair, fabric, hands
3. Camera motion: dolly, track, pan, tilt, crane, orbit, handheld
4. Environmental motion: rain, smoke, dust, crowd, vehicles, particles

Do not let all four layers become intense at once. If subject action is complex, simplify camera motion. If camera motion is strong, anchor character positions.

## Style Placement

Style works best when it is attached to the thing it controls.

- Put light source, direction, exposure, and haze in `[风格]`.
- Put lens/FOV, focus, movement, and stability in `[镜头]`.
- Put acting, breath, gaze, hand pressure, skin detail, and body tension in `[动作]` or `[主体]`.
- Put gravity, inertia, contact, cloth, hair, water, smoke, dust, and particles where the action happens.
- Keep technical finish such as grain, sharpness, and noise short in `[风格]`; keep resolution and provider settings outside the prompt.

Avoid opening the prompt with a generic style pile such as `电影感、史诗感、超真实、高级、震撼`. Start with the current visible shot, then attach style to light, camera, material, and motion.

## Camera Compatibility

For a single shot, `[镜头]` carries both the starting screen geometry and camera execution in one ordered sentence. `[主体]` still owns the character's physical start state.

For a timed shot, state both once inside that shot line. Use a numeric lens/FOV only when the source states it or when no accepted optical authority exists and the number adds real control. Never add a numeric FOV merely to make an inherited focal length sound more technical.

If character position matters, the camera must preserve blocking:

```text
[镜头] 中景，角色A保持左三分之一，角色B保持右三分之一，中间负空间清晰；35mm，眼平机位，摄影机因角色A靠近而从固定正面角度缓慢推进约10%，云台稳定，焦点锁定角色A眼睛。
```

When an accepted authority explicitly supplies both focal length and FOV, preserve the pair:

```text
35mm 广角/约63度视场，眼平机位，摄影机从阴影侧缓慢推进，适中景深，焦点锁定角色A眼睛。
```

## Final Frame

Use a final frame when the ending must be controlled. Do not add it to every ordinary prompt.

Include:

- who/what is visible
- screen position and depth
- pose or object state
- gaze direction
- camera distance and focus
- emotional or narrative endpoint

Example:

```text
[终帧] 最后定格在角色A握紧门框的左侧中近景，角色A眼睛看向画面右侧，角色B仍在右侧中景深处，焦点从手部回到角色A眼睛，中心负空间保持清晰。
```

## Positive Constraint Rewrites

| Need | Use |
|---|---|
| no face change | `人物保持相同面部结构、发型、服装、体型比例和轮廓。` |
| no drifting | `双脚保持同一地面接触点，主体始终位于画面左三分之一。` |
| no swapping | `角色A保持左侧，角色B保持右侧，两人不交换位置。` |
| no random camera | `摄影机进行缓慢受控推进，保持原有构图和空间关系。` |
| no blur | `主体焦点清晰，快速运动只产生受控电影运动模糊。` |

## Complexity Limits

- One shot: one main idea, one main action, one camera strategy.
- More than two strong actions: split into timed shots.
- When order matters but exact seconds do not: use ordered cuts without timecodes.
- More than two camera moves: choose the most important one.
- More than three important characters: split the scene or define foreground/midground/background groups.
- Complex fight/chase/transformation: build separate generation blocks with handoff frames.
