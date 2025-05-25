from aiogram.types import BotCommand, KeyboardButton

START_CMD = BotCommand(command='start', description='Начать работу')
MENU_CMD = BotCommand(command='menu', description='Главное меню')
FAVORITE_CMD = BotCommand(command='favorite', description='Избранные товары')

main_menu_buttons = [
    [KeyboardButton(text='Добавить товар'), KeyboardButton(text='Избранное')]
]
duration_buttons = [
    [KeyboardButton(text='15 дней'), KeyboardButton(text='30 дней')],
    [KeyboardButton(text='45 дней'), KeyboardButton(text='60 дней')],
]
