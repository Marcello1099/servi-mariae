# Branding

## Font

**Fraunces** — variable serif, weights 400/450/500/600 + italic 400.

Loaded Google Fonts in `themes/servi-mariae/layouts/partials/head.html`, declared in `themes/servi-mariae/assets/css/main.css`. Fallback `Georgia, serif`.

## Palette

Sampled from `assets/avatar.png` (logo).

| Role | Hex | Notes |
|---|---|---|
| Marian blue | `#2b4593` | dominant, logo + accents |
| Ink | `#18171a` | text (CSS `--ink`) |
| BG / cream | `#faf7f1` | page background (CSS `--bg`) |
| Marian deep | `#1d3a8a` | CSS `--marian`, links/hover |
| Ink soft | `#4b494f` | secondary text |
| Muted | `#87828c` | meta/dates |
| Rule | `#e8e3da` | borders, hr |

Dark mode (auto, `prefers-color-scheme: dark`): `--bg #0f0f12`, `--ink #ece9e1`, `--marian #8aa6ff` (see `main.css` lines 13–22).
