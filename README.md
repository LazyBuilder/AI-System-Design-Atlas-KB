# AI System Design Atlas

Complete source and static website for **[LazyBuilder/AI-System-Design-Atlas-KB](https://github.com/LazyBuilder/AI-System-Design-Atlas-KB)**.

The site contains 20 canonical system-design patterns, six overlapping categories, 29 HTML pages, and 60 cloud implementation diagrams plus overview and icon assets. Each design has AWS, GCP, and Azure views, service documentation links, tradeoffs, failure modes, and evaluation notes.

## Copy and publish

1. Extract the complete ZIP.
2. Copy **the contents of the extracted folder** into your local `AI-System-Design-Atlas-KB` repository root. Replace matching files. Do not nest this package inside another folder in the repository. Preserve your existing `.git` directory.
3. Include the hidden `.github` directory and `.gitignore`. In macOS Finder, press **Command + Shift + .** to reveal hidden files. Merge `.github`; keep other unrelated workflows. If you already have a different workflow that deploys this same Pages site, remove that older deployment workflow to avoid competing deployments.
4. Commit and push the files to your repository's default branch. The workflow detects the default branch rather than assuming `main` or `master`.
5. On GitHub, open **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**.
6. Open **Actions → Verify and publish Atlas → Run workflow**, selecting the default branch. Later pushes to that branch publish automatically.
7. Open the successful deployment URL shown in the Actions run.

Expected URL for the standard project site: **https://lazybuilder.github.io/AI-System-Design-Atlas-KB/**. This is the intended URL, not confirmation that the repository is already deployed; a custom domain or account settings can change the final URL.

All necessary workflow settings that can be represented in the repository are included: static build and checks, `dist/` upload, deployment permissions, the `github-pages` environment, default-branch restriction, deployment concurrency, and published URL output. PRs run checks without deploying. The Pages **Source** setting is a GitHub repository setting and cannot be activated by copying a YAML file. Confirm GitHub Actions is allowed in Settings → Actions if your organization restricts it. The standard workflow requires no personal access token or custom repository secrets.

## What is included

See [REPOSITORY_MAP.md](REPOSITORY_MAP.md) for every packaged file and its purpose. `dist/` is complete, generated, and checked in; it can be opened locally without running a build. GitHub Actions rebuilds it before publication and uploads **only `dist/`**, so source and repository instructions are not published as website assets.

No `.git` history, credentials, caches, installed dependencies, or machine-specific configuration are included in the ZIP.

## Local preview

From the repository root:

```sh
python3 -m http.server 8765 --directory dist
```

Open **http://localhost:8765/**. Keep the preview server running while reviewing; a stopped local server makes localhost unavailable even when the files are valid.

You can also open `dist/index.html` directly. The provider control uses a local script and no service requests.

## Edit, build, and check

Requires Python 3.12+; Node.js 24 is used only for control verification. The published website requires neither runtime.

```sh
python3 build.py
python3 verify.py
node check-controls.cjs
```

There are no third-party Python or Node packages to install.

- `content.json`: categories, architecture text, primary references, and review dates.
- `cloud.py`: explicit per-block cloud mappings, service notes, and SVG generation.
- `build.py`: page templates and static generation.
- `style.css`: research layout, readable typography, colored labels, and responsive diagrams.
- `site.js`: local, accessible cloud-provider selection.
- `verify.py`: local links and fragments, complete cloud views, SVG validity, subpath support, privacy checks, and deployment configuration checks.
- `check-controls.cjs`: provider-switching logic and accessible-state checks.

Relative URLs and real `index.html` files preserve project-subpath links and page refreshes without application routing or rewrite rules. No repository-name-specific asset prefix is needed.

## Research and privacy

Core references were reviewed October 20, 2026. This distribution was reconstructed from the site developed in the accompanying work and assembled October 22, 2026. It was not merged against the remote repository: downloading that repository was not approved. Review for any independent changes you have made before replacing files.

Cloud diagrams and service mappings are illustrative editorial synthesis, not equivalent feature promises or ready-to-deploy infrastructure. Local inference, human review, and custom application code are explicitly distinguished from managed cloud services. Verify current regional and model support in the linked provider documentation.

The website is static and read-only. It contains no forms, accounts, analytics, cookies, visitor storage, third-party scripts, fonts, or embeds. Buttons change only published content visibility. If JavaScript is disabled, all three provider sections remain readable.

Local build, link, diagram, privacy, deterministic-rebuild, clean-package, and provider-control checks are included. A live GitHub deployment and visual browser review have not been verified for this package.
