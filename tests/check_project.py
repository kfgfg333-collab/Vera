#!/usr/bin/env python3
"""Проверка целостности проекта «Вера: путешественница во времени».

Запуск из корня проекта:  python3 tests/check_project.py
Только стандартная библиотека. Ничего не меняет в файлах.
Проверяет: обязательные файлы, ссылки на файлы проекта в Markdown, формат skills,
закрытые блоки кода, отсутствие устаревших правил (кроме архивных тестов),
наличие ключевых правил актуальной концепции.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVED = {  # архивные разборы прежних версий правил — устаревшие формулировки там допустимы
    "tests/2026-10-25_topic_filter_tests.md",
    "tests/2026-10-25_v2_major_events_tests.md",
}

REQUIRED = [
    "CLAUDE.md", "README.md", "PROJECT_BOOTSTRAP_PROMPT.md",
    "knowledge/series_bible.md", "knowledge/topic_selection.md",
    "knowledge/vera_character_bible.md", "knowledge/visual_style.md",
    "knowledge/history_research_protocol.md", "knowledge/google_flow_guide.md",
    "knowledge/elevenlabs_guide.md", "knowledge/capcut_guide.md",
    "knowledge/subtitle_style.md", "knowledge/episode_template.md",
    "knowledge/continuity_template.md", "knowledge/sources.md",
    "episodes/README.md",
    "references/vera_face_reference.png", "references/vera_body_reference.png",
] + [f"episodes/episode_template/{n}" for n in (
    "00_brief.md", "01_research_and_factcheck.md", "02_vera_costume_reference_prompt.md",
    "03_script_and_voiceover.md", "04_flow_clips.md", "05_cover_prompt.md",
    "06_subtitles.md", "07_capcut_edit_plan.md", "08_publish_pack.md",
    "09_continuity.md", "10_final_qc.md")]

SKILLS = ["topic-scout", "episode-production", "historical-research",
          "flow-prompt-review", "continuity-check", "final-qc"]

# Устаревшие правила прежних версий, которых не должно остаться в действующих файлах
STALE = {
    r"не более 1 (из 5|серии из 5)": "старая квота курьёзов (v2)",
    r"собирательн\w+ вымышленн": "обязательный собирательный персонаж (v2)",
    r"без натурализма": "универсальное смягчение насилия (v2)",
    r"\bP[1-8]\b": "шкала P1–P8 (v2)",
    r"\bK(10|[1-9])\b": "шкала K1–K10 (v1)",
    r"анти-скук": "фильтр анти-скуки (v1–v2)",
    r"сюжетн\w+ лини": "термин «сюжетная линия» вместо «эпизод» (v2)",
    r"глазами (человека той эпохи|крестьянки|горожанина|ратника)": "подмена события очевидцем (v2)",
}

# Ключевые правила актуальной версии: (файл, регулярное выражение, что проверяем)
MUST = [
    ("knowledge/topic_selection.md", r"C4 < 7", "порог показываемого события"),
    ("knowledge/topic_selection.md", r"C5 < 6", "порог доказуемости"),
    ("knowledge/topic_selection.md", r"предположение", "запрет выдуманной популярности"),
    ("knowledge/topic_selection.md", r"непосредственно", "показ самого события"),
    ("knowledge/visual_style.md", r"## Насилие и драматичные сцены", "раздел о насилии"),
    ("knowledge/visual_style.md", r"не автоматическое решение", "размытие не по умолчанию"),
    ("knowledge/visual_style.md", r"лестниц", "запасная лестница постановки"),
    ("episodes/episode_template/04_flow_clips.md", r"EVENT", "тип клипа EVENT"),
    ("episodes/episode_template/10_final_qc.md", r"само событие", "QC: показ события"),
    ("CLAUDE.md", r"Показывать само событие", "правило в CLAUDE.md"),
    ("knowledge/vera_character_bible.md", r"\*\*Главный\*\* источник идентичности", "главные референсы"),
]

PATH_RE = re.compile(r"`((?:knowledge|episodes|references|tests|\.claude)/[^`*<>\s]+)`")
LINK_RE = re.compile(r"\]\((?!https?://|computer://|#|URL\))([^)\s]+)\)")


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        yield p, p.relative_to(ROOT).as_posix()


def main():
    errors, checked = [], 0

    for rel in REQUIRED:
        checked += 1
        if not (ROOT / rel).exists():
            errors.append(f"нет обязательного файла: {rel}")

    for name in SKILLS:
        checked += 1
        f = ROOT / ".claude/skills" / name / "SKILL.md"
        if not f.exists():
            errors.append(f"нет skill: {name}")
            continue
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{name}: нет корректного YAML-frontmatter")
            continue
        fm = m.group(1)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not re.search(rf"^name:\s*{re.escape(name)}\s*$", fm, re.M):
            errors.append(f"{name}: name не совпадает с папкой")
        if not desc or len(desc.group(1)) > 1536:
            errors.append(f"{name}: нет description или длиннее 1536 символов")
        if len(text.splitlines()) > 500:
            errors.append(f"{name}: SKILL.md длиннее 500 строк")

    for path, rel in md_files():
        text = path.read_text(encoding="utf-8")
        checked += 1
        if text.count("```") % 2:
            errors.append(f"{rel}: незакрытый блок кода ```")
        for ref in set(PATH_RE.findall(text)):
            if any(t in ref for t in ("EPNN", "EP*", "<")):
                continue
            if not (ROOT / ref.rstrip("/")).exists():
                errors.append(f"{rel}: ссылка на несуществующий путь `{ref}`")
        for link in set(LINK_RE.findall(text)):
            target = (path.parent / link).resolve()
            if not target.exists():
                errors.append(f"{rel}: битая локальная ссылка ({link})")
        if rel in ARCHIVED or rel == "PROJECT_BOOTSTRAP_PROMPT.md":
            continue
        for pat, why in STALE.items():
            for m in re.finditer(pat, text):
                line = text.count("\n", 0, m.start()) + 1
                errors.append(f"{rel}:{line}: устаревшее правило — {why}: «{m.group(0)}»")

    for rel, pat, why in MUST:
        checked += 1
        f = ROOT / rel
        if not f.exists() or not re.search(pat, f.read_text(encoding="utf-8")):
            errors.append(f"{rel}: нет ключевого правила — {why}")

    print(f"Проверок: {checked}. Ошибок: {len(errors)}.")
    for e in errors:
        print(" -", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
