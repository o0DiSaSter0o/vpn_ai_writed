import aiohttp
from app.config import MARZBAN_API_URL, MARZBAN_API_KEY

async def activate_trial(user_id):
    """Активация пробного периода для пользователя."""
    async with aiohttp.ClientSession() as session:
        data = {"user_id": user_id, "api_key": MARZBAN_API_KEY}
        async with session.post(f"{MARZBAN_API_URL}/activate_trial", json=data) as response:
            if response.status == 200:
                return "Пробный период активирован! Инструкции отправлены вам в сообщении."
            else:
                return "Произошла ошибка при активации пробного периода."

async def buy_subscription(user_id, subscription_type):
    """Покупка подписки для пользователя."""
    async with aiohttp.ClientSession() as session:
        data = {"user_id": user_id, "subscription_type": subscription_type, "api_key": MARZBAN_API_KEY}
        async with session.post(f"{MARZBAN_API_URL}/buy_subscription", json=data) as response:
            if response.status == 200:
                return "Подписка успешно приобретена! Инструкции отправлены вам в сообщении."
            else:
                return "Произошла ошибка при покупке подписки."

async def get_user_info(user_id):
    """Получение информации о пользователе."""
    async with aiohttp.ClientSession() as session:
        params = {"user_id": user_id, "api_key": MARZBAN_API_KEY}
        async with session.get(f"{MARZBAN_API_URL}/user_info", params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                return "Ошибка получения информации о пользователе."

async def add_balance(user_id, amount):
    """Пополнение баланса пользователя."""
    async with aiohttp.ClientSession() as session:
        data = {"user_id": user_id, "amount": amount, "api_key": MARZBAN_API_KEY}
        async with session.post(f"{MARZBAN_API_URL}/add_balance", json=data) as response:
            if response.status == 200:
                return "Баланс успешно пополнен!"
            else:
                return "Ошибка пополнения баланса."

async def process_subscription_payment(user_id, subscription_type):
    """Обработка платежа и активация подписки."""
    async with aiohttp.ClientSession() as session:
        data = {"user_id": user_id, "subscription_type": subscription_type, "api_key": MARZBAN_API_KEY}
        async with session.post(f"{MARZBAN_API_URL}/process_payment", json=data) as response:
            if response.status == 200:
                return "Подписка успешно активирована! Спасибо за покупку."
            else:
                return "Произошла ошибка при обработке платежа."

async def get_subscription_details(user_id):
    """Получение деталей подписки пользователя."""
    async with aiohttp.ClientSession() as session:
        params = {"user_id": user_id, "api_key": MARZBAN_API_KEY}
        async with session.get(f"{MARZBAN_API_URL}/subscription_details", params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                return "Ошибка получения деталей подписки."