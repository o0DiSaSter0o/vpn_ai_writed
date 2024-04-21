import asyncio
import asyncpg
from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

# Глобальная переменная для хранения пула подключений
pool = None

async def create_pool():
    """Создание пула подключений к базе данных."""
    global pool
    pool = await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

async def execute(query, *args):
    """Выполнение SQL запроса."""
    async with pool.acquire() as conn:
        await conn.execute(query, *args)

async def fetch(query, *args):
    """Выполнение SQL запроса и получение результатов."""
    async with pool.acquire() as conn:
        return await conn.fetch(query, *args)

async def close_pool():
    """Закрытие пула подключений."""
    global pool
    await pool.close()
    pool = None