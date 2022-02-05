from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ishdan bo`shash'),
            KeyboardButton(text='🧑‍🏫 O`qituvchilar uchun 🧑‍🏫'),
        ],
        [
            KeyboardButton(text='🧒 Bolalar uchun 👧'),
            KeyboardButton(text='👨‍👨‍👧 Ota-onalar uchun 👨‍👩‍👦‍👦'),
        ],
    ],
    resize_keyboard=True
)
orqaga = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🔙 Orqaga 🔙'),
        ],
    ],
    resize_keyboard=True
)
