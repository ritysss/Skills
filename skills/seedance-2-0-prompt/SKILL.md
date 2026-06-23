---
name: seedance-2-0-prompt
description: Generate production-ready Chinese video prompts for Seedance 2.0-compatible video generation, including 即梦网页, official/API routes, and third-party/API gateways. Use for AI video prompt writing, optimization, or repair across text-to-video, image-anchored video, first/last-frame video, multimodal @图片/@视频/@音频 reference use, video editing, video extension, audio-aware video, real-person/portrait workflows when the current provider supports them, short drama shots, ads, product videos, cinematic blocking, storyboard-style segments, and troubleshooting generated results. Default to one directly pasteable Chinese prompt with explicit base scene, reference roles, shot/timing, subject, action, camera/lens language, style/light/color/texture, positive constraints, audio, and final-frame continuity control.
---

# Seedance 2.0 Prompt

Generate one directly usable prompt for the user's current Seedance-compatible runner. Prioritize stability, reference control, physical camera logic, and pasteability over multiple creative variants.

## Default Contract

- Output **one prompt only** by default. Do not create `稳定版`, `电影版`, `最终版`, or parallel variants unless the user explicitly asks.
- Write the production prompt in Chinese by default. Use English or bilingual output only when requested.
- Treat mode, aspect ratio, duration, resolution, upload strategy, and reference type as preflight decisions. Do not clutter `【基础设定】` with UI settings.
- Always include `[音频]`. If no fixed audio is supplied, write `无BGM` plus concrete ambience, Foley, or silence.
- Use positive anchoring. Replace `不要变形/不要乱动/不要换脸` with stable physical conditions.
- Keep one core action and one core camera behavior per shot unless the user explicitly asks for a multi-shot storyboard.
- Do not generate Nano Banana/image prompts from this skill. If the user needs an image first, output an image anchor card and defer image prompt writing to the dedicated image-prompt skill.
- Do not invent platform limits, hidden API paths, or exact current UI/API choices. If a platform setting is uncertain, say it should follow the current provider's visible options or documentation.

Ask at most one concise question only when a missing detail blocks execution. Otherwise choose the most stable production default and generate directly.

## Preflight

Decide these before composing:

1. **Mode**: text-to-video, image-anchored video, first/last-frame video, multimodal reference, edit video, extend video, or audio-aware video.
2. **Reference manifest**: which `@图片`, `@视频`, and `@音频` exist, what each one controls, and which reference has priority if conflicts appear.
3. **Shot strategy**: single continuous shot, timed multi-shot prompt, or multiple separate generation blocks.
4. **Anchoring risk**: identity, wardrobe/product, environment, composition, pose, contact points, screen position, final frame.
5. **Camera plan**: shot size, angle, lens/focal-length language, movement, speed, stability, focus, and whether the camera preserves blocking.
6. **Audio plan**: no BGM, ambience, Foley, dialogue, singing, beat sync, or supplied audio reference.
7. **Repair path**: if the user is fixing a failed result, identify the failure class before rewriting.

## When To Read References

- Read `references/director-control.md` for character positioning, two-person blocking, pose/state locks, gaze direction, contact points, final-frame control, or hard cinematic single-shot control.
- Read `references/platform-workflow.md` for provider/API boundaries, settings language, real-person/portrait policy handling, first-image workflows, long-video segmentation, reference-count strategy, or low-resolution validation flow.
- Read `references/troubleshooting.md` when the user reports a generated-video defect or asks why a result failed.
- Read `references/vocabulary.md` when choosing precise focal length, movement, lighting, color, texture, physical, or audio terms.
- Read `references/examples.md` when matching output shape for text-to-video, multimodal, first/last-frame, edit, extension, or multi-shot prompts.

## Reference Rules

Use this syntax when references exist:

- Images: `@图片1` to `@图片9`
- Videos: `@视频1` to `@视频3`
- Audio: `@音频1` to `@音频3`
- Mixed materials: keep the total lean; if the current provider has a stricter limit, follow that provider.

Declare reference roles in `【参考素材使用】`, not in `【基础设定】`.

Good role declarations:

- `@图片1 作为首帧、人物外观和起始构图参考。`
- `@图片1 作为首帧，@图片2 作为尾帧目标姿态与最终构图参考。`
- `@视频1 仅参考动作速度和运镜节奏，不复制背景内容。`
- `@音频1 作为对白/节奏参考，画面动作贴合主要拍点。`

If references conflict, state the priority:

- `@图片1 的人物身份优先；@图片2 仅控制服装；@图片3 仅控制场景与光线。`

Do not let one reference control identity, costume, scene, camera, style, and rhythm at the same time unless it is intentionally the locked first frame.

## Output Format

Use this default structure:

```text
【基础设定】
...

【参考素材使用】
...（仅在有参考素材时出现）

【分镜与景别】
...

【提示词】
[主体] ...
[动作] ...
[镜头] ...
[风格] ...
[约束] ...
[音频] ...
```

Do not add a title before the block. Do not append explanations after the prompt unless the user asked for reasoning.

Use optional fields sparingly:

- Add `[终帧]` only when the ending composition must be locked.
- Do not add `[终帧]` for ordinary single-shot prompts. If the ending is simple, fold it into `[动作]` or `【分镜与景别】`.
- Use `[终帧]` for first/last-frame generation, extension continuity, drift repair, wrong-ending repair, complex multi-character blocking, product/logo end states, or handoff frames.

For complex multi-shot output, use:

```text
【分镜】
镜头1 [0:00-0:04]：景别 - 画面内容；镜头语言；光线颜色；声音提示。
镜头2 [0:04-0:08]：...
转场：...
```

Each timed shot must state shot size, main composition, one dominant action, one camera behavior, and sound if relevant.

## Field Rules

### 基础设定

Write one sentence describing only the current shot or segment content.

Good:

- `夜晚雨后的街口，一名穿黑色风衣的女性停在霓虹灯下，准备回头看向镜头。`

Avoid:

- UI settings, seed/model notes, upload method, workflow chatter
- story recap such as `延续上一集剧情`
- vague hype such as `震撼大片级画面`

### 分镜与景别

For a single shot, include shot size and composition:

- `中近景，人物位于画面中央偏右，前景有轻微虚化雨滴，背景是湿润街面和模糊车灯。`

For character blocking, add screen position and depth:

- `中景，人物固定在画面左三分之一，脚位接近画面下缘，另一名角色位于右侧中景深处，中间保留紧张的负空间。`

### [主体]

Describe who or what appears: person/object, age/type, wardrobe, material, product model, core scene object, and visible state. Keep it grounded in what the frame can show.

### [动作]

Write one continuous and physically plausible main action in present tense.

Good:

- `她缓慢抬起右手整理耳返，随后停住并看向镜头。`

Avoid stacking unrelated actions such as running, jumping, fighting, transforming, and exploding in one short shot.

### [镜头]

Always include:

`景别/构图 + 焦段或镜头感 + 角度 + 运镜 + 速度 + 稳定方式 + 焦点`

Examples:

- `35mm 广角中景，眼平机位，摄影机从正前方缓慢推进，云台稳定，焦点锁定人物眼睛。`
- `85mm 中长焦半身特写，浅景深，背景柔和压缩，摄影机轻微横移，焦点稳定锁定面部。`
- `微距镜头固定机位，焦点从产品边缘缓慢转移到品牌标识，三脚架稳定。`

Use focal length as prompt language, not guaranteed metadata. Prefer common lens terms over excessive technical stacks.

### [风格]

Write visual style, light, color palette, tone, and texture in one field. Choose one main visual anchor.

Good:

- `写实电影感，左侧45度柔和窗光，低饱和青绿色调，35mm胶片颗粒，柔和高光溢出。`
- `高端商业广告质感，干净棚拍光，银灰与深蓝色彩基调，产品级锐度，低噪点。`

Avoid stacking unrelated styles.

### [约束]

Use positive anchoring:

- `人物外观一致，面部结构稳定，自然人体比例，脚位保持同一地面接触点，动作连贯，画面平稳，白平衡锁定，主体不漂移。`

For multiple characters, add left/right, depth, gaze, and crossing locks:

- `角色A保持左侧前景，角色B保持右侧中景深处，两人不交换画面位置，中间负空间保持清晰，视线方向连续。`

### [音频]

Always write this field.

- No fixed music: `无BGM，保留雨声、远处车流声和轻微衣料摩擦声。`
- Silence: `无BGM，静音处理，动作节奏由画面运动承担。`
- Audio reference: `@音频1 作为节奏参考，动作贴合主拍点。`
- Dialogue/singing: keep one main speaker or singer per shot.

### [终帧]

Optional. Do not include this field by default.

Use it only when the ending composition matters, when a last frame exists, or when the user has complained about drift, wrong ending, or continuity.

Write a specific final image:

- `最后停在人物右手握住门框的近景，人物仍在左三分之一位置，背景角色保持右侧中景，中心负空间清晰。`

## Mode Handling

Use these modes internally. Do not output a `【模式】` field unless requested.

### Text-To-Video

Use when there is no locked reference. Make subject, action, camera, and style extra explicit. Add `[终帧]` only when the ending composition is part of the request.

### Image-Anchored Video

Use when a locked image exists. State whether the image is first frame, character/product reference, composition reference, or style reference.

### First/Last-Frame Video

Use when two image anchors define start and end. State what `@图片1` and `@图片2` control, then write a natural transition between them.

### Multimodal Reference

Use when images, videos, and/or audio are uploaded together. Assign one job per material and resolve conflicts by priority.

### Edit Video

Start from preservation and change scope:

- preserve original duration/camera/light/space when requested
- define replacement/addition/removal precisely
- constrain untouched areas

### Extend Video

Describe the source ending state and the new continuation. Preserve existing camera motion, subject identity, lighting, color, and audio continuity unless the user asks to change them.

### Audio-Aware Video

Use when dialogue, singing, beat sync, or music rhythm matters. Keep one main speaker/singer per shot. If audio is not fixed, default to `无BGM`.

## Image-First Workflow

If the user wants to create or lock an image before video and the image is not decided, output this card before the video prompt:

```text
【图像锚定卡】
[主体锚点] ...
[构图锚点] ...
[风格锚点] ...
[必须保留细节] ...
[转视频时的首帧用途] ...
```

Do not write the image-generation prompt here. Tell Codex to use the dedicated image prompt skill if the user asks for actual image generation text.

## Complexity Rules

- 4-8 seconds: one strong action.
- 8-12 seconds: one action plus one reveal.
- 12-15 seconds: two or three simple timed beats.
- Complex fight, chase, transformation, group scene, or spatial reversal: split into timed shots or separate generation blocks.
- If a camera move would break character blocking, reduce the camera move and preserve the screen positions.

## Quality Checklist

Before delivering, verify:

- Only one prompt is output unless variants were requested.
- `【基础设定】` describes only current shot content.
- References have explicit roles and priority.
- Shot size and composition are clear.
- `[主体]`, `[动作]`, `[镜头]`, `[风格]`, `[约束]`, and `[音频]` are present.
- `[镜头]` includes lens language, angle, movement, speed, stability, and focus.
- The action is not overloaded.
- Constraints use positive anchoring.
- Character prompts include screen position, state, gaze, contact points, and continuity when needed.
- `[终帧]` is omitted unless ending composition, continuity, or handoff control matters.
