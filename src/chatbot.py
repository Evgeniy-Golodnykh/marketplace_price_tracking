import asyncio

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Message,
    ReplyKeyboardMarkup,
)

from configs import configure_logging
from constants import TELEGRAM_TOKEN


class TrackItem(StatesGroup):
    waiting_for_link = State()
    waiting_for_price = State()
    waiting_for_duration = State()


bot = Bot(
    token=TELEGRAM_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[KeyboardButton(text='Добавить товар'),
               KeyboardButton(text='Избранное')]]
)

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='/start - Начать работу', callback_data='start')],
        [InlineKeyboardButton(
            text='/menu - Главное меню', callback_data='menu')],
        [InlineKeyboardButton(
            text='/favorite - Избранные товары', callback_data='favorite')],
        [InlineKeyboardButton(
            text='/stop - Завершить работу', callback_data='stop')]
    ]
)


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'Добро пожаловать! Выберите действие:', reply_markup=main_menu
    )


@router.message(Command('menu'))
async def cmd_menu(message: Message):
    await message.answer('Главное меню:', reply_markup=main_menu)


@router.message(Command('favorite'))
async def cmd_favorite(message: Message):
    await message.answer('Ваши избранные товары:')


@router.message(Command('stop'))
async def cmd_stop(message: Message):
    await message.answer('Работа завершена. Спасибо!')


@router.message(F.text == 'Добавить товар')
async def add_item(message: Message, state: FSMContext):
    await message.answer('Отправьте ссылку на товар:')
    await state.set_state(TrackItem.waiting_for_link)


@router.message(TrackItem.waiting_for_link)
async def get_link(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer('Введите желаемую цену:')
    await state.set_state(TrackItem.waiting_for_price)


@router.message(TrackItem.waiting_for_price)
async def get_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Введите срок отслеживания (в днях):')
    await state.set_state(TrackItem.waiting_for_duration)


@router.message(TrackItem.waiting_for_duration)
async def get_duration(message: Message, state: FSMContext):
    data = await state.get_data()
    link = data['link']
    price = data['price']
    duration = message.text
    await message.answer(
        f'Товар добавлен:\nСсылка: {link}\nЦена: {price}\n'
        f'Срок: {duration} дней'
    )
    await message.answer(
        'Выберите следующее действие:', reply_markup=main_menu
    )
    await state.clear()


@router.message(F.text == 'Избранное')
async def show_favorites(message: Message):
    await message.answer('Список избранных товаров:')


async def main():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начать работу'),
        types.BotCommand(command='menu', description='Главное меню'),
        types.BotCommand(command='favorite', description='Избранные товары'),
        types.BotCommand(command='stop', description='Завершить работу')
    ])
    await bot.set_chat_menu_button(menu_button=types.MenuButtonCommands())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    configure_logging()
    asyncio.run(main())
