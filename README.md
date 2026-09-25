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
| warp | `space` | double-tap, or **warp** |
| palette | `C` (`shift+C` back) | colour swatch button |
| fly / classic | `M` | mode button |
| new seed | `R` | — |
| copy a link to this look | `L` | — |
| fullscreen | `F` | — |
| vignette + scanlines | `V` | — |
| bloom | `B` | — |
| save a PNG | `P` | — |
| show the controls | `?` | **?** button |
| hide everything | `H` | **hide**, then long-press to bring it back |

The controls legend shows for a few seconds on load, then folds down to a one-line hint. It lists only the controls that work in the current mode and browser. Every change is confirmed by a short message at the top of the screen.

## URL options

Everything lives in the hash, so a look is a shareable link. Changing the seed, palette or mode updates the hash as you go, so the address bar always links to what is on screen. Editing the hash by hand reloads with the new values.

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
| `halo=0` | old bloom: one blur of the whole frame, instead of a thresholded core plus a wide halo |
| `ramp=0` | flat trails: no pale neck behind the head, linear falloff |
| `p3=0` / `p3=1` | never / always draw in Display-P3 (default: when the display supports it) |
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
the host owns. In an embedded frame, `P` (save a PNG), `L` (copy link) and
`F` (fullscreen) are left out of the legend. Pressing them there shows a
message saying they are unavailable.

## Licence

[CC BY-NC-SA 4.0](LICENSE) — share and remix with attribution, non-commercial, share alike.
