# Завдання 3.2: Створення структури Inline-клавіатур

В Telegram API кнопки під повідомленнями називаються **Inline Keyboards**.  
Структура клавіатури у форматі Telegram Bot API — це двовимірний список (список рядків, де кожен рядок містить список кнопок-словників):
```json
[
    [{"text": "Курс валют", "callback_data": "get_rates"}],
    [{"text": "Погода", "callback_data": "get_weather"}, {"text": "Допомога", "callback_data": "help"}]
]
```

### 🎯 Ваше завдання:
Реалізуйте функцію `build_inline_keyboard(buttons: list[tuple[str, str]], columns: int = 2) -> list[list[dict]]`:
1. Вона приймає список кортежів `(button_text, callback_data)` та бажану кількість колонок у рядку `columns`.
2. Кожна кнопка формується як словник: `{"text": text, "callback_data": callback_data}`.
3. Функція має розбити кнопки на рядки по `columns` штук у кожному рядку.
   *(Якщо передано 4 кнопки і `columns=2`, результат має містити 2 рядки по 2 кнопки. Якщо 3 кнопки і `columns=2`, перший рядок містить 2 кнопки, другий — 1 кнопку)*.
