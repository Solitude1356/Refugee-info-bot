from aiogram import types
from loader import dp
import asyncio

@dp.message_handler()
async def error(message: types.Message):
    await message.answer(f'Команда {message.text} наразі не доступна')
    await asyncio.sleep(1)
    await message.answer(f'Спробуйте скористатися /info, для перегляду інформації для біженців закордоном')