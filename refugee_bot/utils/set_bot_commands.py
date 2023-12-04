from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Run bot'),
        types.BotCommand('help', 'Ask for help'),
        types.BotCommand('info', 'Get country info'),
        # types.BotCommand('menu', 'show up buttons'),
        # types.BotCommand('register', 'I need your details'),
        # types.BotCommand('subscribe', 'Задати ключові слова')
    ])
    
    