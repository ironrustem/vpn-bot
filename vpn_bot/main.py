import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Text
from aiogram.filters.command import Command
import os
import sys
from aiogram.types import FSInputFile, InputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, я бот Маркиз!👋 Я дам доступ к впн)💻")

    kb = [
        [types.KeyboardButton(text="Готов!")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Ну что, готов получить доступ к лучшему сервису ?", reply_markup=keyboard)

@dp.message(Text(text="Готов!"))
async def cmd_start(message: types.Message):
    if not os.path.exists("/root/wg0-client-{message.from_user.id}.conf"):
        print(os.system(f"/opt/vpn-bot/vpn_bot/wireguard-install.sh {message.from_user.id}"))

    keyboard = types.ReplyKeyboardRemove()
    await message.answer("Отлично!❤️ Сейчас отправлю тебе файл \n\nТвои шаги: \n1.Cкачай wireguard https://www.wireguard.com/install/ \n2.Открой файл через это приложение", reply_markup=keyboard)
    photo = FSInputFile(f"/root/wg0-client-{message.from_user.id}.conf", filename="W-VPN.conf")
    await bot.send_document(message.chat.id, document=photo)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    bot = Bot(token=sys.argv[1])
    asyncio.run(main())