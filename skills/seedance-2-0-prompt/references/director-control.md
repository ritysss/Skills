# Director Control Reference

Read this when a Seedance prompt needs strict character anchoring, screen positioning, pose locks, gaze direction, two-character blocking, camera compatibility, or final-frame control.

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

State the hierarchy in `【参考素材使用】` when multiple references can conflict.

## Screen Map

Use screen geometry as a strong compositional anchor:

- `左三分之一 / 中央 / 右三分之一`
- `前景 / 中景 / 背景`
- `上三分之一 / 下三分之一`
- `x=30% / x=50% / x=70%` when precision helps
- `脚位接近 y=88%` or `主体占画面高度约45%` when ground contact or scale matters

Treat percentages as prompt anchors, not exact guarantees. Combine them with normal film language.

## Character Anchor Block

For difficult character shots, compose a compact anchor before writing `[动作]` and `[镜头]`.

Template:

```text
角色A锚定：人物来自@图片1，保持相同面部、发型、服装、体型比例和轮廓；固定在画面左三分之一，中心约x=30%，位于前景，中景/半身/全身；身体朝向画面右侧，视线看向角色B；双脚踩在同一地面接触点，右手握住门框；情绪保持紧张克制。
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
- object in hand
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

## Camera Compatibility

Always specify:

- shot size: wide, full shot, medium, close-up, macro
- angle: eye-level, low-angle, high-angle, overhead, POV, over-the-shoulder
- lens: 24mm, 35mm, 50mm, 85mm, 135mm, macro, anamorphic
- movement: locked-off, slow dolly-in, lateral track, crane up, orbit, handheld
- focus: shallow depth, deep focus, rack focus, focus locked on eyes/product/logo
- composition: rule of thirds, symmetry, negative space, leading lines

If character position matters, the camera must preserve blocking:

```text
35mm 中景眼平机位，摄影机从固定正面角度缓慢推进，只推进约10%，全程保持角色A在左三分之一、角色B在右三分之一，中间负空间不被破坏。
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
- More than two camera moves: choose the most important one.
- More than three important characters: split the scene or define foreground/midground/background groups.
- Complex fight/chase/transformation: build separate generation blocks with handoff frames.
