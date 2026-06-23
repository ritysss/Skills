# Platform And Workflow Reference

Read this when a task depends on provider behavior, upload strategy, settings language, real-person/portrait support, long-video planning, first-image workflow, or API/platform boundaries.

## Provider-First Boundary

- Default to the runner/provider the user is actually using.
- If the user says they use a third-party/API gateway that supports real-person references, do not apply 即梦网页 face-upload restrictions to the prompt.
- If the user explicitly uses official 即梦网页 or 火山方舟, follow that route's current restrictions and docs.
- Do not present web-front-end limitations as universal Seedance model limitations.
- Do not mention `asset://` or SDK details unless the user explicitly asks about official API/Fangzhou/SDK.
- If exact platform limits, model menus, membership tiers, or resolution choices matter, use wording like `以当前入口/当前 provider 可选项为准` instead of inventing values.
- If the current provider behavior conflicts with this reference, the current provider wins.

## Reference Strategy

Use the smallest set of references that can control the shot:

- one locked first frame for composition and identity
- one identity/wardrobe reference when first frame is not enough
- one environment reference if the scene must stay specific
- one video reference only for motion/camera rhythm
- one audio reference only for beat, dialogue, or ambience

Avoid uploading too many references for local fixes. Too many references can reintroduce old wardrobe, scene, or composition errors.

## Mode Selection

- Text-to-video: no visual anchor; write subject, action, camera, and style explicitly; add a final-frame lock only when the ending composition matters.
- Image-anchored video: approved still controls first frame, identity, product, or composition.
- First/last-frame video: start and end stills define transition.
- Multimodal reference: combine image/video/audio, but assign one job per material.
- Edit video: preserve what should stay, change only the named region/object/action, and protect untouched areas.
- Extend video: describe the source ending state, then write the new continuation.
- Audio-aware video: one main speaker/singer or one clear beat relationship per shot.

## Settings Language

Keep settings out of `【基础设定】`.

Mention settings outside the prompt only if helpful:

- start with short low-cost tests when uncertain
- lock aspect ratio before reference preparation
- use current provider choices for duration and resolution
- move to higher resolution only after composition, identity, and motion are accepted

For production workflows, prefer:

1. low-resolution or short-duration test for motion/composition
2. review the actual output
3. revise one variable at a time
4. generate final resolution only after the shot logic is accepted
5. upscale or finish externally only after the Seedance result is compositionally correct

## Long Video Strategy

Do not force a long story into one prompt.

- 4-8 seconds: one strong action.
- 8-12 seconds: one action plus one reveal.
- 12-15 seconds: two or three simple timed beats.
- Long scenes: split into independent generation blocks with a clear handoff frame.
- Keep original audio external when video generation is visual-only; add final sound design in editing.

For each block, define:

- start state
- end state
- reference roles
- one narrative task
- one camera strategy
- continuity locks
- final frame/handoff frame

## First-Image Workflow

If the video depends on an image that is not locked yet:

1. output `【图像锚定卡】`
2. state what the later approved image will control
3. do not write a full Nano Banana/image prompt in this skill
4. after the image is approved, write the Seedance prompt with that image as `@图片1`

Use the image card to protect:

- subject identity
- wardrobe/product
- composition
- scene geometry
- light/color
- details that must survive video generation

## Real-Person And API Policy

- Do not make the skill itself reject human faces. The prompt writer should adapt to the user's provider.
- For official 即梦网页/火山方舟, treat realistic human face reference support as restricted unless current docs or the user-provided route say otherwise.
- For third-party/API gateways that support verified real-person references, write normal portrait/identity prompts and preserve face consistency, expression, body, wardrobe, and consent-safe identity language.
- Do not promise any provider will accept a request unless the current route is verified or the user confirms it works.
- When platform support is uncertain, phrase it as a provider/workflow note, not as a prompt limitation.

## Production Handoff

When upstream assets are already accepted:

- translate the accepted shot card, still, or storyboard into a Seedance prompt
- do not redesign the story, character, wardrobe, or scene unless requested
- if references conflict, surface the conflict and assign priority
- preserve project authority assets over style inspiration

When generated output is being reviewed:

- judge the actual output, not the intended prompt
- identify the smallest failing variable
- revise only the variable that caused the failure
- keep accepted identity, scene, and timing intact
