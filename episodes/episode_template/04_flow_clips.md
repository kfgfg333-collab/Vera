# Клипы Google Flow

Стандарт: `knowledge/google_flow_guide.md` §3–4. Писать только после готового `02_vera_costume_reference_prompt.md`.
Модель по умолчанию: Veo 3.1 Fast · Ingredients · 9:16 · 8 с (ingredients у Veo — только 8 с; 10 с — только Omni Flash; Veo Quality — без ingredients).

**Главное правило:** в **каждом** клипе Вера видна от первого до последнего кадра, лицо читается; событие разворачивается за ней, сбоку или в глубине и не перекрыто ею. Клипов без Веры нет. Каждый промпт самодостаточен и прямо закрепляет присутствие Веры (блок [VERA]) — Flow не помнит соседние клипы.

**Речь:** если по сценарию Вера говорит — полная русская реплика в кавычках прямо в промпте ([SPEECH]: says aloud in Russian, lips and jaw move with each word, finishes before the end of the clip); один окончательный промпт на клип (`CLAUDE.md` → «Производственный процесс»).

**Как прикреплять референсы (≤ 3 ingredients):** персонаж `Vera EPNN` (если создан в Characters) **или** лицо (`vera_face_reference.png`) + костюмный кадр (`refs/costume.png`); + локация (`@loc_…`); при свободном слоте — участник/техника (`@ref_…`). Листы A/B не прикреплять. Реальных людей — без фото, по описанию эпохи. Метки `@…` заменить на имена, которые Flow показывает после ввода `@` (соответствие — `09_continuity.md`).

| № | Таймкод (расчёт) | Длит. | Модель/режим | Вера: режим · положение | Событие за ней | Фраза |
|---|---|---|---|---|---|---|
| 01 | 0:00–0:0_ | 8 с | Veo 3.1 Fast · Ingredients | TALK · передний план, центр | | |

Вера во всех клипах: __ из __ (должно быть 100%).

---
## Клип 01
1. **Номер и длительность / таймкод / модель:** 01 · 8 с (в монтаже 0:00–0:0_) · ___
2. **Фрагмент озвучки:** «…»
3. **Положение Веры в начале кадра:**
4. **Выражение лица, взгляд, действие (TALK/REACT; когда в камеру, когда на событие):**
5. **Что происходит на фоне и как меняется за клип:**
6. **Композиция и движение камеры:**
7. **Свет, атмосфера, детали эпохи:**
8. **Постоянство внешности Веры (что прикрепить):** персонаж `@Vera EPNN` **или** `@vera_face` + `@vera_EPNN_costume`; `@loc_…`; (`@ref_…`)
9. **Финал клипа и переход к следующему:**
10. **Основной промпт:**
```
[SCENE ROLE] …
[REFERENCES] Use @vera_face as the exact identity and @vera_EPNN_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_… as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. Position: … TALK/REACT: … Emotion: … Gaze: …
[EVENT BEHIND HER] … (develops during the clip; clearly visible behind her, not blocked by her)
[SETTING & ERA] … (period-accurate uniforms, weapons, vehicles, architecture)
[CAMERA] … one smooth movement, vertical 9:16 composition: Vera …, event …
[LIGHT & PALETTE] …
[START/END] Starts with … (Vera visible). Ends with … (Vera visible).
[AUDIO] …
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант** (полный самодостаточный промпт: проще действие, статичнее камера; для сцен насилия/катастроф — следующая ступень лестницы из `visual_style.md`, Вера остаётся в кадре):
```
(полный запасной промпт со всеми блоками, включая [VERA])
```
