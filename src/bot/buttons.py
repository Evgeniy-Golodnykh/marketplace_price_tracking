from aiogram.types import BotCommand, KeyboardButton

from core.constants import TRACKING_DURATION

START_CMD = BotCommand(command='start', description='Начать работу')
MENU_CMD = BotCommand(command='menu', description='Главное меню')
FAVORITE_CMD = BotCommand(command='favorite', description='Избранные товары')

main_menu_buttons = [
    [KeyboardButton(text='Добавить товар'), KeyboardButton(text='Избранное')]
]
duration_buttons = [
    [KeyboardButton(text=TRACKING_DURATION[i]),
     KeyboardButton(text=TRACKING_DURATION[i + 1])]
    for i in range(0, len(TRACKING_DURATION), 2)
]
