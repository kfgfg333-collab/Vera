# Костюмный референс Веры

## Исследование костюма
| Элемент | Решение для эпохи | Источник |
|---|---|---|
| Нижняя/верхняя одежда | | |
| Обувь | | |
| Головной убор / причёска | | |
| Материалы и цвета (винный акцент) | | |
| Аксессуары (брошь-компас как фибула/застёжка?) | | |
| Социальный статус «легенды» | | |
| Где спрятан прибор | | |

Источники по костюму — в таблице выше и в `01_research_and_factcheck.md` (≥2 на ключевые элементы).

## Что загрузить (ingredients)
- `references/vera_face_reference.png` — лицо (**главный** источник идентичности)
- `references/vera_body_reference.png` — тело и пропорции (**главный**)
- (опц.) изображение исторического костюма/музейного предмета — только одежда, без чужого лица в кадре
- Листы `vera_character_sheet_A/B.png` **не загружать**.
Настройки во Flow: режим Image, модель Nano Banana (по умолчанию Pro), «Image aspect ratio» 9:16 (или 3:4), 2–4 варианта.

## Промпт 1 — полный рост (Nano Banana во Flow или Gemini)
```
Use the uploaded face image as the strict identity reference and the uploaded body image as the reference for body shape and proportions of the same woman, Vera. Keep exactly the same face, age (mid-twenties), eye shape and grey-green eye color, the small mole under the eye, light freckles, dark-brown hair color and length, and the same slim athletic natural adult proportions. Change only the clothing and the way the hair is arranged, to [EPOCH COSTUME DESCRIPTION; HAIR ARRANGEMENT / HEADWEAR]. Full-body front view, standing in a relaxed neutral pose, arms slightly away from the body so the costume reads clearly, plain light warm-grey studio background, soft even lighting, high detail on fabrics and fastenings. Semi-realistic cinematic 3D/2.5D animation style with a subtle painterly texture; not cartoonish, not photorealistic. Single character only, no text, no logos, no watermark, no props except [PROPS].
```

## Промпт 2 — портрет (по необходимости: головной убор, причёска)
```
Use the uploaded face image as the strict identity reference and the uploaded full-body costume image as the outfit reference for the same woman, Vera: identical face, grey-green eyes, mole under the eye, freckles, dark-brown hair. Head-and-shoulders portrait, three-quarter view, wearing the same [HEADWEAR / NECKLINE DETAILS] as in the costume image. Plain light warm-grey background, soft key light. Semi-realistic cinematic animation style with painterly texture. No text, no logos.
```

## Отбор
Лицо узнаётся? Родинка на месте? Пропорции не «кукольные»? Костюм без анахронизмов? → сохранить как `refs/costume.png` (+ `refs/costume_portrait.png`); во Flow — оставить в проекте (рабочая метка `vera_EPNN_costume`) и, если доступно, создать персонажа `Vera EPNN` в Characters (2 изображения: полный рост + портрет). Имена внести в `09_continuity.md` → «Ассеты Flow».
