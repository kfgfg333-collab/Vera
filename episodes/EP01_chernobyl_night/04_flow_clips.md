# Клипы Google Flow — EP01 (версия 2, концепция v4)

Стандарт: `knowledge/google_flow_guide.md` §3–4. Файл 02 готов (`02_vera_costume_reference_prompt.md`).

**Главное правило:** Вера в кадре во **всех 12 клипах** от первого до последнего кадра, лицо читается; станция, взрыв, пожарные, Припять — за её спиной. Каждый промпт самодостаточен и сам закрепляет присутствие Веры (блок [VERA] + запрет в [AVOID]).
**Режимы:** TALK — Вера говорит в камеру (сгенерированная речь заменяется озвучкой ElevenLabs); REACT — смотрит на событие, рот закрыт, голос поверх.
**Референсы (≤ 3):** Вера — персонаж `Vera EP01` (если Characters работают в режиме) **или** `@vera_face` + `@vera_EP01_costume`; + локация (`@loc_unit4_night` / `@loc_control_room` / `@loc_pripyat_street`); в клипах 08–09 + `@ref_firefighter`. Листы A/B не прикреплять. Метки заменить на имена, которые Flow показывает после `@`. Реальных людей — без фото, безымянными образами эпохи.
**Что сделано и что нет:** промпты подготовлены, но **не сгенерированы и не протестированы** во Flow — результат проверяется при генерации.

| № | Таймкод (расчёт) | Длит. | Модель/режим | Вера | Событие за ней |
|---|---|---|---|---|---|
| 01 | 0:00–0:05 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | TALK · Передний план | Спокойная ночная станция: горят окна, лёгкий пар из вентиляции, двое р… |
| 02 | 0:05–0:13 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | REACT · Средний план | Три оператора в белых халатах и шапочках работают за длинным пультом: … |
| 03 | 0:13–0:23 | 10 с | Gemini Omni Flash 1.1 · Ingredients · 10 с | TALK · Средне-крупный план | На стене за ней начинают мигать несколько лампочек мнемосхемы; стрелка… |
| 04 | 0:23–0:29 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | REACT · Передний план слева | Молодой оператор в белом халате твёрдо нажимает большую квадратную кно… |
| 05 | 0:29–0:37 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | REACT · Средний план | Зал начинает дрожать: лампы мигают, стрелки приборов уходят до упора, … |
| 06 | 0:37–0:42 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | REACT · Передний план | Первый взрыв пара и обломков над крышей 4-го блока; через две секунды … |
| 07 | 0:42–0:48 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | TALK · Средний план | Над развороченным блоком красное свечение; по плоской кровле машзала г… |
| 08 | 0:48–0:53 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | REACT · Передний план слева | Две красные пожарные машины тормозят у машзала, пожарные в брезентовых… |
| 09 | 0:53–1:00 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | TALK · Передний план | Четыре пожарных на кровле направляют две струи воды на огонь; огонь по… |
| 10 | 1:00–1:05 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | TALK · Средний план | Обычная жизнь: женщина с сумкой, отец с коляской, двое мужчин разговар… |
| 11 | 1:05–1:12 | 8 с | Veo 3.1 Fast · Ingredients · 8 с | REACT · Передний план справа | Длинная колонна жёлто-кремовых автобусов вдоль улицы; жители с маленьк… |
| 12 | 1:12–1:23 | 10 с | Gemini Omni Flash 1.1 · Ingredients · 10 с | TALK · Средний план | Город пуст после эвакуации: тёмные окна, пустая остановка, ветер гонит… |

Вера во всех клипах: 12 из 12. TALK: 6 · REACT: 6. Сумма клипов: 100 с ≥ расчётная озвучка ≈ 83 с + запас. Таймкоды — расчётные (145 сл/мин), после озвучки сверить.

---
## Клип 01
1. **Номер и длительность / таймкод / модель:** 01 · 8 с (в монтаже ≈ 0:00–0:05) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Видите здание за моей спиной? Через несколько минут реактор в нём взорвётся.»
3. **Положение Веры в начале кадра:** Передний план, нижняя треть кадра, по центру; за ней через площадку — корпус 4-го блока с полосатой трубой.
4. **Выражение лица, взгляд, действие:** Говорит в камеру (TALK), тихое напряжение; на «за моей спиной» коротко оглядывается на здание и снова смотрит в камеру.
5. **Что происходит на фоне и как меняется:** Спокойная ночная станция: горят окна, лёгкий пар из вентиляции, двое рабочих в спецовках проходят вдоль машзала. Ничего не взрывается — тревога только в её лице.
6. **Композиция и движение камеры:** Средний план, медленный наезд; Вера внизу, здание и труба в верхней половине.
7. **Свет, атмосфера, детали эпохи:** Оранжевые натриевые фонари, холодное синее небо, тёплый блик на лице Веры; апрель 1986, ясная ночь.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или персонаж `@Vera EP01`) + `@loc_unit4_night`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: Вера смотрит в камеру → прямая склейка в блочный щит (02).
10. **Основной промпт:**
```
[SCENE ROLE] Hook: Vera faces the camera in front of the Chernobyl unit 4 building minutes before the accident.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_unit4_night as the setting and the exact look of the plant buildings.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground, lower third, centred, the unit 4 building and the red-and-white striped ventilation stack rising behind her. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: quiet tension; she glances back over her shoulder at the building once, then looks into the camera again.
[EVENT BEHIND HER] The plant is calm: lit windows, a thin plume of steam from a vent, two workers in dark work clothes walk slowly along the turbine hall; nothing explodes.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, about 1 a.m., clear calm spring night, concrete reactor building, long turbine hall, sodium street lamps, power lines.
[CAMERA] Medium shot, slow push-in toward Vera, vertical 9:16 composition: Vera in the lower half, the building and stack in the upper half.
[LIGHT & PALETTE] Warm orange sodium light on her face, cold dark-blue sky, cool white window light.
[START/END] Starts with Vera already looking into the camera. Ends with Vera looking into the camera, the plant calm behind her.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: night crickets, distant transformer hum.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Буквы на здании, лишние рабочие, «гриб» или огонь раньше времени; если лицо мелкое — запасной (ближе).
```
[SCENE ROLE] Hook: Vera in front of a Soviet nuclear power plant at night.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_unit4_night as the setting and the exact look of the plant buildings.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground, lower third, centred. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: quiet tension, looking into the camera.
[EVENT BEHIND HER] A calm power plant with a striped ventilation stack and lit windows behind her.
[SETTING & ERA] Chernobyl nuclear power plant, night of 26 April 1986, clear spring night.
[CAMERA] Static medium shot, vertical 9:16 composition, Vera in the lower half.
[LIGHT & PALETTE] Orange street-lamp light, dark-blue sky.
[START/END] Starts and ends with Vera looking into the camera.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: crickets.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 02
1. **Номер и длительность / таймкод / модель:** 02 · 8 с (в монтаже ≈ 0:05–0:13) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Двадцать шестое апреля восемьдесят шестого, Чернобыльская станция. Четвёртый блок перед ремонтом, и ночью на нём проводят испытание.»
3. **Положение Веры в начале кадра:** Средний план, левая треть кадра, у стены блочного щита; операторы за пультом — справа и в глубине.
4. **Выражение лица, взгляд, действие:** REACT: рот закрыт, внимательно и настороженно смотрит на операторов; в конце коротко переводит взгляд в камеру.
5. **Что происходит на фоне и как меняется:** Три оператора в белых халатах и шапочках работают за длинным пультом: один следит за приборами, другой переключает тумблер, третий что-то говорит, не поворачиваясь (без звука речи). Её никто не замечает (🎭).
6. **Композиция и движение камеры:** Средний план, медленный боковой проезд слева направо вдоль пульта; Вера остаётся в левой трети.
7. **Свет, атмосфера, детали эпохи:** Холодный люминесцентный свет, серо-зелёные пульты, красные и жёлтые лампочки; ночь.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_control_room`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: взгляд Веры в камеру → склейка на её крупный план (03) в том же зале.
10. **Основной промпт:**
```
[SCENE ROLE] Immersion: Vera stands inside the unit 4 control room while the night shift prepares a test; nobody notices her.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, left third of the frame, standing by the wall, the control desks and operators to her right and behind her. She does not speak; her mouth is closed. Emotion and gaze: alert and uneasy; she watches the operators, then briefly looks into the camera at the end.
[EVENT BEHIND HER] Three operators in white cotton lab coats and white caps work at the long control desk: one watches the gauges, one flips a switch, one leans toward a colleague; none of them looks at Vera.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, about 1 a.m., Soviet control room, long grey-green control desks, a wall panel with a circular grid of small lamps.
[CAMERA] Medium shot, slow lateral dolly from left to right along the desks, vertical 9:16 composition: Vera in the left third, operators in the right two thirds.
[LIGHT & PALETTE] Cold fluorescent ceiling light, pale green-grey palette, small red and amber indicator lamps, her wine-red scarf as the warm accent.
[START/END] Starts with Vera watching the operators. Ends with Vera glancing into the camera.
[AUDIO] She does not speak; no dialogue; natural ambient sound: electrical hum, soft relay clicks.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Надписи на пульте, лишние пальцы у операторов, операторы смотрят на Веру (нельзя — она незаметна).
```
[SCENE ROLE] Immersion: Vera inside a Soviet control room at night.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, left third. She does not speak; her mouth is closed. Emotion and gaze: uneasy, watching the room.
[EVENT BEHIND HER] Two operators in white coats sit at a long control desk behind her.
[SETTING & ERA] Soviet nuclear plant control room, night of 26 April 1986.
[CAMERA] Static medium shot, vertical 9:16 composition, Vera on the left.
[LIGHT & PALETTE] Cold fluorescent light, small red lamps.
[START/END] Starts and ends with Vera watching the operators.
[AUDIO] She does not speak; no dialogue; natural ambient sound: electrical hum.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 03
1. **Номер и длительность / таймкод / модель:** 03 · 10 с (в монтаже ≈ 0:13–0:23) · Gemini Omni Flash 1.1 · Ingredients · 10 с
2. **Фрагмент озвучки:** «Но реактор уже в опасном режиме — мощность упала слишком низко. А у таких реакторов есть изъян: в этом режиме они могут резко разогнаться.»
3. **Положение Веры в начале кадра:** Средне-крупный план, правая половина кадра; за её плечом — стена с круглой мнемосхемой и операторы.
4. **Выражение лица, взгляд, действие:** TALK: объясняет в камеру просто и тревожно; на «изъян» бросает взгляд на мигающую панель за спиной.
5. **Что происходит на фоне и как меняется:** На стене за ней начинают мигать несколько лампочек мнемосхемы; стрелка круглого прибора дёргается; оператор наклоняется к пульту.
6. **Композиция и движение камеры:** Средне-крупный план, очень медленный наезд; панель за плечом в фокусе.
7. **Свет, атмосфера, детали эпохи:** Холодный свет, мигающие янтарные лампочки отражаются на её лице.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_control_room`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: Вера оборачивается к пульту → склейка на нажатие кнопки за ней (04).
10. **Основной промпт:**
```
[SCENE ROLE] Rising tension: Vera explains to the camera that the reactor is in a dangerous state while warning lamps flicker behind her.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: medium close-up, right half of the frame, the wall panel and the operators visible over her shoulder. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: worried, explaining simply; on the word about the flaw she glances back at the flickering panel, then returns her eyes to the camera.
[EVENT BEHIND HER] Behind her several lamps on the circular wall panel start to blink, the needle of a round gauge twitches, an operator leans in toward the desk.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, about 1:20 a.m., Soviet control room, grey-green desks, round gauges, wall panel with a circular grid of small lamps.
[CAMERA] Medium close-up, very slow push-in, vertical 9:16 composition: Vera on the right, the blinking panel on the left and behind her, in focus.
[LIGHT & PALETTE] Cold fluorescent light, blinking amber lamps reflecting on her face.
[START/END] Starts with Vera looking into the camera. Ends with Vera turning her head toward the control desk.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: electrical hum, a faint irregular beeping.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Нарисованные цифры/буквы на приборах; дрожание лица при наезде. Omni Text/Ingredients 10 с — подтверждено (Ingredients); если Omni недоступен — Veo Fast 8 с, фраза уйдёт на начало 04.
```
[SCENE ROLE] Rising tension: Vera talks to the camera in a control room as warning lamps blink.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: medium close-up, right half. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: worried, looking into the camera.
[EVENT BEHIND HER] Warning lamps blink on the wall panel behind her.
[SETTING & ERA] Soviet nuclear plant control room, night of 26 April 1986.
[CAMERA] Static medium close-up, vertical 9:16 composition.
[LIGHT & PALETTE] Cold light, amber lamps.
[START/END] Starts and ends with Vera looking into the camera.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: electrical hum.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 04
1. **Номер и длительность / таймкод / модель:** 04 · 8 с (в монтаже ≈ 0:23–0:29) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Час двадцать три. Оператор нажимает кнопку аварийной остановки. Почему именно сейчас — так и не выяснили.»
3. **Положение Веры в начале кадра:** Передний план слева, в профиль/три четверти к пульту; оператор и кнопка — в центре на среднем плане.
4. **Выражение лица, взгляд, действие:** REACT: рот закрыт; затаила дыхание, смотрит на руку оператора; лицо в три четверти, эмоция читается.
5. **Что происходит на фоне и как меняется:** Молодой оператор в белом халате твёрдо нажимает большую квадратную кнопку; двое коллег оборачиваются к нему.
6. **Композиция и движение камеры:** Через плечо Веры: её голова и плечо на переднем плане слева, рука на кнопке в фокусе; статично.
7. **Свет, атмосфера, детали эпохи:** Холодный свет, красные лампочки.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_control_room`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: кнопка нажата, лампы мигают → склейка на тряску зала (05).
10. **Основной промпт:**
```
[SCENE ROLE] Turning point: behind Vera an operator presses the emergency shutdown button.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground left, her head and shoulder in three-quarter view toward the desk, face visible. She does not speak; her mouth is closed. Emotion and gaze: holding her breath, tense, eyes fixed on the operator's hand.
[EVENT BEHIND HER] A young operator in a white lab coat and cap firmly presses a single large square push-button on the control desk; two colleagues turn toward him.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, 1:23 a.m., Soviet control room, grey-green desks, rows of switches, indicator lamps.
[CAMERA] Static over-the-shoulder medium shot, vertical 9:16 composition: Vera's head and shoulder in the left foreground, the hand on the button in focus in the centre.
[LIGHT & PALETTE] Cold fluorescent light, red indicator lamps lighting up.
[START/END] Starts with the operator's hand above the button and Vera watching. Ends with the button pressed, lamps flashing, Vera still in frame.
[AUDIO] She does not speak; no dialogue; natural ambient sound: electrical hum, one heavy click.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Надписи на кнопке; Вера уходит из кадра при фокусе на руке — в промпте зафиксировано, что её голова и плечо остаются.
```
[SCENE ROLE] Turning point: an operator presses a button on a control desk while Vera watches.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground left, three-quarter view. She does not speak; her mouth is closed. Emotion and gaze: tense.
[EVENT BEHIND HER] A man in a white lab coat presses a large button on a control desk.
[SETTING & ERA] Soviet control room, night of 26 April 1986.
[CAMERA] Static over-the-shoulder shot, vertical 9:16 composition.
[LIGHT & PALETTE] Cold light, red lamps.
[START/END] Starts and ends with Vera watching the desk.
[AUDIO] She does not speak; no dialogue; natural ambient sound: a click.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 05
1. **Номер и длительность / таймкод / модель:** 05 · 8 с (в монтаже ≈ 0:29–0:37) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Стержни идут вниз, чтобы заглушить реактор. Но из-за их устройства в первые секунды они его разгоняют.»
3. **Положение Веры в начале кадра:** Средний план, центр; операторы и мигающая панель за ней.
4. **Выражение лица, взгляд, действие:** REACT: рот закрыт; страх нарастает, хватается за край пульта, оглядывается на панель.
5. **Что происходит на фоне и как меняется:** Зал начинает дрожать: лампы мигают, стрелки приборов уходят до упора, операторы вскакивают; с потолка сыплется пыль.
6. **Композиция и движение камеры:** Средний план, лёгкая ручная камера (одно направление — лёгкая тряска), Вера в центре.
7. **Свет, атмосфера, детали эпохи:** Мигающий люминесцентный свет, красные тревожные лампы.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_control_room`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: сильный толчок, свет гаснет на мгновение → склейка на улицу, взрыв за Верой (06).
10. **Основной промпт:**
```
[SCENE ROLE] Escalation: the control room shakes as the power surges; Vera grabs the edge of a desk.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, centred, operators and the blinking wall panel behind her. She does not speak; her mouth is closed. Emotion and gaze: growing fear; she grips the edge of a desk and looks back at the panel.
[EVENT BEHIND HER] The room begins to tremble: lamps flicker, gauge needles swing to the limit, the operators jump up from their seats, dust falls from the ceiling.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, 1:23 a.m., Soviet control room, grey-green desks, round gauges, wall panel with a circular grid of lamps.
[CAMERA] Medium shot, gentle handheld shake in one direction, vertical 9:16 composition: Vera in the centre, operators behind her.
[LIGHT & PALETTE] Flickering fluorescent light, red alarm lamps.
[START/END] Starts with a first tremor. Ends with a strong jolt and the lights dipping for a moment, Vera still in frame.
[AUDIO] She does not speak; no dialogue; natural ambient sound: rising low rumble, rattling metal.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Хаотичная камера, искажение лица при тряске → запасной статичный.
```
[SCENE ROLE] Escalation: Vera in a shaking control room.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_control_room as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, centred. She does not speak; her mouth is closed. Emotion and gaze: afraid.
[EVENT BEHIND HER] Lamps flicker and the operators stand up behind her.
[SETTING & ERA] Soviet control room, night of 26 April 1986.
[CAMERA] Static medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Flickering light, red lamps.
[START/END] Starts and ends with Vera holding the desk.
[AUDIO] She does not speak; no dialogue; natural ambient sound: low rumble.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 06
1. **Номер и длительность / таймкод / модель:** 06 · 8 с (в монтаже ≈ 0:37–0:42) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Два взрыва. Крышу реакторного зала разносит, раскалённые обломки летят на соседние здания.»
3. **Положение Веры в начале кадра:** Передний план, правая треть, на открытой площадке на безопасной дистанции; взрыв — над 4-м блоком в верхней левой части кадра.
4. **Выражение лица, взгляд, действие:** REACT: рот закрыт; шок, вздрагивает от первого взрыва, прикрывает лицо рукой при втором, затем смотрит на зарево.
5. **Что происходит на фоне и как меняется:** Первый взрыв пара и обломков над крышей 4-го блока; через две секунды второй, сильнее — светящиеся фрагменты летят высоко, начинает подниматься столб дыма и пара у полосатой трубы.
6. **Композиция и движение камеры:** Общий план с Верой, статично, лёгкая тряска на каждом ударе.
7. **Свет, атмосфера, детали эпохи:** Ночная синева, вспышки оранжево-белого, красное зарево на лице Веры.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_unit4_night`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: обломки падают, Вера опускает руку → склейка на её средний план у горящих крыш (07).
10. **Основной промпт:**
```
[SCENE ROLE] Climax: two explosions tear through the unit 4 reactor building behind Vera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_unit4_night as the setting and the exact look of the plant buildings.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground, right third of the frame, standing on open ground at a distance, the unit 4 building in the upper left behind her. She does not speak; her mouth is closed. Emotion and gaze: shock; she flinches at the first blast, raises an arm to shield her face at the second, then stares at the glow.
[EVENT BEHIND HER] A first bright burst of steam and debris erupts from the roof of the unit 4 reactor building; two seconds later a second, larger blast throws glowing fragments high into the night sky; a column of smoke and steam rises beside the striped stack.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, about 1:24 a.m., clear calm night.
[CAMERA] Wide shot with Vera, static camera with a light shake on each blast, vertical 9:16 composition: Vera in the lower right, the explosions in the upper left.
[LIGHT & PALETTE] Night blue broken by orange-white flashes, a red glow on Vera's face.
[START/END] Starts with Vera standing and the plant intact. Ends with glowing fragments falling and Vera lowering her arm, still in frame.
[AUDIO] She does not speak; no dialogue; natural ambient sound: two deep booms two seconds apart, a rumbling echo.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups. No mushroom cloud.
```
11. **Нежелательные артефакты и запасной вариант:** «Ядерный гриб» (👁 неверный образ) — в AVOID; если блок генератора — запасной: «industrial steam explosion», силуэт Веры на фоне вспышки (лестница, ступень 3).
```
[SCENE ROLE] Climax: an industrial steam explosion at a power plant behind Vera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_unit4_night as the setting and the exact look of the plant buildings.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground right, in silhouette against the flash. She does not speak; her mouth is closed. Emotion and gaze: shock, shielding her face.
[EVENT BEHIND HER] A bright burst of steam, smoke and glowing debris erupts from the roof of a large concrete industrial building behind her.
[SETTING & ERA] Soviet power plant, night of 26 April 1986, clear night.
[CAMERA] Static wide shot, vertical 9:16 composition, Vera in the lower right.
[LIGHT & PALETTE] Orange flash, dark-blue night.
[START/END] Starts with the flash. Ends with smoke rising and Vera still in frame.
[AUDIO] She does not speak; no dialogue; natural ambient sound: a deep boom.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups. No mushroom cloud.
```

---
## Клип 07
1. **Номер и длительность / таймкод / модель:** 07 · 8 с (в монтаже ≈ 0:42–0:48) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Реактор разрушен. На крышах пожар. А радиацию не видно и не слышно.»
3. **Положение Веры в начале кадра:** Средний план, центр-низ; за ней разрушенный верх 4-го блока и горящая кровля машзала.
4. **Выражение лица, взгляд, действие:** TALK: потрясена, говорит в камеру тихо и отрывисто; на «не видно и не слышно» оглядывается на зарево.
5. **Что происходит на фоне и как меняется:** Над развороченным блоком красное свечение; по плоской кровле машзала горят очаги, разлетаются искры; дым тянется к трубе.
6. **Композиция и движение камеры:** Средний план, медленный отъезд назад (масштаб растёт).
7. **Свет, атмосфера, детали эпохи:** Красно-оранжевое зарево на лице и пальто Веры, тёмное небо, серый дым.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_unit4_night`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: вдали появляются синие проблесковые огни → склейка на приезд пожарных (08).
10. **Основной промпт:**
```
[SCENE ROLE] Aftermath of the blast: Vera speaks to the camera in front of the wrecked, burning unit 4.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_unit4_night as the setting and the exact look of the plant buildings.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, lower centre, the wrecked top of unit 4 and the burning turbine hall roof behind her. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: shaken, speaking quietly and abruptly; at the end she glances back at the glow.
[EVENT BEHIND HER] A red glow rises from the open, wrecked top of the unit 4 building; several fires burn across the flat roof of the turbine hall, sparks drift, smoke flows toward the striped stack.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, about 1:30 a.m., clear night.
[CAMERA] Medium shot, slow pull-back that reveals the scale of the fires, vertical 9:16 composition: Vera in the lower centre, the fires in the upper half.
[LIGHT & PALETTE] Red-orange firelight on her face and coat, dark sky, grey smoke.
[START/END] Starts with Vera looking into the camera. Ends with blue flashing lights appearing far behind her, Vera still in frame.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: crackling fire, a distant siren starting.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups. No mushroom cloud.
```
11. **Нежелательные артефакты и запасной вариант:** Ожоги/кровь на людях — не показывать; лишние люди на крыше.
```
[SCENE ROLE] Vera in front of a burning industrial building at night.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_unit4_night as the setting and the exact look of the plant buildings.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, lower centre. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: shaken, looking into the camera.
[EVENT BEHIND HER] Fires burn on a flat industrial roof behind her; smoke rises.
[SETTING & ERA] Soviet power plant, night of 26 April 1986.
[CAMERA] Static medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Orange firelight, dark sky.
[START/END] Starts and ends with Vera looking into the camera.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: crackling fire.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 08
1. **Номер и длительность / таймкод / модель:** 08 · 8 с (в монтаже ≈ 0:48–0:53) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Первыми приезжают пожарные. Они поднимаются на крыши — совсем рядом с открытым реактором.»
3. **Положение Веры в начале кадра:** Передний план слева; машины и пожарные проезжают/бегут за ней к стене здания.
4. **Выражение лица, взгляд, действие:** REACT: рот закрыт; тревога и сочувствие, провожает пожарных взглядом.
5. **Что происходит на фоне и как меняется:** Две красные пожарные машины тормозят у машзала, пожарные в брезентовых куртках и касках выпрыгивают, тянут рукава и бегут к вертикальной стальной лестнице; наверху — огонь.
6. **Композиция и движение камеры:** Средний план, плавная панорама справа налево вслед за пожарными; Вера остаётся слева на переднем плане.
7. **Свет, атмосфера, детали эпохи:** Синие проблесковые огни + оранжевый огонь сверху, ночь.
8. **Постоянство внешности Веры (что прикрепить):** Персонаж `@Vera EP01` + `@loc_unit4_night` + `@ref_firefighter`; если персонажа нет — `@vera_face` + `@vera_EP01_costume` + `@ref_firefighter` (станция — текстом). Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: первый пожарный хватается за лестницу → склейка на крышу (09).
10. **Основной промпт:**
```
[SCENE ROLE] Response: firefighters arrive and run toward the burning building behind Vera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @ref_firefighter as the exact look of the firefighters' uniforms.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground left, three-quarter view, the fire engines and firefighters passing behind her. She does not speak; her mouth is closed. Emotion and gaze: anxious and compassionate; she follows the firefighters with her eyes.
[EVENT BEHIND HER] Two red Soviet fire engines brake near the turbine hall; firefighters in dark canvas turnout coats and helmets jump out, pull hoses and run behind her toward a vertical steel ladder on the wall; fire glows on the roof above.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, USSR, night of 26 April 1986, about 1:30 a.m., clear night, long turbine hall, 1970s bonneted red Soviet fire trucks with a white stripe and blue flashing lights.
[CAMERA] Medium shot, smooth pan from right to left following the firefighters, vertical 9:16 composition: Vera stays in the left foreground.
[LIGHT & PALETTE] Blue flashing lights mixed with orange firelight from above, dark night.
[START/END] Starts with the trucks braking behind Vera. Ends with the first firefighter grabbing the ladder, Vera still in frame.
[AUDIO] She does not speak; no dialogue; natural ambient sound: engines idling, boots on concrete, hoses unrolling, fire crackling above.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Надписи на машинах; пожарные проходят «сквозь» Веру — в промпте они бегут позади неё.
```
[SCENE ROLE] Firefighters run past behind Vera toward a burning building at night.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @ref_firefighter as the exact look of the firefighters' uniforms.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground left. She does not speak; her mouth is closed. Emotion and gaze: anxious.
[EVENT BEHIND HER] Three firefighters in dark canvas coats and helmets run behind her toward a building with fire on the roof.
[SETTING & ERA] Soviet power plant, night of 26 April 1986.
[CAMERA] Static medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Blue flashing light, orange glow.
[START/END] Starts and ends with Vera in the foreground.
[AUDIO] She does not speak; no dialogue; natural ambient sound: running boots.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 09
1. **Номер и длительность / таймкод / модель:** 09 · 8 с (в монтаже ≈ 0:53–1:00) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Огонь на крышах сбивают за несколько часов. Но шестеро пожарных потом умрут от лучевой болезни.»
3. **Положение Веры в начале кадра:** Передний план, нижняя треть, ниже уровня крыши; на крыше за ней — силуэты пожарных со шлангами на фоне зарева и трубы.
4. **Выражение лица, взгляд, действие:** TALK: тихо, с болью; на второй фразе опускает взгляд, затем снова смотрит в камеру.
5. **Что происходит на фоне и как меняется:** Четыре пожарных на кровле направляют две струи воды на огонь; огонь постепенно ослабевает, в небе начинает светлеть (ночь переходит в предрассветную синеву).
6. **Композиция и движение камеры:** Общий план с Верой, нижний ракурс, очень медленный наезд.
7. **Свет, атмосфера, детали эпохи:** Красное зарево сменяется холодной предрассветной синевой; струи воды ловят свет.
8. **Постоянство внешности Веры (что прикрепить):** Персонаж `@Vera EP01` + `@loc_unit4_night` + `@ref_firefighter`; если персонажа нет — `@vera_face` + `@vera_EP01_costume` + `@ref_firefighter`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: огонь почти погас, небо светлеет → склейка на утро в Припяти (10).
10. **Основной промпт:**
```
[SCENE ROLE] Resolution of the night: firefighters on the roof put out the fires behind Vera as dawn approaches.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @ref_firefighter as the exact look of the firefighters' uniforms.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground, lower third, below roof level, the firefighters on the roof above and behind her. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: quiet pain; she lowers her eyes on the second sentence, then looks into the camera again.
[EVENT BEHIND HER] Four firefighters in silhouette stand on the high flat roof and direct two canvas hoses at the fire; during the clip the flames weaken and the sky begins to pale before dawn; smoke rises past the red-and-white striped stack.
[SETTING & ERA] Chernobyl nuclear power plant, Ukrainian SSR, early morning of 26 April 1986, before dawn, calm weather, firefighters in dark canvas turnout coats and helmets without respirators.
[CAMERA] Wide shot with Vera, low angle, very slow push-in, vertical 9:16 composition: Vera in the lower third, the roof and firefighters in the upper half.
[LIGHT & PALETTE] Red glow fading into cold pre-dawn blue, white water jets catching the light.
[START/END] Starts with flames on the roof and Vera looking into the camera. Ends with the fire almost out, the sky paler, Vera still in frame.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: rushing water jets, hiss of steam, fading fire.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Больше 4 людей на крыше; портретное сходство с реальными пожарными не добиваемся (🎭).
```
[SCENE ROLE] Firefighters with hoses on a roof behind Vera before dawn.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @ref_firefighter as the exact look of the firefighters' uniforms.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground, lower third. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: quiet pain, looking into the camera.
[EVENT BEHIND HER] Silhouettes of three firefighters spray water at a fire on a flat roof behind her.
[SETTING & ERA] Soviet power plant roof, early morning of 26 April 1986, red-and-white striped stack.
[CAMERA] Static wide shot, low angle, vertical 9:16 composition.
[LIGHT & PALETTE] Fading red glow, pale pre-dawn sky.
[START/END] Starts and ends with Vera in the foreground.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: water jets.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 10
1. **Номер и длительность / таймкод / модель:** 10 · 8 с (в монтаже ≈ 1:00–1:05) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Утро. В Припяти обычная суббота. Об аварии городу не сказали.»
3. **Положение Веры в начале кадра:** Средний план, левая нижняя треть, у автобусной остановки; прохожие за ней; на горизонте справа — тонкий столб дыма над станцией.
4. **Выражение лица, взгляд, действие:** TALK: горькое спокойствие; смотрит в камеру, на последней фразе переводит взгляд на прохожих.
5. **Что происходит на фоне и как меняется:** Обычная жизнь: женщина с сумкой, отец с коляской, двое мужчин разговаривают (без звука речи), голуби; далеко над крышами — серый дым.
6. **Композиция и движение камеры:** Средний план, статично.
7. **Свет, атмосфера, детали эпохи:** Мягкое утреннее солнце, бледно-голубое небо, тёплые тона.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_pripyat_street`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: Вера смотрит на прохожих → склейка на автобусы (11).
10. **Основной промпт:**
```
[SCENE ROLE] Contrast: an ordinary Saturday morning in Pripyat while smoke rises over the distant plant; Vera speaks to the camera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, lower left third, by a bus stop, passers-by behind her, a thin smoke plume on the horizon to the right. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: bitter calm; she looks into the camera and on the last sentence turns her eyes to the passers-by.
[EVENT BEHIND HER] An ordinary morning: a woman with a shopping bag, a father with a pram and two men chatting walk calmly behind her; pigeons on the pavement; far beyond the rooftops a thin grey smoke plume rises over the power plant.
[SETTING & ERA] Pripyat, Ukrainian SSR, Saturday morning, 26 April 1986, sunny and warm, white panel apartment blocks, young poplars with fresh leaves.
[CAMERA] Static medium shot, vertical 9:16 composition: Vera lower left, passers-by in the middle, the smoke plume upper right.
[LIGHT & PALETTE] Soft warm morning sun, pale blue sky, her wine-red scarf as the accent.
[START/END] Starts with Vera looking into the camera. Ends with Vera looking at the passers-by, still in frame.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: birds, footsteps, distant voices without words.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Надписи на остановке/вывесках; руки у прохожих — не более 4–5 человек на среднем плане.
```
[SCENE ROLE] Vera on a sunny morning street; a smoke plume on the horizon.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, lower left. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: bitter calm, looking into the camera.
[EVENT BEHIND HER] A few passers-by walk behind her; a thin smoke plume far on the horizon.
[SETTING & ERA] Pripyat, morning of 26 April 1986, sunny, white apartment blocks.
[CAMERA] Static medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Warm morning sun.
[START/END] Starts and ends with Vera in frame.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: birds.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 11
1. **Номер и длительность / таймкод / модель:** 11 · 8 с (в монтаже ≈ 1:05–1:12) · Veo 3.1 Fast · Ingredients · 8 с
2. **Фрагмент озвучки:** «Только на следующий день к домам подают автобусы. Около пятидесяти тысяч человек уезжают. Им говорят — временно.»
3. **Положение Веры в начале кадра:** Передний план справа, три четверти к колонне автобусов; колонна уходит в глубину кадра слева.
4. **Выражение лица, взгляд, действие:** REACT: рот закрыт; печаль, смотрит на людей у дверей автобуса, в конце — короткий взгляд в камеру.
5. **Что происходит на фоне и как меняется:** Длинная колонна жёлто-кремовых автобусов вдоль улицы; жители с маленькими сумками и чемоданами спокойно садятся; мать ведёт ребёнка за руку; милиционер в серой форме у двери; первый автобус трогается.
6. **Композиция и движение камеры:** Общий план с Верой, медленный боковой проезд вдоль колонны.
7. **Свет, атмосфера, детали эпохи:** Яркий весенний день, мягкие тени, приглушённые пастельные тона.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_pripyat_street`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Конец: автобус уезжает, Вера смотрит в камеру → склейка на пустую улицу (12).
10. **Основной промпт:**
```
[SCENE ROLE] Consequence: residents board a long column of evacuation buses behind Vera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground right, three-quarter view toward the bus column, the column receding into the depth on the left. She does not speak; her mouth is closed. Emotion and gaze: sadness; she watches the people at the bus doors and briefly looks into the camera at the end.
[EVENT BEHIND HER] A long column of yellow and cream Soviet city buses stands along the street; residents with small bags and suitcases quietly walk to the doors and board, a mother leads a child by the hand, a policeman in a grey 1980s Soviet militia uniform stands by a door; the first bus starts to move.
[SETTING & ERA] Pripyat, Ukrainian SSR, afternoon of 27 April 1986, sunny and warm, white panel apartment blocks, young poplars, 1980s LAZ and Ikarus style buses.
[CAMERA] Wide shot with Vera, slow lateral dolly along the column, vertical 9:16 composition: Vera in the right foreground, the column on the left.
[LIGHT & PALETTE] Bright spring daylight, soft shadows, muted pastel colours.
[START/END] Starts with people walking to the buses behind Vera. Ends with the first bus pulling away and Vera looking into the camera.
[AUDIO] She does not speak; no dialogue; natural ambient sound: bus engines, footsteps, quiet murmur without words.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```
11. **Нежелательные артефакты и запасной вариант:** Номера и надписи на автобусах; толпа «кипит» — люди идут в одном направлении к дверям.
```
[SCENE ROLE] A column of buses behind Vera during an evacuation.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: foreground right. She does not speak; her mouth is closed. Emotion and gaze: sad.
[EVENT BEHIND HER] A long column of Soviet buses stands along a street of apartment blocks; a few people walk to the doors.
[SETTING & ERA] Pripyat, afternoon of 27 April 1986, sunny.
[CAMERA] Static wide shot, vertical 9:16 composition, Vera on the right.
[LIGHT & PALETTE] Bright daylight.
[START/END] Starts and ends with Vera in frame.
[AUDIO] She does not speak; no dialogue; natural ambient sound: bus engines.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups.
```

---
## Клип 12
1. **Номер и длительность / таймкод / модель:** 12 · 10 с (в монтаже ≈ 1:12–1:23) · Gemini Omni Flash 1.1 · Ingredients · 10 с
2. **Фрагмент озвучки:** «Виновата не одна кнопка, а изъян реактора, о котором персонал толком не знал, и нарушения при испытании. Город, которому было шестнадцать лет, пустует до сих пор.»
3. **Положение Веры в начале кадра:** Средний план, центр, посреди пустой улицы; за ней — те же дома с тёмными окнами.
4. **Выражение лица, взгляд, действие:** TALK: тихо и твёрдо в камеру; на последней фразе поднимает взгляд на тёмные окна и снова смотрит в камеру.
5. **Что происходит на фоне и как меняется:** Город пуст после эвакуации: тёмные окна, пустая остановка, ветер гонит листья; ни одного человека. Здания целые (это 1986, не руины 2000-х).
6. **Композиция и движение камеры:** Средний план → очень медленный отъезд назад, Вера становится меньше, улица — больше.
7. **Свет, атмосфера, детали эпохи:** Холодный пасмурный вечер, десатурация; её винный шарф — единственный тёплый цвет.
8. **Постоянство внешности Веры (что прикрепить):** `@vera_face` + `@vera_EP01_costume` (или `@Vera EP01`) + `@loc_pripyat_street`. Блок [REFERENCES] + [VERA] с описанием лица и костюма — в промпте.
9. **Финал клипа и переход:** Финал: последняя фраза → выдержка 1–2 с на Вере → затемнение.
10. **Основной промпт:**
```
[SCENE ROLE] Final: Vera alone in the empty, evacuated city speaks to the camera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, centred, in the middle of the empty street, the apartment blocks with dark windows behind her. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: quiet and firm; on the last sentence she looks up at the dark windows, then back into the camera.
[EVENT BEHIND HER] The city is empty after the evacuation: dark windows, an empty bus stop, the wind pushes fallen leaves along the pavement; no other people; the buildings are intact.
[SETTING & ERA] Pripyat, Ukrainian SSR, after the evacuation of 27 April 1986, overcast evening, white panel apartment blocks, poplars.
[CAMERA] Medium shot with a very slow pull-back, vertical 9:16 composition: Vera centred, growing smaller as the empty street opens up around her.
[LIGHT & PALETTE] Cold grey-blue overcast light, desaturated palette, her wine-red scarf the only warm colour.
[START/END] Starts with Vera looking into the camera. Ends with Vera small in the centre of the empty street, still looking into the camera.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: wind, rustling leaves, silence.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups. Intact buildings, no ruins, no graffiti.
```
11. **Нежелательные артефакты и запасной вариант:** Руины/граффити/деревья сквозь асфальт (анахронизм для 1986) → «intact buildings, no ruins». Фраза ≈ 10 с — на пределе клипа: при нехватке — стоп-кадр последней секунды (Вера в кадре).
```
[SCENE ROLE] Final: Vera stands alone on an empty city street and speaks to the camera.
[REFERENCES] Use @vera_face as the exact identity and @vera_EP01_costume as the exact outfit of the woman (Vera). Keep her face, age, eye shape, grey-green eyes, mole under the eye, freckles, dark-brown shoulder-length wavy hair and natural adult proportions identical. Use @loc_pripyat_street as the setting.
[VERA] Vera is the main character and stays clearly visible in frame from the first to the last frame, face readable. She wears a knee-length charcoal-grey wool coat with broad shoulders, a wine-red knitted scarf and a small brass compass brooch on the lapel. Position: mid-ground, centred. She talks to the camera, her lips moving naturally as she speaks. Emotion and gaze: quiet and firm, looking into the camera.
[EVENT BEHIND HER] Empty apartment blocks with dark windows behind her; no other people.
[SETTING & ERA] Pripyat after the evacuation of 1986, overcast evening.
[CAMERA] Static medium shot, vertical 9:16 composition.
[LIGHT & PALETTE] Cold grey light.
[START/END] Starts and ends with Vera looking into the camera.
[AUDIO] Any generated speech will be replaced in editing; natural ambient sound: wind.
[STYLE] Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions, expressive but realistic facial acting, detailed materials (skin texture, wool, linen, leather, wood, stone, metal, smoke, snow, mud), natural motivated lighting, atmospheric depth, historically plausible props and architecture. Not cartoonish, not childlike, not photorealistic. No on-screen text, no subtitles, no logos, no watermarks.
[AVOID] No shots without Vera, Vera must not leave the frame, no text, no logos, no watermarks, no extra limbs or fingers, no face changes, no outfit changes, no modern objects, no anachronisms, no chaotic camera, no gratuitous gore close-ups. Intact buildings, no ruins.
```
