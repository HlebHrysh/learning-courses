# Завдання 3.3: Міні-проект: Інтеграція Telegram + Requests

Це кульмінаційне завдання першого модуля! Ми об'єднуємо роботу з мережею (`requests`) та сервісну логіку бота.

### 🎯 Ваше завдання:
Реалізуйте сервісну функцію для бота `fetch_crypto_rate_message(crypto_id: str) -> str`:
1. Зробіть GET-запит до публічного CoinGecko API:
   `url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd,eur"`
2. Якщо статус відповіді `200`:
   * Отримайте JSON: `data = response.json()`.
   * Якщо `crypto_id` є в `data` (наприклад `data["bitcoin"]`):
     Отримайте ціни `usd = data[crypto_id]["usd"]` та `eur = data[crypto_id]["eur"]`.
     Поверніть відформатований рядок повідомлення:
     `f"💰 Курс {crypto_id.capitalize()}:\n💵 USD: ${usd}\n💶 EUR: €{eur}"`
   * Якщо монету не знайдено у відповіді:
     поверніть: `f"Криптовалюту '{crypto_id}' не знайдено."`
3. Якщо статус не 200 або виникла помилка з'єднання (`requests.RequestException`):
   поверніть: `"Сервіс курсів валют тимчасово недоступний. Спробуйте пізніше."`
