import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os
import sys
from aiogram.types import FSInputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, я бот Маркиз!👋 Я даю доступ к впн)💻 \n\nНу что, готов получить доступ к лучшему сервису ?)")

@dp.message(Command("Get"))
async def cmd_start(message: types.Message):
    print(os.system(f"./wireguard-install.sh {message.from_user.id}"))
    agenda = FSInputFile("/root/", filename=f"wg0-client-{message.from_user.id}.conf")
    await message.reply_document(agenda)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    bot = Bot(token=sys.argv[1])
    asyncio.run(main())