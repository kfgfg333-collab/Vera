# Костюмный референс Веры — EP01, Припять, апрель 1986

## Исследование костюма
| Элемент | Решение для эпохи | Источник |
|---|---|---|
| Нижняя/верхняя одежда | Угольно-серое шерстяное пальто до колена с широкими плечами и поясом; под ним бежевый свитер ручной вязки; прямая тёмная юбка ниже колена, плотные тёмные колготки | Широкие плечи у пальто и пиджаков 1980-х — «Вокруг света» (13); вязаные вещи (в т. ч. перевязанные из старых) — «Афиша Daily» (14). Юбка и колготки — 🎭 нейтральный вариант |
| Обувь | Коричневые кожаные ботинки на низком каблуке | 🎭 (без сенсационных деталей; проверить по фото Припяти 1986) |
| Головной убор / причёска | Без головного убора (тёплая весна); волосы свои, до плеч, распущены | 🎭; апрель, ночь/день — не зимняя одежда |
| Материалы и цвета (винный акцент) | Шерсть, вязка, кожа; **винный вязаный шарф** — фирменный акцент Веры | 13, 14; палитра — `vera_character_bible.md` |
| Аксессуары (брошь-компас) | Латунная брошь-компас на лацкане пальто (читается как значок/брошь эпохи); коричневая кожаная сумка через плечо | `vera_character_bible.md` |
| Социальный статус «легенды» | Молодая жительница Припяти / приезжая специалистка (город молодых: строился с 1970) | 🎭; возраст города — источники 10, 11 в 01 |
| Где спрятан прибор | Под левым рукавом пальто | `vera_character_bible.md` |

Источники по костюму — в таблице выше и в `01_research_and_factcheck.md` (13, 14). Оба популярные, музейный источник по женской одежде УССР 1986 не найден — элементы выбраны базовые, без спорных деталей.

## Что загрузить (ingredients)
- `references/vera_face_reference.png` — лицо (**главный** источник идентичности)
- `references/vera_body_reference.png` — тело и пропорции (**главный**)
- Листы `vera_character_sheet_A/B.png` **не загружать**.
Настройки во Flow: режим Image, модель Nano Banana (по умолчанию Pro), «Image aspect ratio» 9:16 (или 3:4), 2–4 варианта.

## Промпт 1 — полный рост (Nano Banana во Flow или Gemini)
```
Use the uploaded face image as the strict identity reference and the uploaded body image as the reference for body shape and proportions of the same woman, Vera. Keep exactly the same face, age (mid-twenties), eye shape and grey-green eye color, the small mole under the eye, light freckles, dark-brown hair color and length, and the same slim athletic natural adult proportions. Change only the clothing and the way the hair is arranged, to a Soviet mid-1980s spring outfit: a knee-length charcoal-grey wool coat with broad padded shoulders and a fabric belt, worn open over a beige hand-knitted wool sweater; a long wine-red hand-knitted scarf; a straight dark-grey wool skirt below the knee with opaque dark tights; brown leather ankle boots with a low heel; a worn brown leather shoulder bag; a small brass compass-rose brooch on the coat lapel. Hair loose to the shoulders with a light natural wave, no hat. Full-body front view, standing in a relaxed neutral pose, arms slightly away from the body so the costume reads clearly, plain light warm-grey studio background, soft even lighting, high detail on fabrics and fastenings. Semi-realistic cinematic 3D/2.5D animation style with a subtle painterly texture; not cartoonish, not photorealistic. Single character only, no text, no logos, no watermark, no props except the shoulder bag.
```

## Промпт 2 — портрет (по необходимости: головной убор, причёска)
```
Use the uploaded face image as the strict identity reference and the uploaded full-body costume image as the outfit reference for the same woman, Vera: identical face, grey-green eyes, mole under the eye, freckles, dark-brown hair. Head-and-shoulders portrait, three-quarter view, wearing the same charcoal-grey wool coat with broad shoulders, the wine-red hand-knitted scarf wrapped loosely around the neck, the beige knitted sweater collar visible, and the small brass compass-rose brooch on the lapel; hair loose to the shoulders. Plain light warm-grey background, soft key light. Semi-realistic cinematic animation style with painterly texture. No text, no logos.
```

## Отбор
Лицо узнаётся? Родинка на месте? Пропорции не «кукольные»? Костюм без анахронизмов (нет пуховиков, кроссовок, логотипов, современных молний)? → сохранить как `refs/costume.png` (+ `refs/costume_portrait.png`); во Flow — оставить в проекте (рабочая метка `vera_EP01_costume`) и, если доступно, создать персонажа `Vera EP01` в Characters (2 изображения: полный рост + портрет). Имена внесены в `09_continuity.md` → «Ассеты Flow».

## Референсы локаций и участников (фон за Верой; делать после костюма)
Режим Image, 9:16, без людей (кроме референса пожарного). Это фон и участники для клипов — **в самих клипах Вера всегда в кадре**. Сохранить в `refs/`.

`loc_control_room` — `refs/loc_control_room.png`:
```
Vertical 9:16 image of a Soviet nuclear power plant unit control room at night in 1986: long grey-green control desks with rows of switches, round analogue gauges and small indicator lamps, a large wall panel covered with a circular grid of small lamps, cold fluorescent ceiling light, linoleum floor, no windows. No people. Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural motivated lighting, atmospheric depth. No text, no letters, no labels with readable writing, no logos, no watermark.
```


`loc_unit4_night` — `refs/loc_unit4_night.png`:
```
Vertical 9:16 wide establishing image of a large Soviet nuclear power plant at night in spring 1986: long rectangular concrete reactor building of unit 4 with a tall red-and-white striped ventilation stack beside it, a long turbine hall in front, sodium street lamps, a few lit windows, power lines, flat landscape, clear dark-blue night sky. No people. Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural motivated lighting, atmospheric depth. No text, no letters, no logos, no watermark.
```

`loc_pripyat_street` — `refs/loc_pripyat_street.png`:
```
Vertical 9:16 image of a residential street in a young Soviet city in April 1986: nine- and sixteen-storey white panel apartment blocks, wide pavements, young poplar trees with first green leaves, a bus stop shelter, simple street lamps, early morning soft light. No people, no cars. Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural lighting. No text, no letters, no signs with readable writing, no logos, no watermark.
```

`ref_firefighter` — `refs/ref_firefighter.png`:
```
Vertical 9:16 full-body reference image of a Soviet firefighter in 1986, a man in his twenties: dark canvas firefighter turnout coat with a wide belt, canvas trousers, rubber boots, a simple dark fire helmet, no respirator mask, holding a folded canvas fire hose. Plain light warm-grey background, soft even light. Semi-realistic cinematic 3D/2.5D animation with a subtle painterly texture, natural adult proportions. Single character only, no text, no badges with readable writing, no logos, no watermark.
```
