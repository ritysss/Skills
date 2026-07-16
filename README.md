# Rity AI Prompt Skills

Two production-focused Codex skills for AI image and video prompt engineering.

## Skills

- `nanobanana-prompt` — writes copy-ready Nano Banana prompts for generation, surgical edits, exact text, products, posters, character consistency, and multi-reference role mapping, with provider-aware Pro/Flash routing.
- `seedance-prompt` — writes provider-aware Seedance-compatible video prompts for text-to-video, multimodal references, editing, extension, ads, dialogue, action, and cinematic blocking. Single shots use a compact six-field contract; sequential and timed shot lists are used only when cuts are required.

## Install

Copy the skill folders into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/nanobanana-prompt ~/.codex/skills/
cp -R skills/seedance-prompt ~/.codex/skills/
```

Then restart Codex or reload skills.

## Notes

- These are prompt-engineering skills. They do not call image or video generation APIs directly.
- Provider limits and model availability can change. The skills prefer current provider settings over hard-coded assumptions.
- `nanobanana-prompt` keeps cached official model guidance separate from live verification for current provider behavior.

## License

License is pending final confirmation before public release.
