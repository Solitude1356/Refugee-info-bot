from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types
import asyncio

from loader import dp
from states import stateRegister

@dp.message_handler(Command('subscribe'))
async def register(message: types.Message):
    await message.answer('Будь ласка, ведіть через кому ключові слова для пошуку:')
    await stateRegister.keys.set()
    
@dp.message_handler(state=stateRegister.keys)
async def state1(message: types.Message, state: FSMContext):
    subscription = message.text.split(',')
    for i in subscription:
        i.strip()
    # subscription = await enumerate(subscription, start = 1)
    await state.update_data(keys=subscription)
    data = await state.get_data()
    await message.answer('Дякую, підписка створенна')

    await asyncio.sleep(1)
    await message.answer(f"Ключові слова: {subscription}")
    await state.finish()