import logging
from aiogram import Dispatcher
from data.config import adminId

async def on_startup_notify(dp: Dispatcher):
    for admin in adminId:
        try: 
            text = 'Activated'
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logging.exception(err)