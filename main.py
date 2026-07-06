import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from dotenv import load_dotenv
import os
load_dotenv()
Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Katalog'), KeyboardButton(text='Sebet')],
        [KeyboardButton(text='Baylanis')],

    ],
    resize_keyboard=True
)
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Kitaplar"),
            KeyboardButton(text="📝 Bánt etiw")
        ],
        [
            KeyboardButton(text="⏰ Qaytarıw múddeti")
        ]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Assalawma aleykum 😊",reply_markup=menu)

<<<<<<< HEAD
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Kitaplar"),
            KeyboardButton(text="📝 Bánt etiw")
        ],
        [
            KeyboardButton(text="⏰ Qaytarıw múddeti")
        ]
    ],
    resize_keyboard=True
)

=======
@dp.message(Command('email'))
async def email(message: Message):
    await message.answer("kadirbergenova",reply_markup=menu)
>>>>>>> 442ee37927e630390e110b265480762f96adefe0

async def main():
    print('bot iske qosildi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())