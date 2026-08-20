# -*- coding: utf-8 -*-
"""Normalize NABH PDF Private-Use-Area ligature glyphs to ASCII.

NABH Hospitals 6th Edition portal PDF embeds ``fi`` / ``fl`` as custom
Private Use Area glyphs (U+F001 / U+F002) instead of U+FB01 / U+FB02.
pdftotext preserves those codepoints. When the DOCX is opened without the
NABH font, the glyphs vanish and words read as ``identies``, ``denes``,
``ofcer``, ``ow``, etc.

Call :func:`normalize_nabh_text` on every string that enters the v2 draft /
render pipeline so future chapters (MOM, PRE, IPC, …) stay clean.
"""
from __future__ import annotations

import re
from typing import Any

# Primary fix: map PDF PUA + Unicode ligatures to ASCII digraphs.
LIGATURE_MAP = str.maketrans(
    {
        "\uf001": "fi",  # NABH PDF PUA "fi"
        "\uf002": "fl",  # NABH PDF PUA "fl"
        "\ufb01": "fi",  # standard Latin ligature fi
        "\ufb02": "fl",  # standard Latin ligature fl
        "\ufb00": "ff",
        "\ufb03": "ffi",
        "\ufb04": "ffl",
    }
)

# Secondary repair: already-stripped ASCII forms (fi/fl missing entirely).
# Built from words observed in HCO extracts; extend as new forms appear.
# Longer keys first so "identication" wins over shorter stems.
_STRIPPED_FI_FL: list[tuple[str, str]] = [
    ("identication", "identification"),
    ("identications", "identifications"),
    ("identiying", "identifying"),
    ("identies", "identifies"),
    ("identied", "identified"),
    ("insufcient", "insufficient"),
    ("sufcient", "sufficient"),
    ("efcient", "efficient"),
    ("signicant", "significant"),
    ("specication", "specification"),
    ("specications", "specifications"),
    ("benefts", "benefits"),
    ("beneft", "benefit"),
    ("certicate", "certificate"),
    ("certicates", "certificates"),
    ("artiicial", "artificial"),
    ("denitions", "definitions"),
    ("denition", "definition"),
    ("denes", "defines"),
    ("dened", "defined"),
    ("dening", "defining"),
    ("modied", "modified"),
    ("qualied", "qualified"),
    ("classied", "classified"),
    ("justied", "justified"),
    ("claried", "clarified"),
    ("simplied", "simplified"),
    ("ofcers", "officers"),
    ("ofcer", "officer"),
    ("ofcial", "official"),
    ("ofce", "office"),
    ("ofers", "offers"),
    ("ofering", "offering"),
    ("ofered", "offered"),
    ("ofer", "offer"),
    ("proles", "profiles"),
    ("prole", "profile"),
    ("specied", "specified"),
    ("specic", "specific"),
    ("afrm", "affirm"),
    ("conrm", "confirm"),
    ("ndings", "findings"),
    ("nalise", "finalise"),
    ("nalize", "finalize"),
    ("rst", "first"),
]


def _repair_stripped_ascii(text: str) -> str:
    """Restore fi/fl in already-stripped ASCII tokens (case-preserving)."""

    def repl_word(match: re.Match[str]) -> str:
        word = match.group(0)
        lower = word.lower()
        for bad, good in _STRIPPED_FI_FL:
            if lower == bad:
                # Preserve capitalization pattern of the original token.
                if word.isupper():
                    return good.upper()
                if word[0].isupper():
                    return good[0].upper() + good[1:]
                return good
        return word

    # Match letter-runs long enough to be candidates.
    return re.sub(r"[A-Za-z]+", repl_word, text)


def normalize_nabh_text(text: str) -> str:
    """Replace NABH PUA ligatures and repair known stripped ASCII forms."""
    if not text:
        return text
    text = text.translate(LIGATURE_MAP)
    text = _repair_stripped_ascii(text)
    return text


def normalize_nabh_obj(obj: Any) -> Any:
    """Deep-normalize all strings in a draft dict / list structure."""
    if isinstance(obj, str):
        return normalize_nabh_text(obj)
    if isinstance(obj, list):
        return [normalize_nabh_obj(x) for x in obj]
    if isinstance(obj, dict):
        return {k: normalize_nabh_obj(v) for k, v in obj.items()}
    return obj


def distribution_dedupe(parts: list[str]) -> str:
    """Join distribution roles with '; ', dropping exact casefold duplicates."""
    seen: set[str] = set()
    out: list[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        key = p.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return "; ".join(out)
