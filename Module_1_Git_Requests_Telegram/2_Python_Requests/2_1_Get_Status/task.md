# Завдання 2.1: HTTP GET-запити та статус-коди

Бібліотека `requests` — це стандарт для взаємодії з REST API на Python.

### 📚 Теорія:
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.ok)           # True (якщо код 200..299)
```
Статус-коди:
* **2xx (200, 201)**: Успіх.
* **4xx (400, 401, 403, 404)**: Помилка клієнта (невірний запит, нема доступу, не знайдено).
* **5xx (500, 502)**: Помилка на стороні сервера.

### 🎯 Ваше завдання:
Реалізуйте функцію `check_service_status(url: str) -> dict`:
1. Зробіть GET-запит за переданою URL-адресою за допомогою `requests.get(url, timeout=5)`.
2. Якщо запит пройшов успішно (статус 200..299):
   поверніть словник: `{"is_online": True, "status_code": <код>}`.
3. Якщо сервер повернув помилку (наприклад 404 або 500):
   поверніть: `{"is_online": False, "status_code": <код>}`.
4. Якщо виникла мережева помилка (наприклад `requests.RequestException`):
   перехопіть виключення і поверніть: `{"is_online": False, "status_code": None}`.
