# Клипы Google Flow — EP01

Стандарт: `knowledge/google_flow_guide.md` §3–4. Файл 02 готов (`02_vera_costume_reference_prompt.md`).
Модель по умолчанию: Veo 3.1 Fast · Ingredients · 9:16 · 8 с (ingredients у Veo — только 8 с). Клипы 01, 02, 12 — Gemini Omni Flash 1.1, 10 с (длинные фразы; 01 — режим Text, без ingredients).

**Как прикреплять референсы:** VERA — персонаж `Vera EP01` (если создан в Characters) **или** `@vera_face` + `@vera_EP01_costume`; + `@loc_pripyat_street`. EVENT — `@loc_unit4_night` / `@loc_pripyat_street` и `@ref_firefighter`. Не более 3 ingredients. Листы A/B не прикреплять. Метки `@…` заменить на имена, которые Flow показывает после `@` (соответствие — `09_continuity.md`). Реальные люди (операторы, Правик) — без фото, безымянные образы эпохи.

| № | Тип | Таймкод | Длит. | Модель/режим | Фраза | План |
|---|---|---|---|---|---|---|
| 01 | EVENT | 0:00–0:08 | 10 с | Gemini Omni Flash 1.1 · Text · 10 с (запасной: Veo 3.1 Fast · Text · 8 с) | Час ночи, двадцать три минуты сорок секунд. Инженер нажимает… | Деталь → средний |
| 02 | EVENT | 0:08–0:19 | 10 с | Gemini Omni Flash 1.1 · Ingredients · 10 с (фраза ≈ 9–10 с) | Чернобыльская атомная станция, Украинская ССР, двадцать шест… | Общий (establishing) |
| 03 | VERA | 0:19–0:28 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Я в Припяти, в нескольких километрах от станции. Город спит.… | Через плечо → на горизонт |
| 04 | EVENT | 0:28–0:31 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Два взрыва, один за другим.… | Общий |
| 05 | EVENT | 0:31–0:36 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Реактор разрушен, раскалённые обломки и графит падают на кры… | Средний |
| 06 | EVENT | 0:36–0:39 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Первыми на крыши поднимаются пожарные.… | Средний, вслед |
| 07 | EVENT | 0:39–0:47 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Караул лейтенанта Владимира Правика тушит огонь рядом с трет… | Общий, силуэты |
| 08 | EVENT | 0:47–0:51 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | За несколько часов огонь на крышах сбит.… | Средний |
| 09 | VERA | 0:51–0:59 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | А утром в Припяти обычная суббота. Люди гуляют, а я смотрю н… | Средний → реакция |
| 10 | EVENT | 0:59–1:07 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Эвакуацию объявят только на следующий день. Около пятидесяти… | Общий |
| 11 | EVENT | 1:07–1:15 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | Двадцать восемь человек умрут от лучевой болезни за три меся… | Общий |
| 12 | VERA | 1:15–1:24 | 10 с | Gemini Omni Flash 1.1 · Ingredients · 10 с (фраза ≈ 11 с: последний титр на финальной выдержке/затемнении) | Причиной потом назвали и дефекты конструкции реактора, и нар… | Общий, Вера мала в кадре |

Итого EVENT: 9 из 12 (≥ 50%). VERA: 3. Селфи: 0. Сумма клипов: 102 с ≥ озвучка (расчёт ≈ 80 с) + запас; таймкоды — расчётные (140 сл/мин), сверить по реальной озвучке.

---
## Клип 01 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 01 · EVENT · 10 с (в монтаже 0:00–0:08) · модель/режим: Gemini Omni Flash 1.1 · Text · 10 с (запасной: Veo 3.1 Fast · Text · 8 с)
2. **Цель и эмоция:** Крючок: зритель сразу у пульта; тревога, тишина перед бедой.
3. **Фраза озвучки:** «Час ночи, двадцать три минуты сорок секунд. Инженер нажимает кнопку, которая должна заглушить реактор. Через несколько секунд реактор взрывается.»
4. **Референсы (что прикрепить):** Без ingredients (режим Text) **или** Ingredients без Веры: только при наличии референса пульта. Рекомендуется: Omni Flash · **Text** · 10 с (фраза ≈ 8–9 с). Поддержка режима Text у Omni в справке явно не расписана — **проверить в интерфейсе**; если нет — Veo 3.1 Fast · Text · 8 с (фразу в монтаже довести на начале клипа 02).
5. **Промпт:**
```
[SCENE ROLE] Hook: a reactor operator presses the emergency shutdown button in the control room at night.
[REFERENCES] No reference images; no Vera in this shot.
[EVENT ACTION] A young male operator in a white lab coat and white cap firmly presses a single large square push-button on a long control desk; two colleagues in white coats turn toward him, tense.
[SETTING & ERA] Soviet nuclear power plant control room, night of 26 April 1986, about 1:23 a.m., no windows, 1980s grey-green control desks with rows of switches, round gauges, indicator lamps and a large circular panel of small lamps on the wall.
[CAMERA] Extreme close-up of the finger over the button, slow pull-back to a medium shot; vertical 9:16 composition.
[LIGHT & PALETTE] Cold fluorescent ceiling light, pale green-grey palette, small red and amber indicator lamps glowing.
[START/END] Starts with the finger above the button. Ends with the operators frozen, looking at the gauges, a faint vibration in the room.
[AUDIO] No dialogue; natural sound: electrical hum, relay clicks, a low rumble at the very end
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** ECU → медленный отъезд (одно движение)
7. **Действие участников события / фон:** Оператор нажимает кнопку; двое коллег оборачиваются. Лиц исторических людей не воспроизводим — безымянные операторы.
8. **Исторические детали, свет, атмосфера:** Белые халаты и шапочки (🎭, проверить по фото); серо-зелёные пульты, круглая мнемосхема; надписей нет.
9. **Начало / конец для склейки:** Конец: замершие операторы, гул → склейка на общий план станции (02).
10. **Риски и запасной вариант:** Генератор может нарисовать надписи на кнопке — в AVOID «no text»; при надписях использовать запасной (статичный ECU).
```
[SCENE ROLE] Hook: a finger presses an emergency shutdown button on a control desk.
[REFERENCES] No reference images.
[EVENT ACTION] A hand in a white lab coat sleeve presses one large square push-button on a control desk.
[SETTING & ERA] Soviet nuclear power plant control room, night of 26 April 1986, 1980s grey-green control desk with switches and round gauges.
[CAMERA] Static extreme close-up of the hand and the button, vertical 9:16 composition.
[LIGHT & PALETTE] Cold fluorescent light, small red indicator lamps.
[START/END] Starts with the hand approaching. Ends with the button pressed and lamps flickering.
[AUDIO] No dialogue; natural sound: electrical hum, one sharp click
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 02 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 02 · EVENT · 10 с (в монтаже 0:08–0:19) · модель/режим: Gemini Omni Flash 1.1 · Ingredients · 10 с (фраза ≈ 9–10 с)
2. **Цель и эмоция:** Контекст: масштаб станции, спокойная ночь за секунды до взрыва.
3. **Фраза озвучки:** «Чернобыльская атомная станция, Украинская ССР, двадцать шестое апреля тысяча девятьсот восемьдесят шестого. Четвёртый блок собирались остановить на ремонт — а перед этим провести испытание.»
4. **Референсы (что прикрепить):** REF_LOCATION `@loc_unit4_night`.
5. **Промпт:**
```
[SCENE ROLE] Context: establishing shot of the Chernobyl nuclear power plant, calm, seconds before the accident.
[REFERENCES] Use @loc_unit4_night as the exact look of the plant buildings and the striped ventilation stack.
[EVENT ACTION] The plant stands quiet; a thin plume of white steam drifts from a vent, a few windows glow, nothing dramatic happens yet.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, Night of 26 April 1986, about 1:23 a.m., clear calm spring night, long concrete reactor building of unit 4 beside a tall red-and-white striped ventilation stack, long turbine hall in front, sodium street lamps, power lines, flat wooded landscape.
[CAMERA] Wide establishing shot, slow push-in toward the unit 4 building, vertical 9:16 composition with the striped stack in the upper half.
[LIGHT & PALETTE] Dark-blue night sky, warm orange sodium lamps, cold white window light.
[START/END] Starts wide and still. Ends closer on the unit 4 building, still calm.
[AUDIO] No dialogue; natural sound: night crickets, distant transformer hum
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** Общий, медленный наезд
7. **Действие участников события / фон:** Станция спокойна — это ещё до взрыва.
8. **Исторические детали, свет, атмосфера:** Полосатая вентиляционная труба, корпус 4-го блока, машзал (🎭 по фото).
9. **Начало / конец для склейки:** Конец: ближе к 4-му блоку → склейка на Веру в Припяти (03).
10. **Риски и запасной вариант:** Если Omni недоступен — Veo 3.1 Fast 8 с и замедление до ~85% в CapCut; при неудаче — запасной статичный.
```
[SCENE ROLE] Context: still establishing shot of a Soviet nuclear power plant at night.
[REFERENCES] Use @loc_unit4_night as the setting.
[EVENT ACTION] The plant stands quiet at night; light steam drifts from a vent.
[SETTING & ERA] Chernobyl nuclear power plant, night of 26 April 1986, clear spring night, concrete reactor building, red-and-white striped ventilation stack.
[CAMERA] Static wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Dark-blue sky, orange sodium lamps.
[START/END] Starts and ends on the same calm view.
[AUDIO] No dialogue; natural sound: crickets, faint hum
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 03 (тип: VERA)
1. **Номер / тип / длительность / таймкод:** 03 · VERA · 8 с (в монтаже 0:19–0:28) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Проводник: Вера ночью на улице спящего города; тревога, бессилие.
3. **Фраза озвучки:** «Я в Припяти, в нескольких километрах от станции. Город спит. Я знаю, что сейчас будет, — и ничего не могу изменить.»
4. **Референсы (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или персонаж `@Vera EP01`); `@loc_pripyat_street`.
5. **Промпт:**
```
[SCENE ROLE] Vera stands alone on a sleeping city street at night and looks toward the distant power plant.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting, at night.
[SUBJECT & ACTION] Vera, a woman in her mid-twenties, stands still on an empty pavement, hands in her coat pockets, looking at the horizon, anxious and helpless. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel.
[SETTING & ERA] Pripyat, Ukrainian SSR, night of 26 April 1986, clear calm night, white panel apartment blocks with dark windows, young poplars, street lamps.
[BACKGROUND] Far beyond the rooftops, the small lights of the power plant and its striped stack; all calm.
[CAMERA] Over-the-shoulder medium shot, slow push-in, vertical 9:16 composition, the distant plant in the upper third, in focus.
[LIGHT & PALETTE] Cool blue night, warm street-lamp pools, her wine-red scarf the only saturated colour.
[START/END] Starts behind her shoulder. Ends with the distant plant lights still calm.
[AUDIO] She does not speak; no dialogue; natural ambient sound: quiet night, a dog barking far away, a light breeze in the poplars
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```
6. **Камера:** Через плечо, медленный наезд
7. **Действие Веры / что происходит в событии / фон:** Вера стоит, смотрит на огни станции вдали; рот не в кадре.
8. **Исторические детали, свет, атмосфера:** Панельные дома, тополя; огни станции далеко.
9. **Начало / конец для склейки:** Конец: спокойные огни на горизонте → склейка на вспышку (04) с того же ракурса.
10. **Риски и запасной вариант:** Лицо мало в кадре — сходство не критично. Если «уплывает» костюм — добавить портрет `costume_portrait.png`.
```
[SCENE ROLE] Vera on a night street looks at the distant power plant.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting, at night.
[SUBJECT & ACTION] Vera, a woman in her mid-twenties, stands on a pavement, seen from behind, looking at the horizon. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel.
[SETTING & ERA] Pripyat, night of 26 April 1986, clear spring night, white apartment blocks.
[BACKGROUND] Distant lights of the power plant on the horizon.
[CAMERA] Static over-the-shoulder medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Blue night, street-lamp light.
[START/END] Starts and ends on the same calm view.
[AUDIO] She does not speak; no dialogue; natural ambient sound: quiet night
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```

---
## Клип 04 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 04 · EVENT · 8 с (в монтаже 0:28–0:31) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Кульминационный удар: два взрыва над 4-м блоком.
3. **Фраза озвучки:** «Два взрыва, один за другим.»
4. **Референсы (что прикрепить):** `@loc_unit4_night`.
5. **Промпт:**
```
[SCENE ROLE] Climax beat: two explosions in quick succession tear through the unit 4 reactor building.
[REFERENCES] Use @loc_unit4_night as the exact look of the plant buildings and the striped ventilation stack.
[EVENT ACTION] A first bright burst of steam and debris erupts from the top of the unit 4 reactor building; two seconds later a second, larger blast throws glowing fragments high into the night sky; a column of smoke rises beside the striped stack.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, night of 26 April 1986, about 1:24 a.m., clear calm spring night, concrete reactor building, turbine hall, sodium lamps.
[CAMERA] Wide shot from a distance, static camera with a light shake on each blast, vertical 9:16 composition, the blast in the upper half.
[LIGHT & PALETTE] Night blue broken by orange-white flashes and a red glow.
[START/END] Starts with the calm plant. Ends with glowing fragments falling and smoke rising.
[AUDIO] No dialogue; natural sound: two deep booms two seconds apart, a rumbling echo
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups. No mushroom cloud.
```
6. **Камера:** Общий, статично, тряска на ударах
7. **Действие участников события / фон:** Два взрыва, обломки летят вверх.
8. **Исторические детали, свет, атмосфера:** Без «ядерного гриба» (👁 — неверный образ).
9. **Начало / конец для склейки:** Конец: обломки падают → склейка на крышу машзала (05).
10. **Риски и запасной вариант:** Возможен блок на «nuclear explosion» — в промпте этих слов нет; запасной — «industrial steam explosion». «No mushroom cloud» уже в AVOID.
```
[SCENE ROLE] Climax beat: an industrial steam explosion at a power plant at night.
[REFERENCES] Use @loc_unit4_night as the setting.
[EVENT ACTION] A bright burst of steam, smoke and glowing debris erupts from the roof of a large concrete industrial building; smoke rises.
[SETTING & ERA] Soviet power plant, night of 26 April 1986, clear spring night, striped ventilation stack.
[CAMERA] Static wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Night blue with an orange glow.
[START/END] Starts calm. Ends with smoke and falling sparks.
[AUDIO] No dialogue; natural sound: a deep boom, rumble
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 05 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 05 · EVENT · 8 с (в монтаже 0:31–0:36) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Масштаб разрушения: огонь на крышах.
3. **Фраза озвучки:** «Реактор разрушен, раскалённые обломки и графит падают на крыши соседних зданий.»
4. **Референсы (что прикрепить):** `@loc_unit4_night`.
5. **Промпт:**
```
[SCENE ROLE] Development: glowing debris and graphite blocks land on the turbine hall roof and start fires.
[REFERENCES] Use @loc_unit4_night as the exact look of the plant buildings.
[EVENT ACTION] Glowing black graphite blocks and burning fragments fall onto the flat bitumen roof of the long turbine hall and set small fires that spread across the roof; smoke drifts toward the striped ventilation stack.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, night of 26 April 1986, shortly after 1:24 a.m., clear calm night, wrecked upper part of the unit 4 building in the background.
[CAMERA] Medium-wide shot from roof level, slow pan from right to left along the burning roof, vertical 9:16 composition.
[LIGHT & PALETTE] Orange firelight against a dark-blue sky, grey smoke.
[START/END] Starts with fragments falling into frame. Ends with several fires burning along the roof.
[AUDIO] No dialogue; natural sound: crackling fire, hissing, debris thudding onto the roof
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups. No mushroom cloud.
```
6. **Камера:** Средне-общий, медленная панорама
7. **Действие участников события / фон:** Обломки и графит падают, крыша загорается.
8. **Исторические детали, свет, атмосфера:** Плоская битумная кровля машзала (🎭).
9. **Начало / конец для склейки:** Конец: огни на крыше → склейка на прибытие пожарных (06).
10. **Риски и запасной вариант:** Мелкие обломки могут «кипеть» — запасной статичный.
```
[SCENE ROLE] Development: small fires burn on a flat industrial roof at night.
[REFERENCES] Use @loc_unit4_night as the setting.
[EVENT ACTION] Several small fires burn on a flat industrial roof; smoke drifts.
[SETTING & ERA] Soviet power plant, night of 26 April 1986, clear night.
[CAMERA] Static medium-wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Orange firelight, dark sky.
[START/END] Starts and ends with fires burning.
[AUDIO] No dialogue; natural sound: crackling fire
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 06 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 06 · EVENT · 8 с (в монтаже 0:36–0:39) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Появление героев события.
3. **Фраза озвучки:** «Первыми на крыши поднимаются пожарные.»
4. **Референсы (что прикрепить):** `@loc_unit4_night` + `@ref_firefighter`.
5. **Промпт:**
```
[SCENE ROLE] Climax build-up: firefighters arrive and run toward the burning building.
[REFERENCES] Use @loc_unit4_night as the setting and @ref_firefighter as the exact look of the firefighters' uniforms.
[EVENT ACTION] Two red Soviet fire engines stop near the turbine hall; firefighters in dark canvas turnout coats and helmets jump out, pull hoses and run toward a vertical steel ladder on the wall of the building.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, night of 26 April 1986, about 1:30 a.m., clear night, fire glowing on the roof above, 1970s bonneted red Soviet fire trucks with a white stripe and blue flashing lights.
[CAMERA] Medium tracking shot following behind the firefighters as they run toward the ladder, vertical 9:16 composition.
[LIGHT & PALETTE] Blue flashing lights mixed with orange firelight from above, dark night.
[START/END] Starts with the trucks braking. Ends with the first firefighter grabbing the ladder.
[AUDIO] No dialogue; natural sound: engines idling, boots on concrete, hoses unrolling, fire crackling above
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** Средний, вслед (одно направление)
7. **Действие участников события / фон:** Машины, пожарные, рукава, лестница.
8. **Исторические детали, свет, атмосфера:** ЗИЛ-130 (🎭, проверить по фото); брезент, каски, без респираторов.
9. **Начало / конец для склейки:** Конец: рука на лестнице → склейка на крышу (07).
10. **Риски и запасной вариант:** Надписи на машинах — «no text»; если искажены — запасной без машин.
```
[SCENE ROLE] Firefighters run toward a burning industrial building at night.
[REFERENCES] Use @ref_firefighter as the exact look of the firefighters.
[EVENT ACTION] Three firefighters in dark canvas coats and helmets run toward a building with fire on the roof.
[SETTING & ERA] Soviet power plant, night of 26 April 1986, clear night.
[CAMERA] Static medium-wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Blue flashing light, orange glow.
[START/END] Starts with them running in. Ends at the wall of the building.
[AUDIO] No dialogue; natural sound: running boots, fire
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 07 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 07 · EVENT · 8 с (в монтаже 0:39–0:47) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Кульминация: пожарные на крыше у зарева — главный визуальный момент.
3. **Фраза озвучки:** «Караул лейтенанта Владимира Правика тушит огонь рядом с третьим блоком — тот ещё работает, и пламя нельзя пустить дальше.»
4. **Референсы (что прикрепить):** `@loc_unit4_night` + `@ref_firefighter`.
5. **Промпт:**
```
[SCENE ROLE] Climax: firefighters on the roof fight the fire next to the still-working neighbouring unit.
[REFERENCES] Use @loc_unit4_night as the setting and @ref_firefighter as the exact look of the firefighters.
[EVENT ACTION] Four firefighters stand on a high flat roof and direct two canvas hoses at burning debris; a young officer at the front points toward the fire; behind them the wrecked unit 4 glows red and smoke rises past the red-and-white striped ventilation stack.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, night of 26 April 1986, around 2 a.m., clear night, roofs of the plant buildings, firefighters in dark canvas turnout coats and helmets without respirators.
[CAMERA] Wide shot from a low angle, slow push-in, vertical 9:16 composition, the striped stack and glow in the upper half, silhouettes in the lower half.
[LIGHT & PALETTE] Red-orange glow from the wreck, white jets of water catching the light, dark-blue sky.
[START/END] Starts with the hoses opening. Ends with the firefighters advancing into the smoke.
[AUDIO] No dialogue; natural sound: roaring fire, rushing water jets, hiss of steam
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** Общий, нижний ракурс, медленный наезд
7. **Действие участников события / фон:** Пожарные со шлангами; офицер впереди — образ, не портрет Правика.
8. **Исторические детали, свет, атмосфера:** Полосатая труба, зарево, брезент.
9. **Начало / конец для склейки:** Конец: шаг в дым → склейка на рассвет (08).
10. **Риски и запасной вариант:** Портретное сходство с Правиком не добиваемся (🎭, без фото). Много людей — максимум 4.
```
[SCENE ROLE] Climax: silhouettes of firefighters with hoses on a roof against a red glow.
[REFERENCES] Use @ref_firefighter as the exact look of the firefighters.
[EVENT ACTION] Three firefighters in silhouette spray water from a hose at a fire on a flat roof.
[SETTING & ERA] Soviet power plant roof, night of 26 April 1986, clear night, red-and-white striped ventilation stack behind.
[CAMERA] Static wide shot from a low angle, vertical 9:16 composition.
[LIGHT & PALETTE] Red-orange glow, dark sky.
[START/END] Starts and ends with the hose spraying.
[AUDIO] No dialogue; natural sound: fire, water jet
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 08 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 08 · EVENT · 8 с (в монтаже 0:47–0:51) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Итог ночи: огонь сбит, люди измотаны.
3. **Фраза озвучки:** «За несколько часов огонь на крышах сбит.»
4. **Референсы (что прикрепить):** `@loc_unit4_night` + `@ref_firefighter`.
5. **Промпт:**
```
[SCENE ROLE] Resolution of the night: at dawn the roof fires are out and exhausted firefighters climb down.
[REFERENCES] Use @loc_unit4_night as the setting, now at dawn, and @ref_firefighter as the exact look of the firefighters.
[EVENT ACTION] Two exhausted firefighters in soot-stained canvas coats slowly climb down a steel ladder; a white ambulance waits on the ground; thin grey smoke still rises from the wrecked unit 4 behind them.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, early morning of 26 April 1986, first light, calm weather, the fires on the roofs extinguished, wet concrete and puddles from the hoses.
[CAMERA] Medium shot, static camera, vertical 9:16 composition.
[LIGHT & PALETTE] Cold grey-blue dawn light, a pale pink horizon, no flames.
[START/END] Starts with boots on the ladder. Ends with the firefighters reaching the ground near the ambulance.
[AUDIO] No dialogue; natural sound: dripping water, distant engine idling, birds starting to sing
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** Средний, статично
7. **Действие участников события / фон:** Пожарные спускаются; скорая. Лучевых поражений не показываем.
8. **Исторические детали, свет, атмосфера:** Скорая — белый «РАФ» (🎭); мокрый бетон.
9. **Начало / конец для склейки:** Конец: земля, скорая → склейка на утро в Припяти (09).
10. **Риски и запасной вариант:** Без крупных планов лиц и следов болезни.
```
[SCENE ROLE] Dawn after the fire: smoke over a damaged industrial building.
[REFERENCES] Use @loc_unit4_night as the setting, now at dawn.
[EVENT ACTION] Thin grey smoke rises from a damaged concrete building at dawn; no flames.
[SETTING & ERA] Soviet power plant, early morning of 26 April 1986, calm weather.
[CAMERA] Static wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Cold dawn light.
[START/END] Starts and ends with smoke rising.
[AUDIO] No dialogue; natural sound: birds, dripping water
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 09 (тип: VERA)
1. **Номер / тип / длительность / таймкод:** 09 · VERA · 8 с (в монтаже 0:51–0:59) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Контраст: обычная жизнь и дым на горизонте; Вера знает.
3. **Фраза озвучки:** «А утром в Припяти обычная суббота. Люди гуляют, а я смотрю на дым над станцией. Городу ничего не объявили.»
4. **Референсы (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`); `@loc_pripyat_street`.
5. **Промпт:**
```
[SCENE ROLE] Contrast: an ordinary Saturday morning in the city while Vera looks at the smoke over the plant.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting, in the morning.
[SUBJECT & ACTION] Vera, a woman in her mid-twenties, stands by a bus stop and slowly turns her head from the passers-by to the horizon, worried. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel.
[SETTING & ERA] Pripyat, Ukrainian SSR, Saturday morning, 26 April 1986, sunny and warm, white panel apartment blocks, young poplars.
[BACKGROUND] A few passers-by walk calmly (a woman with a shopping bag, a father with a pram); far on the horizon a thin grey smoke plume rises over the power plant.
[CAMERA] Static medium shot, vertical 9:16 composition, Vera lower left, the smoke plume upper right.
[LIGHT & PALETTE] Soft warm morning sun, pale blue sky, her wine-red scarf as the accent.
[START/END] Starts with her watching the passers-by. Ends with her looking at the smoke plume.
[AUDIO] She does not speak; no dialogue; natural ambient sound: birds, footsteps, distant voices without words
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```
6. **Камера:** Средний, статично
7. **Действие Веры / что происходит в событии / фон:** Вера переводит взгляд с прохожих на дым.
8. **Исторические детали, свет, атмосфера:** Одежда прохожих — середина 80-х; без надписей.
9. **Начало / конец для склейки:** Конец: взгляд на дым → склейка на автобусы (10).
10. **Риски и запасной вариант:** Толпа может исказить руки — прохожих не больше 4–5, на среднем плане.
```
[SCENE ROLE] Vera on a sunny morning street looks toward a distant smoke plume.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting, in the morning.
[SUBJECT & ACTION] Vera, a woman in her mid-twenties, stands still and looks toward the horizon, worried. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel.
[SETTING & ERA] Pripyat, morning of 26 April 1986, sunny, white apartment blocks.
[BACKGROUND] A thin smoke plume far on the horizon.
[CAMERA] Static medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Warm morning sun.
[START/END] Starts and ends with her looking at the horizon.
[AUDIO] She does not speak; no dialogue; natural ambient sound: birds
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```

---
## Клип 10 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 10 · EVENT · 8 с (в монтаже 0:59–1:07) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Последствия: эвакуация города.
3. **Фраза озвучки:** «Эвакуацию объявят только на следующий день. Около пятидесяти тысяч человек сядут в автобусы. Им скажут — временно.»
4. **Референсы (что прикрепить):** `@loc_pripyat_street`.
5. **Промпт:**
```
[SCENE ROLE] Consequence: residents of the city board a long column of buses during the evacuation.
[REFERENCES] Use @loc_pripyat_street as the setting, in the afternoon.
[EVENT ACTION] A long column of yellow and cream Soviet city buses stands along the street; residents with small bags and suitcases quietly board them, a mother leads a child by the hand, a policeman in a grey 1980s Soviet militia uniform stands by the door.
[SETTING & ERA] Pripyat, Ukrainian SSR, afternoon of 27 April 1986, sunny and warm, white panel apartment blocks, young poplars, 1980s LAZ and Ikarus style buses.
[CAMERA] Wide shot along the column, slow dolly sideways from left to right, vertical 9:16 composition.
[LIGHT & PALETTE] Bright spring daylight, soft shadows, muted pastel colours.
[START/END] Starts with people walking to the buses. Ends with the first bus starting to move.
[AUDIO] No dialogue; natural sound: bus engines, footsteps, quiet murmur without words
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** Общий, боковой dolly
7. **Действие участников события / фон:** Посадка в автобусы, милиционер у двери.
8. **Исторические детали, свет, атмосфера:** ЛАЗ/Ikarus (🎭); форма милиции 80-х; без номеров и надписей.
9. **Начало / конец для склейки:** Конец: автобус трогается → склейка на станцию днём (11).
10. **Риски и запасной вариант:** Номерные знаки и надписи — «no text».
```
[SCENE ROLE] Consequence: a column of buses on a city street during an evacuation.
[REFERENCES] Use @loc_pripyat_street as the setting.
[EVENT ACTION] A long column of Soviet buses stands along a street of apartment blocks; a few people walk to the doors.
[SETTING & ERA] Pripyat, afternoon of 27 April 1986, sunny.
[CAMERA] Static wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Bright daylight.
[START/END] Starts and ends with the column standing.
[AUDIO] No dialogue; natural sound: bus engines
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 11 (тип: EVENT)
1. **Номер / тип / длительность / таймкод:** 11 · EVENT · 8 с (в монтаже 1:07–1:15) · модель/режим: Veo 3.1 Fast · Ingredients · 8 с
2. **Цель и эмоция:** Цена: разрушенный блок днём; тишина.
3. **Фраза озвучки:** «Двадцать восемь человек умрут от лучевой болезни за три месяца. Шестеро из них — пожарные. Правик — одиннадцатого мая.»
4. **Референсы (что прикрепить):** `@loc_unit4_night` (днём) + `@ref_firefighter` (каски).
5. **Промпт:**
```
[SCENE ROLE] Aftermath: the wrecked unit 4 in daylight, with firefighters' helmets left on a bench in the foreground.
[REFERENCES] Use @loc_unit4_night as the exact look of the plant buildings, now in daylight, and @ref_firefighter as the exact look of the helmets.
[EVENT ACTION] Thin smoke rises from the open, wrecked top of the unit 4 building beside the red-and-white striped ventilation stack; in the foreground several dark fire helmets lie on a wooden bench, untouched.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, late April 1986, overcast day, calm air, no people.
[CAMERA] Wide shot, very slow push-in toward the wrecked building over the helmets, vertical 9:16 composition, helmets in the lower third.
[LIGHT & PALETTE] Flat grey overcast daylight, desaturated palette.
[START/END] Starts on the helmets in the foreground. Ends with the wrecked building filling the upper half.
[AUDIO] No dialogue; natural sound: wind, a distant helicopter, silence
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```
6. **Камера:** Общий, очень медленный наезд
7. **Действие участников события / фон:** Пустые каски на скамье — символ, не утверждение о факте (👁: в 08 не подавать как документ).
8. **Исторические детали, свет, атмосфера:** Вертолёт — звук (по NRC, тушение с вертолётов в следующие дни).
9. **Начало / конец для склейки:** Конец: развал блока → склейка на пустой город (12).
10. **Риски и запасной вариант:** Каски на скамье — 🎭 символ; если генератор добавляет людей — запасной без касок.
```
[SCENE ROLE] Aftermath: a damaged concrete industrial building under an overcast sky.
[REFERENCES] Use @loc_unit4_night as the setting, in daylight.
[EVENT ACTION] Thin smoke rises from the damaged top of a large concrete building beside a red-and-white striped stack.
[SETTING & ERA] Soviet power plant, late April 1986, overcast day, no people.
[CAMERA] Static wide shot, vertical 9:16 composition.
[LIGHT & PALETTE] Grey overcast light.
[START/END] Starts and ends with smoke rising.
[AUDIO] No dialogue; natural sound: wind
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no modern objects, no anachronisms, no gratuitous gore close-ups.
```

---
## Клип 12 (тип: VERA)
1. **Номер / тип / длительность / таймкод:** 12 · VERA · 10 с (в монтаже 1:15–1:24) · модель/режим: Gemini Omni Flash 1.1 · Ingredients · 10 с (фраза ≈ 11 с: последний титр на финальной выдержке/затемнении)
2. **Цель и эмоция:** Финал: пустота; тихая скорбь.
3. **Фраза озвучки:** «Причиной потом назвали и дефекты конструкции реактора, и нарушения при испытании. Город, которому было шестнадцать лет, стоит пустым до сих пор.»
4. **Референсы (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`); `@loc_pripyat_street`.
5. **Промпт:**
```
[SCENE ROLE] Final shot: Vera alone on the empty, abandoned street of the city.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting, now abandoned.
[SUBJECT & ACTION] Vera, a woman in her mid-twenties, walks slowly away from the camera down the empty street and stops to look up at the dark windows, quiet and sad. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel.
[SETTING & ERA] Pripyat, Ukrainian SSR, after the evacuation of 27 April 1986, overcast evening, intact white panel apartment blocks with dark windows, an empty bus stop, poplars, no other people.
[BACKGROUND] Empty pavements, a few fallen leaves moved by the wind, no movement in the windows.
[CAMERA] Static wide shot from behind, vertical 9:16 composition, Vera small in the lower third.
[LIGHT & PALETTE] Cold grey-blue evening light, her wine-red scarf the only warm colour.
[START/END] Starts with her walking into frame. Ends with her standing still, small, in the empty street.
[AUDIO] She does not speak; no dialogue; natural ambient sound: wind, rustling leaves, silence
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```
6. **Камера:** Общий со спины, статично
7. **Действие Веры / что происходит в событии / фон:** Вера уходит и останавливается.
8. **Исторические детали, свет, атмосфера:** Город пуст; без граффити и примет современности (👁: это 1986, не руины 2000-х).
9. **Начало / конец для склейки:** Конец: финальный кадр → затемнение.
10. **Риски и запасной вариант:** Генератор может добавить «руины зоны» (разбитые окна, деревья сквозь асфальт) — это анахронизм для 1986: в AVOID есть «no modern objects»; при появлении — добавить «intact buildings, no ruins».
```
[SCENE ROLE] Final shot: Vera stands alone on an empty city street.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting, abandoned.
[SUBJECT & ACTION] Vera, a woman in her mid-twenties, stands still in the middle of an empty street, seen from behind. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel.
[SETTING & ERA] Pripyat after the evacuation of 1986, overcast evening, empty apartment blocks.
[BACKGROUND] No people, no movement.
[CAMERA] Static wide shot from behind, vertical 9:16 composition.
[LIGHT & PALETTE] Cold grey light.
[START/END] Starts and ends with her standing still.
[AUDIO] She does not speak; no dialogue; natural ambient sound: wind
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no chaotic camera.
```
