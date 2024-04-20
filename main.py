from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers import register_handlers_main
from commands import register_commands_main
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())

if __name__ == '__main__':
    register_handlers_main(dp)
    register_commands_main(dp)
    executor.start_polling(dp, skip_updates=True)