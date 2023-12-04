from aiogram import types
from loader import dp
import asyncio

@dp.message_handler(text = '/help')
async def command_help(message: types.Message):
    await message.answer('Тут будудуть описані функції бота')
    await asyncio.sleep(1.5)
    await message.answer('Наразі, бот може надати корисну інформацію для біженців про країну, що цікавить')
    await asyncio.sleep(2)
    await message.answer('Вже зараз ви можете переглянути каталог за командою /info')