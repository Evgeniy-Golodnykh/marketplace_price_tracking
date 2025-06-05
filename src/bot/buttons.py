from aiogram.types import BotCommand, KeyboardButton

from bot import text
from core.constants import TRACKING_DURATION

START_CMD = BotCommand(command=text.START, description=text.START_DESC)
MENU_CMD = BotCommand(command=text.MENU, description=text.MENU_DESC)
FAVORITE_CMD = BotCommand(
    command=text.FAVORITE, description=text.FAVORITE_DESC
)
INFO_CMD = BotCommand(command=text.INFO, description=text.INFO_DESC)

main_menu_buttons = [
    [
        KeyboardButton(text=text.ADD_ITEM_MESSAGE),
        KeyboardButton(text=text.FAVORITE_DESC)
    ]
]
duration_buttons = [
    [KeyboardButton(text=TRACKING_DURATION[i]),
     KeyboardButton(text=TRACKING_DURATION[i + 1])]
    for i in range(0, len(TRACKING_DURATION), 2)
]
