# Завдання 2.3: POST-запити, Headers та Bearer Token

POST-запити використовуються для створення сутностей на сервері (новий пост, оплата, реєстрація).  
Майже всі захищені API вимагають передавати токен авторизації у заголовках (`headers`):
```python
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
payload = {"title": "Новий пост", "price": 100}
response = requests.post(url, json=payload, headers=headers)
```

### 🎯 Ваше завдання:
Реалізуйте функцію `create_remote_post(api_url: str, token: str, title: str, content: str) -> dict`:
1. Сформуйте словник `headers` з авторизаційним заголовком:
   `"Authorization": f"Bearer {token}"`.
2. Сформуйте тіло запиту (`payload`) зі словником `{"title": title, "content": content}`.
3. Зробіть POST-запит: `requests.post(api_url, json=payload, headers=headers)`.
4. Якщо `response.status_code == 201` (успішно створено), поверніть `{"success": True, "data": response.json()}`.
5. Для будь-якого іншого коду поверніть `{"success": False, "status_code": response.status_code}`.
