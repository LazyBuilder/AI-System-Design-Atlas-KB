# Complete repository contents

Copy these files into the root of `LazyBuilder/AI-System-Design-Atlas-KB`.

## Structure

```text
AI-System-Design-Atlas-KB/
  .github/workflows/pages.yml
  .gitignore
  AGENTS.md
  MANIFEST.sha256
  README.md
  REPOSITORY_MAP.md
  build.py
  check-controls.cjs
  cloud.py
  content.json
  dist/.nojekyll
  dist/about.html
  dist/architectures.html
  dist/architectures/batch/index.html
  dist/architectures/chained-voice/index.html
  dist/architectures/computer-use/index.html
  dist/architectures/document/index.html
  dist/architectures/embedded-copilot/index.html
  dist/architectures/event-driven/index.html
  dist/architectures/human-review/index.html
  dist/architectures/hybrid/index.html
  dist/architectures/multi-agent/index.html
  dist/architectures/on-device/index.html
  dist/architectures/rag/index.html
  dist/architectures/realtime-voice/index.html
  dist/architectures/recommendation/index.html
  dist/architectures/request-response/index.html
  dist/architectures/review-loop/index.html
  dist/architectures/routing/index.html
  dist/architectures/streaming/index.html
  dist/architectures/tool-agent/index.html
  dist/architectures/wake-word/index.html
  dist/architectures/workflow/index.html
  dist/categories/applications/index.html
  dist/categories/background/index.html
  dist/categories/conversation/index.html
  dist/categories/devices/index.html
  dist/categories/orchestration/index.html
  dist/categories/voice/index.html
  dist/diagrams/atlas.svg
  dist/diagrams/batch-aws.svg
  dist/diagrams/batch-azure.svg
  dist/diagrams/batch-gcp.svg
  dist/diagrams/chained-voice-aws.svg
  dist/diagrams/chained-voice-azure.svg
  dist/diagrams/chained-voice-gcp.svg
  dist/diagrams/computer-use-aws.svg
  dist/diagrams/computer-use-azure.svg
  dist/diagrams/computer-use-gcp.svg
  dist/diagrams/document-aws.svg
  dist/diagrams/document-azure.svg
  dist/diagrams/document-gcp.svg
  dist/diagrams/embedded-copilot-aws.svg
  dist/diagrams/embedded-copilot-azure.svg
  dist/diagrams/embedded-copilot-gcp.svg
  dist/diagrams/event-driven-aws.svg
  dist/diagrams/event-driven-azure.svg
  dist/diagrams/event-driven-gcp.svg
  dist/diagrams/human-review-aws.svg
  dist/diagrams/human-review-azure.svg
  dist/diagrams/human-review-gcp.svg
  dist/diagrams/hybrid-aws.svg
  dist/diagrams/hybrid-azure.svg
  dist/diagrams/hybrid-gcp.svg
  dist/diagrams/icon.svg
  dist/diagrams/multi-agent-aws.svg
  dist/diagrams/multi-agent-azure.svg
  dist/diagrams/multi-agent-gcp.svg
  dist/diagrams/on-device-aws.svg
  dist/diagrams/on-device-azure.svg
  dist/diagrams/on-device-gcp.svg
  dist/diagrams/rag-aws.svg
  dist/diagrams/rag-azure.svg
  dist/diagrams/rag-gcp.svg
  dist/diagrams/realtime-voice-aws.svg
  dist/diagrams/realtime-voice-azure.svg
  dist/diagrams/realtime-voice-gcp.svg
  dist/diagrams/recommendation-aws.svg
  dist/diagrams/recommendation-azure.svg
  dist/diagrams/recommendation-gcp.svg
  dist/diagrams/request-response-aws.svg
  dist/diagrams/request-response-azure.svg
  dist/diagrams/request-response-gcp.svg
  dist/diagrams/review-loop-aws.svg
  dist/diagrams/review-loop-azure.svg
  dist/diagrams/review-loop-gcp.svg
  dist/diagrams/routing-aws.svg
  dist/diagrams/routing-azure.svg
  dist/diagrams/routing-gcp.svg
  dist/diagrams/streaming-aws.svg
  dist/diagrams/streaming-azure.svg
  dist/diagrams/streaming-gcp.svg
  dist/diagrams/tool-agent-aws.svg
  dist/diagrams/tool-agent-azure.svg
  dist/diagrams/tool-agent-gcp.svg
  dist/diagrams/wake-word-aws.svg
  dist/diagrams/wake-word-azure.svg
  dist/diagrams/wake-word-gcp.svg
  dist/diagrams/workflow-aws.svg
  dist/diagrams/workflow-azure.svg
  dist/diagrams/workflow-gcp.svg
  dist/index.html
  dist/site.js
  dist/style.css
  site.js
  style.css
  verify.py
```

## What the directories contain

- `.github/workflows/`: checked builds and GitHub Pages deployment.
- `dist/`: the entire published static website, including 29 pages and 62 SVGs.
- `dist/categories/`: six category collections linking to shared design pages.
- `dist/architectures/`: 20 canonical system-design pages with three cloud views each.
- `dist/diagrams/`: 60 provider-specific flows, an overview, and the icon.

The repository-root source files regenerate the published files; see `README.md` for editing and publishing. `MANIFEST.sha256` records the checksums of every packaged file other than itself.

No `.git`, cache, dependency, credential, or unrelated project files are included.
