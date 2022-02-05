from cgitb import text
from email import message
from unicodedata import name
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import InputFile
from keyboards.default.adminKeyboard import admin
from aiogram.dispatcher import FSMContext
from states.personalData import personalData

from loader import dp


@dp.message_handler(chat_id=5069753238,text = "Admin_panel")
async def bot_tart(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n Admin panelga xush kelibsiz.", reply_markup=admin)
    await personalData.main.set()

