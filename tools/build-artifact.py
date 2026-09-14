#!/usr/bin/env python3
"""Derive the Artifact-hosted copy from index.html.

The Artifact runtime supplies its own <!doctype>, <html>, <head> and <body>, so
the published file is the page *content* only: the <title>, the <style>, then
the body. Document-level tags that the host owns (charset, viewport, favicon,
Open Graph) are dropped -- the host sets those itself.

Deriving rather than forking means index.html stays the single source; run this
after any change and republish.

    python3 tools/build-artifact.py [out.html]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "build" / "artifact.html"


def section(html: str, tag: str) -> str:
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.DOTALL | re.IGNORECASE)
    if not m:
        raise SystemExit(f"index.html has no <{tag}> section")
    return m.group(1)


def main() -> None:
    html = SRC.read_text(encoding="utf-8")

    title = re.search(r"<title>(.*?)</title>", html, re.DOTALL | re.IGNORECASE).group(1).strip()
    style = section(html, "style")
    body = section(html, "body").strip()

    # The host owns document-level metadata; ours would be ignored or conflict.
    dropped = len(re.findall(r"<(?:meta|link)\b[^>]*>", section(html, "head"), re.IGNORECASE))

    out = f"<title>{title}</title>\n<style>\n{style.strip()}\n</style>\n\n{body}\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(out, encoding="utf-8")

    for tag in ("<!DOCTYPE", "<html", "<head", "<body"):
        if tag.lower() in out.lower():
            raise SystemExit(f"{tag} leaked into the artifact copy")

    print(
        f"{OUT.relative_to(ROOT) if OUT.is_relative_to(ROOT) else OUT}  "
        f"{len(out):,} bytes  (title {title!r}, dropped {dropped} meta/link tags)"
    )


if __name__ == "__main__":
    main()
