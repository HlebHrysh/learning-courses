# Завдання 2.2: Параметри запиту (Params) та парсинг JSON

Коли ми шукаємо або фільтруємо дані в API, ми передаємо параметри у запиті через `params`:
```python
params = {"category": "books", "limit": 10}
response = requests.get("https://api.example.com/items", params=params)
data = response.json()  # перетворює JSON відповідь у python-словник або список
```

### 🎯 Ваше завдання:
Реалізуйте функцію `filter_active_users(api_url: str, min_rating: float) -> list[str]`:
1. Зробіть GET-запит до `api_url`, передавши query-параметр `status="active"`.
2. Отримайте список користувачів через `response.json()`. Формат списку:
   ```json
   [
       {"username": "alex", "rating": 4.8},
       {"username": "olena", "rating": 3.9}
   ]
   ```
3. Відфільтруйте користувачів: залиште тільки тих, у кого `rating >= min_rating`.
4. Поверніть список їхніх імен (`username`).
