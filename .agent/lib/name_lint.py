"""Strict-tier name-lint validator for dashboard files.

Detects honorifics, postnominals, and known fabricated expert names
in dashboard interpretation files (JS/HTML/MD).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class NameViolation:
    file: Path
    line: int
    column: int
    matched_text: str
    rule: str


STRICT_PATTERNS: list[tuple[str, str]] = [
    (r'\b(Dr|Prof|Professor|Adv)(?:\.|\s+[A-Z])', 'honorific'),
    (r',\s*(?:PhD|DPhil|MD|JD|EdD|MBBS)\b', 'postnominal'),
    (
        r'\b(Elena Vasquez|Amira Khalil|Kwame Osei-Mensah|Daniel Kiprotich'
        r'|Aroha Te Kanawa|Priya Sharma|Yuki Tanaka-Morrison|Miriam Johansson'
        r'|Ricardo Mendoza-Lagos|James Crawford|Fatima Al-Rashid|Sarah Chen)\b',
        'known-fabricated-name',
    ),
]

_COMPILED_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(pat), rule) for pat, rule in STRICT_PATTERNS
]

# Fields in JS files that carry attribution names
_JS_ATTR_FIELDS = re.compile(
    r'(?:expertName|member|councilMember|author|attributedTo|reviewer)\s*:\s*"([^"]*)"'
)


def lint_file(path: Path) -> list[NameViolation]:
    """Scan every line of *path* against STRICT_PATTERNS."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    violations: list[NameViolation] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for compiled, rule in _COMPILED_PATTERNS:
            for m in compiled.finditer(line):
                violations.append(
                    NameViolation(
                        file=path,
                        line=lineno,
                        column=m.start() + 1,
                        matched_text=m.group(),
                        rule=rule,
                    )
                )
    return violations


def lint_js_attribution_fields(path: Path) -> list[NameViolation]:
    """Extract JS attribution field values and lint each one."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    violations: list[NameViolation] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for field_match in _JS_ATTR_FIELDS.finditer(line):
            value = field_match.group(1)
            if not value:
                continue
            value_start = field_match.start(1)
            for compiled, rule in _COMPILED_PATTERNS:
                for m in compiled.finditer(value):
                    violations.append(
                        NameViolation(
                            file=path,
                            line=lineno,
                            column=value_start + m.start() + 1,
                            matched_text=m.group(),
                            rule=rule,
                        )
                    )
    return violations
