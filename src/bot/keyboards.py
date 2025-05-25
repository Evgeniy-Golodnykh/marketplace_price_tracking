from aiogram.types import ReplyKeyboardMarkup

from bot.buttons import duration_buttons, main_menu_buttons

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=main_menu_buttons,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие:',
)

tracking_duration_keyboard = ReplyKeyboardMarkup(
    keyboard=duration_buttons,
    resize_keyboard=True,
    one_time_keyboard=True,
)
