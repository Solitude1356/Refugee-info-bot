from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
from keyboard.inline import inline_countries
from keyboard.inline import inline_keyboard_menu
from keyboard.inline import inline_keyboard_menu_2
from keyboard.default import keyboard_test
from sheetsApi import sheet_values

@dp.message_handler(text = '/info')
async def choose_country(message: types.Message):
    await message.answer('Оберіть країну, яка цікавить:', reply_markup=inline_countries)
    
@dp.callback_query_handler(text = '0 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][0]}')
    
@dp.callback_query_handler(text = '1 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][1]}')
    
@dp.callback_query_handler(text = '2 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][2]}')
    
@dp.callback_query_handler(text = '3 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][3]}')
    
@dp.callback_query_handler(text = '4 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][4]}')
    
@dp.callback_query_handler(text = '5 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][5]}')
    
@dp.callback_query_handler(text = '6 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][6]}')

    
# @dp.callback_query_handler(text = 'alert')
# async def pushed_reply(call: CallbackQuery):
#     await call.answer('alert active')                                                           # Popup notification
    
# @dp.callback_query_handler(text = 'inline buttons swapped')
# async def pushed_reply(call: CallbackQuery):
#     await call.message.edit_reply_markup(inline_keyboard_menu_2)