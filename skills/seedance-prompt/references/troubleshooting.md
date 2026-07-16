# Troubleshooting Reference

Read this when the user reports a bad Seedance result, asks why a shot failed, or wants a repair prompt.

## Repair Workflow

1. Identify the visible failure.
2. Keep accepted parts unchanged.
3. Remove conflicting or low-priority references.
4. Rewrite the smallest prompt area that controls the failure.
5. Change one variable per retry when practical.

## Failure Matrix

### Narrative Or Shot Logic Breaks

Symptoms: teleporting, missing intermediate beat, unclear cause/effect, wrong order.

Fix:

- split into timed shots or separate generation blocks
- give each segment one narrative task
- write explicit start state and final frame
- use hard cuts when continuity is more important than a single take

### Image Anchor Does Not Stick

Symptoms: character, outfit, product, or composition drifts away from approved still.

Fix:

- state `@图片1 作为首帧/人物外观/构图参考`
- reduce action range
- reduce camera movement
- add identity, wardrobe, silhouette, and contact-point locks
- remove secondary references that contradict the approved image

### Subject Drifts Or Floats

Symptoms: feet slide, character changes screen position, body floats.

Fix:

- add screen position and depth
- add ground contact points
- lock body state and allowed micro-motions
- use slower camera movement
- specify that camera motion preserves composition

### Characters Swap Positions

Symptoms: two people switch sides, cross the center line, or merge.

Fix:

- define Character A and Character B separately
- lock left/right side, depth, distance, gaze, and crossing rule
- preserve central negative space
- simplify action so neither character crosses the center line

### Face, Hands, Or Body Deforms

Symptoms: unstable face, wrong proportions, extra fingers, distorted limbs.

Fix:

- reduce action intensity
- keep face/hands in controlled focus
- anchor natural body proportions
- avoid combining fast movement, close-up face, and complex hand action
- use stable shot size instead of extreme dynamic camera

### Camera Feels Random

Symptoms: unexpected cuts, uncontrolled pans, inconsistent framing.

Fix:

- choose one camera behavior
- state movement speed and stability
- lock focus target
- say the camera preserves subject screen position
- use `固定机位` or `缓慢推进` for repair attempts

### Style Or Color Drifts

Symptoms: style changes mid-shot, color temperature flickers, lighting resets.

Fix:

- choose one main visual anchor
- state light source, color palette, texture, and white-balance stability
- remove contradictory style stacks
- keep environment and exposure continuity in `[约束]`

### Audio Or Dialogue Fails

Symptoms: lip sync poor, too many speakers, beat mismatch.

Fix:

- use one main speaker/singer per shot
- shorten dialogue
- specify timing only for the key line
- use `@音频1` only for rhythm/dialogue if it is actually supplied
- if audio is not fixed, default to `无BGM`

### Edit Video Changes Too Much

Symptoms: background, camera, lighting, or untouched areas mutate.

Fix:

- start with preservation scope
- define the exact replacement/addition/removal
- name untouched areas
- preserve duration, camera, lighting, and space when appropriate
- reduce edit scope before retrying

### Extension Has A Seam

Symptoms: continuation does not match source ending.

Fix:

- use the latest accepted ending, never a rejected retry, as the handoff authority
- describe that ending's final visible pose, contact state, composition, optics, camera phase, focus, and active motion
- convert actions completed before the cut into start-state facts instead of replaying them
- continue camera/body motion only if it is visibly active at the cut; otherwise begin from the settled ending state
- continue existing camera direction and speed
- preserve subject identity, light, color, and environment
- make the first new action small and physically connected
- after repeated chained extensions or the first drift, re-anchor from the latest accepted clip/frame and the smallest persistent reference set
- write final frame for the extension

### Text Or Logo Is Unreadable

Symptoms: garbled subtitle, wrong slogan, unstable logo.

Fix:

- keep text short
- use simple words and common punctuation
- specify timing, position, font style, color, and size
- avoid long sentences or multiple text blocks
- for exact logos, prefer compositing in post unless the generation only needs a rough placeholder

## Minimum Repair Template

```text
保留：...
修正：...
参考优先级：...
动作限制：...
镜头限制：...
终帧：...
```

Convert this into the normal prompt format before final delivery.
