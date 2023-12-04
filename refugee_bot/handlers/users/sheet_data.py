from re import I
from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
from keyboard.inline.inline_sheet_data import inline_sheet_countries, inline_sheet_themes, inline_sheet_issues_0, inline_sheet_issues_1, inline_sheet_issues_2, inline_sheet_issues_3, inline_sheet_issues_4, inline_sheet_issues_5, inline_sheet_issues_6, inline_sheet_issues_7, inline_sheet_issues_8, inline_sheet_issues_9, inline_sheet_issues_10, inline_sheet_issues_11
from keyboard.inline import inline_keyboard_menu
from keyboard.inline import inline_keyboard_menu_2
from keyboard.default import keyboard_test
from sheetsApi import sheet_values
from telegramApi.client import check_and_get
import asyncio

# ----------------------Країни------------------------

@dp.message_handler(text = '/info')
async def choose_country(message: types.Message):
    await message.answer('Наразі доступна лише Італія')
    await asyncio.sleep(0.5)
    await message.answer('Оберіть країну, яка цікавить:', reply_markup=inline_sheet_countries)
    
@dp.callback_query_handler(text = '0 country')
async def pushed_reply(call: CallbackQuery):
    await call.message.edit_reply_markup(inline_sheet_themes)
    
# @dp.callback_query_handler(text = '2 country')
# async def pushed_reply(call: CallbackQuery):
#     await call.message.answer(f'{sheet_values[1][2]}')
    
@dp.callback_query_handler(text = '0 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][0][0]}:', reply_markup=inline_sheet_issues_0)
    
@dp.callback_query_handler(text = '1 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][1][0]}:', reply_markup=inline_sheet_issues_1)
    
@dp.callback_query_handler(text = '2 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][2][0]}:', reply_markup=inline_sheet_issues_2)
    
@dp.callback_query_handler(text = '3 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][3][0]}:', reply_markup=inline_sheet_issues_3)
    
@dp.callback_query_handler(text = '4 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][4][0]}:', reply_markup=inline_sheet_issues_4)
    
@dp.callback_query_handler(text = '5 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][5][0]}:', reply_markup=inline_sheet_issues_5)
    
@dp.callback_query_handler(text = '6 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][6][0]}:', reply_markup=inline_sheet_issues_6)
    
@dp.callback_query_handler(text = '7 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][7][0]}:', reply_markup=inline_sheet_issues_7)
    
@dp.callback_query_handler(text = '8 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][8][0]}:', reply_markup=inline_sheet_issues_8)
    
@dp.callback_query_handler(text = '9 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][9][0]}:', reply_markup=inline_sheet_issues_9)
    
@dp.callback_query_handler(text = '10 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][10][0]}:', reply_markup=inline_sheet_issues_10)
    
@dp.callback_query_handler(text = '11 theme')
async def pushed_reply(call: CallbackQuery):
    await call.message.answer(f'{sheet_values[1][11][0]}:', reply_markup=inline_sheet_issues_11)
    
    
# ----------------------Питання------------------------
    
    

# @dp.callback_query_handler(text = '0 1 issue')
# async def pushed_reply(call: CallbackQuery):
#     message_ok = check_and_get(sheet_values[2][1][1])
#     msg = message_ok('message')
#     await call.message.answer(msg)
    
# @dp.callback_query_handler(text = '0 3 issue')
# async def pushed_reply(call: CallbackQuery):
#     message_ok = check_and_get(sheet_values[2][3][1])
#     msg = message_ok('message')
#     await call.message.answer(msg)

    
