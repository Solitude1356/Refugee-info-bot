from aiogram import types
from loader import dp
from keyboard.default import keyboard_test

@dp.message_handler(text = 'test text')
async def command_start(message: types.Message):
    await message.answer(f'Another hello, {message.from_user.full_name}\n'
                         f'Your ID is {message.from_user.id}', reply_markup=keyboard_test)