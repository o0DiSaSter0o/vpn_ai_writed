# config.py
TOKEN = 'your-telegram-bot-token'
MARZBAN_API_URL = 'your-marzban-api-url'
MARZBAN_API_KEY = 'your-marzban-api-key'
# Другие конфигурации
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Токен Telegram бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# URL и ключ доступа к VPN API
MARZBAN_API_URL = os.getenv("MARZBAN_API_URL")
MARZBAN_API_KEY = os.getenv("MARZBAN_API_KEY")

# Параметры подключения к базе данных
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")