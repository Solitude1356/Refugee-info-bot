from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types
import asyncio

from loader import dp
from states import stateRegister

@dp.message_handler(Command('register'))
async def register(message: types.Message):
    await message.answer('Registration started')
    await asyncio.sleep(1)
    await message.answer('Enter your name:')
    await stateRegister.name.set()
    
@dp.message_handler(state=stateRegister.name)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Your age:')
    await stateRegister.age.set()
    
@dp.message_handler(state=stateRegister.age)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Registration is complete\n')
    await asyncio.sleep(1)
    await message.answer(f"Your name is {data['name']}\n"
                         f"Your age is {data['age']}")
    await state.finish()