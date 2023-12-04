from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Yes'),
            KeyboardButton(text='No'),
        ],
        [
            KeyboardButton(text='???')
        ],
        [
            KeyboardButton(text='test text'),
            KeyboardButton(text='Inline')
        ]
    ],
    resize_keyboard=True
)