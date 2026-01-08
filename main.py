import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def main():
    # Инициализация бота
    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    
    # Регистрация хендлеров
    register_handlers(dp)
    
    # Запуск бота
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
