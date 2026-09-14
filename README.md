# Matrix Digital Rain

An interactive digital rain in a single self-contained HTML file. No build step, no dependencies, no server — open `index.html` and it runs.

Two modes:

- **fly** (default) — a camera travelling through a corridor of falling code, with depth parallax, warp, and a dolly-zoom lens
- **classic** (`M`) — flat columns on fixed depth planes, closer to what the film actually shows

Every field is grown from a seed, so the same seed always produces the same rain.

## Controls

| | desktop | touch |
|---|---|---|
| steer | move the mouse | drag |
| speed | scroll, or `W` / `S` | two fingers up/down |
| warp | `space` | double-tap |
| palette | `C` | **colour** button |
| fly / classic | `M` | **mode** button |
| fullscreen | `F` | — |
| vignette + scanlines | `V` | — |
| bloom | `B` | — |
| save a PNG | `P` | — |
| hide the HUD | `H` | **hide** button |

## URL options

Everything lives in the hash, so a look is a shareable link:

```
index.html#seed=matteo&palette=amber&density=320&msg=WAKE+UP&mode=classic
```

| option | meaning |
|---|---|
| `seed=<string>` | grows the whole field — density, every strand, and the hue under `palette=seed` |
| `palette=` | `green` (default) `amber` `ice` `magenta` `blood` `gold`, or `seed`, or `auto` (tracks the clock) |
| `density=<n>` | strand count, 40–900 (otherwise derived from the seed) |
| `msg=<text>` | hidden message strands; they decode under the cursor |
| `glyphs=<chars>` | use your own character set |
| `mode=classic` | start flat instead of flying |
| `bloom=0..1` | bloom strength, `0` to disable |
| `idle=1` | drift the camera when left unattended |
| `motion=1` | fly even when the OS asks for reduced motion |
| `debug=1` | frame time, glyph and glow counts, render scale, font scaling |

## Notes

The glyphs are half-width katakana drawn mirrored, as in the film. Latin comes from a monospace face, scaled to match the kana stroke height and condensed to the same cell width, so every glyph occupies one uniform cell. On a machine with no Japanese font installed the kana are dropped rather than rendered as boxes.

Rendering adapts to the device: a frame-time governor steps the render scale and far-cull down when frames are dropped and back up when there is headroom, and bloom is dropped on the first step down.

`prefers-reduced-motion` starts the page in classic mode — no camera travel — and stops glyphs flashing when they change.

## Live

Published as a hosted page from `build/artifact.html`, which is derived from
`index.html` — never edited directly:

```
python3 tools/build-artifact.py
```

The Artifact runtime supplies its own document wrapper, so the build strips
`<!doctype>`, `<html>`, `<head>` and `<body>` and the document-level metadata
the host owns. Two controls are unavailable in an embedded frame and degrade
quietly there: `P` (save a PNG) is hidden, and `F` (fullscreen) is a no-op.

## Licence

[CC BY-NC-SA 4.0](LICENSE) — share and remix with attribution, non-commercial, share alike.
