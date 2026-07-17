---
name: seedance-prompt
description: >-
  Generate production-ready Chinese prompts for Seedance-compatible video generation
  across ads, products, narrative, dialogue, action, dance, fashion, music video,
  documentary, UGC, animation, VFX, and abstract motion. Use for text-to-video,
  image/video/audio references, first/last-frame video, edit, extension, cinematic
  blocking, and failed-result repair across official/API routes, 即梦, and third-party
  gateways. Default single-shot output is one compact, directly pasteable six-field
  prompt: [主体], [动作], [镜头], [风格], [约束], and [音频], with reference roles embedded
  where they apply; use sequential or timed shot lists only when the generation contains
  cuts.
---

# Seedance Prompt

Generate one directly usable prompt for the user's current Seedance-compatible runner. Treat genre as a layer over the same controllable primitives: subject state, action, camera, look, constraints, audio, timing, and continuity. Prioritize stability, bounded reference control, physical camera logic, and pasteability over extra wrappers or parallel variants.

## Default Contract

- Output **one prompt only** by default. Do not create `稳定版`, `电影版`, `最终版`, or parallel variants unless the user explicitly asks.
- For a single continuous shot, output only `[主体]`, `[动作]`, `[镜头]`, `[风格]`, `[约束]`, and `[音频]`, plus optional `[终帧]` when the ending must be locked.
- Do not emit `【基础设定】`, `【参考素材使用】`, `【分镜与景别】`, or `【提示词】` around a single-shot prompt. Their useful facts belong inside the six fields.
- Use the minimum sufficient structure. Give each control fact one owner and state it once. Repeat only a cross-shot invariant or a targeted lock for a known failure.
- Resolve creative choices before writing. Commit to one visible action, pose, contact method, composition, and ending per beat; do not leave `或`, `或者`, `二选一`, `A/B`, or `可选` branches unless variants or controlled randomness were requested.
- A reference can own motion or camera, but shorthand such as `按@视频1落地` is not a substitute for visible contact order and terminal pose. Translate decisive contacts and the ending into the prompt.
- Resolve story-critical prop state with the same precision as body pose: holder/hand, grip or support point, orientation, contact relationship, and final visible location.
- Write the production prompt in Chinese by default. Use English or bilingual output only when requested.
- Treat mode, aspect ratio, duration, resolution, upload strategy, and reference type as preflight decisions. Keep UI and provider settings outside the production prompt unless the setting itself must be communicated to the runner in text.
- Always include audio: `[音频]` for a single shot and `【音频】` for a multi-shot prompt. Without fixed audio, write `无BGM` plus concrete ambience, Foley, or silence.
- Write what is visible and measurable. Translate `紧张`, `高级`, or `史诗感` into posture, gaze, hand pressure, camera distance, light direction, material behavior, and timing.
- Use positive anchoring. Replace `不要变形/不要乱动/不要换脸` with stable physical conditions.
- Keep one core action and one core camera behavior per shot unless the user explicitly asks for cuts.
- Lock one composition per shot. Preserve an accepted image/video's visible shot size, screen positions, depth, axis, negative space, and contact relationships without inventing coordinates.
- Preserve explicit optical and camera authority. Carry forward source-authoritative focal length, FOV, perspective, angle/height/axis, movement direction/speed, focus, stability, and camera phase unchanged. Do not invent a companion lens/FOV value.
- Treat each generation block as self-contained. Do not rely on scene numbers, `延续上一段`, or hidden story memory unless an uploaded reference or handoff frame carries that state.
- When an accepted reference already locks appearance, composition, light, or camera, state its bounded role in the field that owns that fact and describe only the requested delta.
- Keep style distributed, not front-loaded. Put performance and physics in `[动作]`, composition and optics in `[镜头]`, and light/color/texture in `[风格]`.
- Do not generate Nano Banana/image prompts from this skill. If an image must be locked first, output an image anchor card and defer image-prompt writing to the dedicated image skill.
- Do not invent platform limits, hidden API paths, or current UI/API choices. Follow the current provider's visible options or documentation.

Ask at most one concise question only when a missing fact blocks execution. Otherwise choose the most stable production answer and generate directly.

## Preflight

Before composing:

1. Select shot precision: one continuous shot, ordered cuts without timecodes, or timed cuts. Use freestyle B-roll only when the user explicitly wants the model to choose angles.
   - Select one camera regime for each shot: `locked-presentational`, `observational-handheld`, or `stabilized-follow`. Encode it inside `[镜头]` or the owning shot line; do not create a new output section or mix regimes inside one shot.
2. Map every reference to bounded ownership and resolve conflicts before output.
3. Check that the first frame can be reconstructed: subject, start state, screen position/depth, orientation, gaze, contact points, light source, and camera axis.
4. Capture source-authoritative optics and camera facts unchanged.
5. Resolve one action path, one prop state, one camera behavior, one ending, and audio.
6. Give every camera move a visible or dramatic reason, execute one primary movement at a time, and define where it settles or holds. If a continuous shot needs multiple movement phases, serialize them and state each settle point. If movement adds no information or emotional change, simplify it.
7. For repairs, identify the smallest failing variable and preserve accepted facts.

## When To Read References

- Read `references/director-control.md` for first-frame blocking, character positioning, gaze, contact points, reference scope, shot precision, camera motivation, composition/optics ownership, or final-frame control.
- Read `references/platform-workflow.md` for provider/API boundaries, upload strategy, real-person policy, first-image workflows, extension canon, reference-count strategy, or low-resolution validation.
- Read `references/troubleshooting.md` when the user reports a defect or asks why a result failed.
- Read `references/vocabulary.md` for precise lens/FOV, cut, camera-recipe, lighting, color, texture, physical, measurable, or audio terms.
- Read `references/examples.md` when matching output density for single-shot, multimodal, first/last-frame, edit, extension, sequential-cut, or timed prompts.

## Reference Rules

Mirror the exact labels visible in the current provider, such as `@图片1`, `@视频1`, and `@音频1`. Do not infer a reference-count limit; keep the set lean and follow the provider's visible limit.

Do not create a separate reference manifest for an ordinary single shot. Declare each role at the point of ownership:

- `[主体]`: identity, face, body, wardrobe, product, prop, environment, and visible start state.
- `[动作]`: motion path, performance, timing, lip movement, contact order, and physics.
- `[镜头]`: first/last-frame composition, shot size, screen geometry, optics, camera axis, movement, and focus.
- `[风格]`: light, color, texture, material finish, and style reference.
- `[音频]`: dialogue, music, beat, ambience, and sound reference.

The same reference may appear in more than one field only when it owns different facts in each field. State the role explicitly every time; do not let a tag silently acquire new control.

If references conflict, resolve the priority inside the field that owns the disputed fact. For example, `[主体] 人物面孔以@图片1为唯一身份权威；@图片2只锁定服装。`

Include a reference tag only in the field or shot where its subject, prop, or control role is active. Do not carry unused tags into later cuts. Restate action-critical small text, logo, color, or prop state in words when it must remain visible; use postproduction for exact typography when necessary.

## Output Format

Choose exactly one contract. Do not mix the six-field stack with a multi-shot list.

### Compact Single-Shot Contract

Use for one continuous shot or one simple beat. Output exactly this field stack, without a title or outer section:

```text
[主体] ...
[动作] ...
[镜头] ...
[风格] ...
[约束] ...
[音频] ...
```

Add `[终帧]` only when ending composition, first/last-frame generation, extension handoff, or drift repair requires it.

### Sequential Multi-Shot Contract

Use when cut order matters but exact seconds do not:

```text
【分镜】
镜头1：唯一景别与构图；唯一主动作；一个运镜；必要的光色与声音。
镜头2：...
转场：...

【跨镜头一致性】
...（仅在两个以上镜头确实共享身份、服装、道具、空间、光色或故障修复时出现）

【音频】
...
```

### Timed Multi-Shot Contract

Use when beats must land on a clock:

```text
【分镜】
镜头1 [0:00-0:04]：唯一景别与构图；唯一主动作；一个运镜；必要的光色与声音。
镜头2 [0:04-0:08]：...
转场：...

【跨镜头一致性】
...（按需出现）

【音频】
...
```

For either multi-shot contract, put a reference role inside the shot where it applies; put only true cross-shot reference ownership in `【跨镜头一致性】`. Omit that section when nothing must be carried across cuts. Do not append the six-field stack after `【分镜】`.

Do not add a title before any contract. Do not append explanations after the prompt unless the user asked for reasoning.

## Field Rules

### [主体]

Absorb the useful content that previously lived in `【基础设定】`: where and when the shot happens, who or what is visible, wardrobe/product/prop, environment, and the reconstructable start state. Include identity, wardrobe, product, prop, or scene reference roles here.

Good:

- `[主体] 夜晚雨后的街口，@图片1锁定25岁女性的面孔、黑色短发和黑色风衣；她站在霓虹招牌下，右手靠近领口，双脚踩在同一湿地反光位置。`

Keep story recap, UI settings, and vague hype out of this field.

### [动作]

Write one continuous, physically plausible action path in present tense. Include action/video-reference roles, performance, gaze changes, breath, hand pressure, body tension, decisive hand/foot/object contacts, prop changes, and the terminal body/object state.

Choose one order. Write `右膝先触地，左脚随后踏实` rather than `单膝或单手触地`. Do not hide decisive contacts behind `沿用参考动作`.

### [镜头]

This field is the sole owner of both static screen geometry and camera execution:

`起始景别与首帧构图 + 主体屏幕位置/深度/比例 + 前中后景与负空间 + 继承的光学关系或一个焦段/FOV + 角度/高度/轴线 + 摄影机制度与稳定基底 + 可见触发/跟随对象 + 一个主运镜 + 速度/幅度/操作质感 + 收住目标/停留 + 焦点 + 必要的结束景别`

The opening must make the first frame reconstructable. When a reference owns composition, write that role here and inherit its visible geometry without inventing percentages or optics. If the reference supplies no numeric lens/FOV, write `继承参考的原始透视与镜头关系`.

Examples:

- `[镜头] 中近景，人物位于画面中央偏右，前景保留虚化雨滴，背景是湿润街面和车灯；85mm中长焦，眼平机位，摄影机因人物回头而缓慢横移半个身位，云台稳定，焦点锁定眼睛。`
- `[镜头] @图片1锁定首帧中景构图、人物屏幕位置和原始透视；摄影机只后退约10%以揭示街机屏幕，眼平轴线不变，云台稳定，焦点保持在眼睛和手部。`

Preserve every source-authoritative camera fact. Do not derive a numeric FOV from focal length or add a preferred lens when the accepted reference already owns perspective.

For dialogue or lip-synced performance, keep the active speaker frontally readable and let the camera settle during the line. Move or reframe between lines or reaction beats unless an accepted source authority explicitly requires otherwise.

### [风格]

Write one coherent scene-specific look: light source and direction, exposure, color as material/light/role, skin or product treatment, texture, grain, and finish. Include style-only reference roles here. Avoid unrelated adjective stacks and keep technical output settings outside the prompt.

### [约束]

Use short positive fixers only for likely failures: identity, contact points, prop state, screen position, continuity, white balance, focus, and final state. Do not recap the other five fields.

For multiple characters, lock left/right, depth, gaze, crossing, and occlusion only when those failures are plausible.

### [音频]

Always write this field.

- No fixed music: `无BGM，保留雨声、远处车流声和衣料摩擦声。`
- Silence: `无BGM，静音处理，动作节奏由画面运动承担。`
- Audio reference: `@音频1锁定对白或节奏，画面动作贴合主要拍点。`
- Dialogue/singing: keep one main speaker or singer per shot.

### [终帧]

Optional. Use only when the ending must be reconstructed for first/last-frame generation, extension, drift repair, product/logo end state, or complex blocking. State one visible final composition, pose/contact state, gaze, prop state, and focus.

## Mode Handling

Keep mode internal; do not emit `【模式】`.

- Text-to-video: make subject, action, camera, look, and sound explicit.
- Image-anchored: declare image ownership in the fields it actually controls and describe only the requested delta.
- First/last-frame: assign start/end composition roles in `[镜头]`, identity in `[主体]`, and one transition path in `[动作]`.
- Multimodal: distribute bounded roles across owning fields and resolve conflicts before output.
- Edit: state preserved subject/scene/camera facts in their fields, then describe only the named change.
- Extend: treat the latest accepted ending as canon; rejected attempts and completed beats are not new actions.
- Audio-aware: keep one main speaker/singer or one clear beat relationship per shot.

### Extension Continuation Canon

- Use the latest accepted clip or approved handoff frame as source of truth.
- Let the source own final pose/contact state, identity, wardrobe/props, environment, light/color, composition, optics, camera phase, focus, and sound bed. Let the new prompt own only the visible delta.
- Convert a completed beat into a start-state fact; do not replay it. Continue body/camera motion only when visibly active at the cut.
- Re-anchor briefly, perform one new action, and end on one reconstructable handoff state.
- After two chained extensions, or at the first visible drift, re-anchor from the latest accepted clip/frame plus the smallest persistent reference set.

## Image-First Workflow

If the image is not decided, output this planning card before the later video prompt:

```text
【图像锚定卡】
[主体锚点] ...
[构图锚点] ...
[风格锚点] ...
[必须保留细节] ...
[转视频时的首帧用途] ...
```

## Complexity And Cut Rules

- 4-8 seconds: one strong action.
- 8-12 seconds: one action plus one reveal.
- 12-15 seconds: two or three simple beats.
- Use ordered cuts without timecodes when sequence matters but exact beat timing does not.
- Use timed cuts only when action, dialogue, music, or a reveal must land at a specified moment.
- Use freestyle B-roll only when the user explicitly accepts model-selected angles; otherwise resolve the shot list.
- When cuts are specified, state only those cuts and do not invite extra camera cuts.
- Complex fight, chase, transformation, group scene, or spatial reversal: use a multi-shot list or separate generation blocks.
- If camera movement would break blocking, simplify the move and preserve screen positions.
- Treat length as a diagnostic, not a platform limit. If a 10-15 second multi-shot prompt exceeds about 1800 Chinese characters, remove duplicate facts or split the generation blocks.

## Deterministic Lint

When the final prompt is saved to a file and tools are available, run:

```bash
python3 "<skill-directory>/scripts/lint_prompt.py" <prompt.md> [--duration 14] [--authority <source.md>]
```

The linter checks legacy-wrapper leakage, contract mixing, missing fields/audio, field order, unresolved branches, inline reference ownership, rejected references, conflicting or unauthorized optics, cut-mode mixing, and timed continuity. Use `--no-invent-optics` when accepted authority supplies no numeric lens/FOV; extension checks can add `--rejected-ref` and `--require-reanchor`. Use `--allow-variants` only when variants were explicitly requested. Apply the same checks manually for chat-only output.

## Quality Checklist

Before delivering, verify:

- Output one prompt and exactly one contract.
- A single shot contains only the six required fields in order, plus optional `[终帧]`.
- No legacy outer sections remain in a single-shot prompt.
- Every reference role is declared in the field or shot that owns it; unused tags are absent.
- `[主体]` reconstructs scene, subject, and visible start state.
- `[动作]` contains one action/contact/prop path and one terminal state.
- `[镜头]` reconstructs the first frame and owns all composition, optics, camera execution, and movement motivation.
- Source-authoritative optics and camera facts remain unchanged; unsupported companion values are absent.
- Multi-shot prompts use ordered or timed shots, optional `【跨镜头一致性】`, and `【音频】`, with no six-field recap.
- An extension uses only the latest accepted handoff and excludes rejected takes and completed beats.
- Locks are positive and limited to likely failures; `[终帧]` appears only when needed.
