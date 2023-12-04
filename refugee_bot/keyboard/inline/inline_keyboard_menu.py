from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard_menu = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text='Swap buttons?', callback_data='buttons swapped'),
                                                    InlineKeyboardButton(text='Link', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                                                ],
                                                [
                                                    InlineKeyboardButton(text='Alert!', callback_data='alert')
                                                ],
                                                [
                                                    InlineKeyboardButton(text='Swap inline buttons?', callback_data='inline buttons swapped')
                                                ]
                                            ])