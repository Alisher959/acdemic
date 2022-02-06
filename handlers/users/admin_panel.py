from cgitb import text
from email import message
from os import stat
from sre_parse import State
from unicodedata import name
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import InputFile
from keyboards.default.adminKeyboard import admin
from aiogram.dispatcher import FSMContext
from states.personalData import personalData

from loader import dp



