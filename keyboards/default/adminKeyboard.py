from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Tugma qo`shish'),
        ],
    ],
    resize_keyboard=True
)