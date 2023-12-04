from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/menu')
        ]
    ],
    resize_keyboard=True
)