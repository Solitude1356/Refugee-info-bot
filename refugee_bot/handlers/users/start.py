from aiogram import types
from loader import dp
import asyncio

@dp.message_handler(text = '/start')
async def command_start(message: types.Message):
    await message.answer(f'Вітаю, {message.from_user.full_name}.\n'
                         f'Цей бот слугує для допомоги біженцям за кордоном у пошуку вакансій')
    await asyncio.sleep(2)
    await message.answer(f'Щогодини ви будете отримувати повідомлення з вакансіями, що вас цікавлять')
    await asyncio.sleep(2)
    await message.answer(f'Якщо ви згодні, за допомогою команди /subscribe додайте ключові слова для пошуку')