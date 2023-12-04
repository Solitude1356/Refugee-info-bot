from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp
from keyboard.default import keyboard_menu

@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    await message.answer('Question?')
#    await message.answer(reply_markup=keyboard_menu)