async def on_startup(dp):
    from utils.notify_admin import on_startup_notify
    await on_startup_notify(dp)
    
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    
    print('LOG: Activated')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    
    executor.start_polling(dp, on_startup=on_startup)

# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor

# bot = Bot(token='')

# dp = Dispatcher(bot)

# @dp.message_handler()
# async def response(message: types.Message):
#     #chatId = message.chat.id
    
#     text = 'kk'
    
#     await message.answer(f'Ok, {message.from_user.full_name}, "{message.text}"')
    
# executor.start_polling(dp)