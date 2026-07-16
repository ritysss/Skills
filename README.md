# Rity AI Prompt Skills

Two production-focused Codex skills for AI image and video prompt engineering.

## Skills

- `nano-banana-prompt` — writes Nano Banana Pro / Gemini 3 Pro Image prompt packages for image generation, editing, typography, product images, posters, and character-consistent visual assets.
- `seedance-prompt` — writes provider-aware Seedance-compatible video prompts for text-to-video, multimodal references, editing, extension, ads, dialogue, action, and cinematic blocking. Single shots use a compact six-field contract; sequential and timed shot lists are used only when cuts are required.

## Install

Copy the skill folders into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/nano-banana-prompt ~/.codex/skills/
cp -R skills/seedance-prompt ~/.codex/skills/
```

Then restart Codex or reload skills.

## Notes

- These are prompt-engineering skills. They do not call image or video generation APIs directly.
- Provider limits and model availability can change. The skills prefer current provider settings over hard-coded assumptions.
- `nano-banana-prompt` uses current Gemini 3 Image GA model IDs as of June 2026.

## License

License is pending final confirmation before public release.
