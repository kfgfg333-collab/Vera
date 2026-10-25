# Клипы Google Flow

Стандарт: `knowledge/google_flow_guide.md` §3–4. Писать только после готового `02_vera_costume_reference_prompt.md`.
Модель по умолчанию: Veo 3.1 Fast · Ingredients · 9:16 · 8 с (ingredients у Veo — только 8 с; 10 с — только Omni Flash; Veo Quality — без ingredients).

**Два типа клипов:**
- **EVENT** — само событие и его участники (Вера вне кадра или на втором плане). **Не менее половины клипов.**
- **VERA** — Вера рядом с событием: реакция, комментарий, проход.

**Как прикреплять референсы:**
- VERA-клип: режим Ingredients → персонаж `Vera EPNN` (если создан в Characters) **или** лицо (`vera_face_reference.png`) + костюмный кадр (`refs/costume.png`); + локация.
- EVENT-клип: локация и, если нужно, референс участника или техники (`@ref_…`), чтобы они совпадали между клипами. Реальных людей — без загрузки фото, по описанию внешности эпохи (`google_flow_guide.md`).
- Не более 3 ingredients. Листы A/B не прикреплять. Метки `@…` заменить на имена, которые Flow показывает после ввода `@`.
Рабочие метки: `@vera_face`, `@vera_EPNN_costume`, `@loc_…`, `@ref_…` (соответствие — в `09_continuity.md`).

| № | Тип | Таймкод | Длит. | Модель/режим | Фраза | План |
|---|---|---|---|---|---|---|
| 01 | EVENT / VERA | 0:00–0:0_ | 8 с | Veo 3.1 Fast · Ingredients | | |

Итого EVENT: __ из __ (≥ 50%).

---
## Клип 01 (тип: VERA)
1. **Номер / тип / длительность / таймкод:** 01 · VERA · 8 с (в монтаже 0:00–0:0_) · модель/режим: ___
2. **Цель и эмоция:**
3. **Фраза озвучки:** «…»
4. **Референсы (что прикрепить):** REF_CHARACTER_FACE (`@vera_face`), REF_EPISODE_COSTUME (`@vera_EPNN_costume`) — или персонаж `@Vera EPNN`; REF_LOCATION (`@loc_…`); REF_PREVIOUS_SHOT — только в режиме Frames
5. **Промпт:**
```
[SCENE ROLE] …
[REFERENCES] Use @vera_face as the exact identity and @vera_EPNN_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical.
[SUBJECT & ACTION] …
[SETTING & ERA] …
[BACKGROUND] … (the historical event visible behind her)
[CAMERA] … vertical 9:16 composition …
[LIGHT & PALETTE] …
[START/END] Starts with … Ends with …
[AUDIO] She does not speak; no dialogue; natural ambient sound: …
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```
6. **Камера:**
7. **Действие Веры / что происходит в событии / фон:**
8. **Исторические детали (форма, оружие, техника, архитектура), свет, атмосфера:**
9. **Начало / конец для склейки:**
10. **Риски и запасной вариант** (полный самодостаточный промпт: меньше действия, статичнее камера):
```
(полный упрощённый промпт со всеми блоками)
```

---
## Клип 02 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 02 · EVENT · 8 с · модель/режим: ___
2. **Цель и эмоция:**
3. **Фраза озвучки:** «…»
4. **Референсы (что прикрепить):** REF_LOCATION (`@loc_…`); участник/техника (`@ref_…`, если нужно); Вера — только если она на втором плане
5. **Промпт:**
```
[SCENE ROLE] …
[REFERENCES] Use @loc_… as the setting [and @ref_… as the exact look of …].
[EVENT ACTION] …
[SETTING & ERA] … (period-accurate uniforms, weapons, vehicles, architecture)
[CAMERA] … vertical 9:16 composition …
[LIGHT & PALETTE] …
[START/END] Starts with … Ends with …
[AUDIO] No dialogue; natural sound: …
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:**
7. **Действие участников события / фон:**
8. **Исторические детали, свет, атмосфера:**
9. **Начало / конец для склейки:**
10. **Риски и запасной вариант** (полный промпт; для сцен насилия — следующая ступень лестницы из `visual_style.md`: широкий план → момент удара → реакция → последствия):
```
(полный запасной промпт)
```
