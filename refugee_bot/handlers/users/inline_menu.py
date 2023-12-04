from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from keyboard.inline import inline_keyboard_menu
from keyboard.inline import inline_keyboard_menu_2
from keyboard.default import keyboard_test

@dp.message_handler(text = 'Inline')
async def show_inline_menu(message: types.Message):
    await message.answer('inline buttons are below', reply_markup=inline_keyboard_menu)
    
@dp.callback_query_handler(text = 'buttons swapped')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer('pushed', reply_markup=keyboard_test)
    
@dp.callback_query_handler(text = 'alert')
async def pushed_reply(call: CallbackQuery):
    await call.answer('alert active')                                                           # Popup notification
    
@dp.callback_query_handler(text = 'inline buttons swapped')
async def pushed_reply(call: CallbackQuery):
    await call.message.edit_reply_markup(inline_keyboard_menu_2)