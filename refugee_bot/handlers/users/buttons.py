import asyncio
from aiogram import types
from loader import dp

@dp.message_handler(text = 'Yes')
async def button_yes(message: types.Message):
    await asyncio.sleep(1)
    await message.answer(f'{message.text}???')
    await asyncio.sleep(2)
    await message.answer('Depression has consumed you')
    
@dp.message_handler(text = 'No')
async def button_no(message: types.Message):
    await asyncio.sleep(1)
    await message.answer('Good for you, buddy! Keep it up')
    
@dp.message_handler(text = '???')
async def button_dontKnow(message: types.Message):
    await asyncio.sleep(1)
    await message.answer("You're don't even a man")