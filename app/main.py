#main.py
import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers import register_handlers
from commands import register_commands

import asyncio
from database import create_pool, close_pool

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)

    try:
        await register_handlers(dp)
        await register_commands(dp)
    except Exception as e:
        print(f"Ошибка при регистрации обработчиков и команд: {e}")
    else:
        await dp.start_polling(skip_updates=True)

async def main():
    # ... (предыдущий код)
    await create_pool()  # Создание пула подключений
    try:
        # ... (код для регистрации обработчиков и команд)
        await dp.start_polling(skip_updates=True)
        
    finally:
        await close_pool()  # Закрытие пула подключений
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен.")