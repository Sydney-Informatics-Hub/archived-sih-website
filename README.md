# Sydney Informatics Hub: Archived Website

This repository is an **archived snapshot of the Sydney Informatics Hub (SIH) website as it stood in 2021**. It is kept for reference only and is **no longer updated**.

- **Archived site:** <https://sydney-informatics-hub.github.io/archived-sih-website/>
- **Current SIH website:** <https://informatics.sydney.edu.au/>

Information on the archived site, including services, people, contact details, training, projects and links, is out of date and should not be relied on. Many external links have likely stopped working.

The repository contains only the final state of the site. The original development history is not included.

## What's here

The site is a static website built with [Hugo](https://gohugo.io/) and a customised copy of the [Mainroad](https://github.com/Vimux/Mainroad) theme (see `themes/mainroad/LICENSE.md`).

| Path | Contents |
| --- | --- |
| `content/` | Pages, news and blog posts (Markdown with TOML front matter) |
| `layouts/` | Site-specific templates and shortcodes, overriding the theme |
| `themes/mainroad/` | The theme, with local modifications |
| `static/` | Images, documents, CSS/JS assets and other files copied as-is |
| `data/` | Data used by templates (see note below) |
| `dynamic/` | Python scripts that generated project pages from SIH's internal JIRA. **Historical only: they need access to an internal system and cannot be run.** |
| `.github/workflows/hugo.yml` | Builds the site and deploys it to GitHub Pages |
| `WebsiteProjectSummaries.pdf` | Original instructions for the JIRA-to-website project summaries workflow |

## Changes made for the archive

Compared with the live site as it last ran, the archived copy has these differences:

- An "Archived copy" banner is shown on every page, and the site title reads "Sydney Informatics Hub Archived Website".
- The page redirects added in late 2019 (a `redirectTo` front-matter field, `.htaccess` rules and meta-refresh tags) have been removed so the old content is viewable. The only redirects left are Hugo `aliases` between old and new internal URLs.
- The navigation menu has been re-enabled.
- Google Analytics was replaced with [GoatCounter](https://www.goatcounter.com/).
- Instagram and Twitter embeds were replaced with plain links, because Hugo fetches embed data at build time and those APIs no longer respond.
- `data/closed-projects.json` was empty in the source snapshot and now contains `[]` so the build succeeds.
- Large images and PDFs were compressed to reduce the repository size.

## Building locally

The templates only work with **Hugo 0.54.0**. Newer versions (0.55 onwards) break the theme. Use the standard (not "extended") build.

1. Download Hugo 0.54.0 from the [v0.54.0 release page](https://github.com/gohugoio/hugo/releases/tag/v0.54.0) for your platform and put the `hugo` binary on your path. The release only includes macOS builds for Intel, which run on Apple Silicon under Rosetta.
2. From the repository root, run:

   ```
   hugo server --baseURL http://localhost:1313/
   ```

3. Open <http://localhost:1313/>.

To produce the site in `public/` instead, run `hugo`. The `public/` folder is git-ignored.

## Deployment

Every push to `main` runs `.github/workflows/hugo.yml`, which:

1. Installs Hugo 0.54.0.
2. Builds the site using the base URL that GitHub Pages provides.
3. Prefixes root-absolute links (such as `href="/services/"`) with the Pages base path. The templates and content use these links, and they would otherwise break when the site is served from `/archived-sih-website/`.
4. Publishes the result with GitHub Pages.

In the repository settings, Pages must be set to the **GitHub Actions** source. The workflow can also be started manually from the Actions tab.

## Page format (for reference)

Pages are Markdown files in `content/` with TOML front matter:

```
+++
date = "2017-06-05T17:25:22+10:00"
title = "Training"
draft = false
type = "sidebar"
stream = "all"
+++
```

- `title` is the page title. A `thumbnail` image can also be set, and it appears at the top of news pages.
- `date` is the authorship date. Pages dated in the future are not built.
- `draft = true` hides the page from the build.
- `type = "sidebar"` shows the sidebar, which has the search box and context-dependent widgets. `stream` selects a news feed: `"news"`, `"blogs"`, or `"all"` for both.
