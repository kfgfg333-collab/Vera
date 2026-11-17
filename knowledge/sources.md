# Источники по инструментам (дата обращения: 25.10.2026)

Исторические источники хранятся в файлах серий (`01_research_and_factcheck.md`).

## Google Flow / Veo / Omni
- [Learn about Flow models & supported features](https://support.google.com/flow/answer/16352836) — модели, длительности, ingredients/frames/extend, Omni
- [Create videos in Google Flow](https://support.google.com/flow/answer/16353334) — режимы Text/Frames/Ingredients, `@`, голосовые референсы, советы по промптам
- [Edit videos & build scenes](https://support.google.com/flow/answer/16935718) — Scenebuilder, Extend, Omni-правка
- [Get started with Google Flow](https://support.google.com/flow/answer/16353333) — SynthID, видимый водяной знак, аудио-возврат кредитов
- [Use the Google Flow Agent](https://support.google.com/flow/answer/17093911)
- [Create & use your avatar](https://support.google.com/flow/answer/17102997) — только своя внешность
- [Manage your Google Flow credits](https://support.google.com/flow/answer/16526234) — стоимость и лимиты
- [Where you can use Google Flow](https://support.google.com/flow/answer/16353544) — страны, 18+
- [Veo 3.1 Ingredients to Video (блог Google, 13.01.2026)](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/) — нативная 9:16, апскейл 1080p/4K
- [100 things we announced at I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) — Gemini Omni, SynthID
- [Manage your Google Flow projects, assets & collections](https://support.google.com/flow/answer/16935308) — Characters (1–2 изображения + голос), коллекции, переименование через Agent
- [Create & edit images in Google Flow](https://support.google.com/flow/answer/16729550) — Nano Banana Pro по умолчанию, «Image aspect ratio», ingredients, `@имя` персонажа
- [Справочный центр Flow (все статьи)](https://support.google.com/flow)

## ElevenLabs
- [Models](https://elevenlabs.io/docs/overview/models) — модели, языки, лимиты символов
- [Prompting / best practices](https://elevenlabs.io/docs/best-practices/prompting) — v4, аудиотеги, паузы, произношение, нормализация, скорость
- [Introducing Eleven v4 (блог)](https://elevenlabs.io/blog/create-realistic-transatlantic-accent-text-to-speech) — анонс 28.09.2026 (адрес страницы не совпадает с заголовком — так в источнике)
- [How do audio tags work with Eleven v3 and v4?](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-alpha) — аудиотеги, рекомендация v4
- [Eleven v4 (capabilities)](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4) — русский в списке; Stability + Similarity (+ Clone Strength для PVC); **Style и Speed недоступны**; SSML не поддерживается
- [What is Eleven v4? (Help Center)](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4) — то же по настройкам; UI и API (`eleven_v4`)
- [Text to Speech — product guide (веб-интерфейс)](https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech) — ползунки UI по моделям, лимит 10 000 симв. для v4, перегенерации, форматы скачивания (страница внутренне противоречит себе насчёт Speed)

## CapCut
- [How to add subtitles in CapCut (31.12.2025)](https://www.capcut.com/resource/how-to-add-subtitle-in-capcut) — автосубтитры Desktop/Mobile/Web
- [Why do the captions fail to export?](https://www.capcut.com/help/captions-fail-to-export) — экспорт SRT/TXT
- [How do I export 2K/4K videos in CapCut?](https://www.capcut.com/help/export-videos-in-capcut) — экспорт, fps, битрейт

## Claude Code
- [Skills — Claude Code docs](https://code.claude.com/docs/en/skills) — формат SKILL.md, `.claude/skills/<name>/`, frontmatter, `$ARGUMENTS`, лимит 500 строк

## Политики платформ (насилие, ИИ-контент)
- [YouTube — Violent or graphic content policies](https://support.google.com/youtube/answer/2802008?hl=en) — EDSA-контекст в изображении/звуке, драматизированное насилие, триггеры возрастного ограничения
- [YouTube — Age-restricted content](https://support.google.com/youtube/answer/2802167?hl=en) — последствия ограничения (18+, незалогиненные, реклама), апелляция
- [YouTube — Disclosing altered or synthetic content (блог, 18.03.2024)](https://blog.youtube/news-and-events/disclosing-ai-generated-content) — когда нужна пометка о реалистичном синтетическом контенте
- [Google Generative AI Prohibited Use Policy (обновл. 17.12.2024)](https://policies.google.com/terms/generative-ai/use-policy?hl=en-gb) — насилие и подстрекательство, выдача себя за реальных людей, исключения EDSA

## Безопасные зоны
Официальных пиксельных значений в проверенных источниках не найдено; в `subtitle_style.md` — консервативная рекомендация. Проверять шаблонами-наложениями площадок.

## Журнал перепроверок
| Дата | Что проверено | Изменения |
|---|---|---|
| 25.10.2026 | Первичная настройка: Flow, ElevenLabs, CapCut, Claude Code skills | — |
| 25.10.2026 | Политики YouTube и Google по насилию и ИИ-контенту (обновление v3) | Добавлен раздел «Насилие и драматичные сцены» в `visual_style.md` |
| 25.10.2026 | Аудит: ElevenLabs v4 (настройки UI vs API), Flow (модели, длительности, 9:16, Characters, регионы) | v4 без Speed/Style — паспорт голоса исправлен; лимит UI v4 = 10 000; добавлены Characters; расхождение справок по Extend; fps клипов не подтверждён |
