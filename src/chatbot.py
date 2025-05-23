import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    BotCommand, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup,
    KeyboardButton, MenuButtonCommands, Message, ReplyKeyboardMarkup,
)

from configs import configure_logging
from constants import MARKETPLACE_URLS, TELEGRAM_TOKEN


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
    link = message.text.strip()
    if all([url not in link for url in MARKETPLACE_URLS]):
        await message.answer('Пожалуйста, введите корректную ссылку')
        return
    await state.update_data(link=link)
    await message.answer('Введите желаемую цену:')
    await state.set_state(TrackItem.waiting_for_price)


@router.message(TrackItem.waiting_for_price)
async def get_price(message: Message, state: FSMContext):
    try:
        price = int(message.text.strip())
        if price < 1:
            raise ValueError
    except ValueError:
        await message.answer('Пожалуйста, введите положительное целое число')
        return
    await state.update_data(price=price)

    durations = ['10', '20', '30', '60']
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=f'{d} дней', callback_data=f'duration_{d}')]
            for d in durations
        ]
    )
    await message.answer('Выберите срок отслеживания:', reply_markup=keyboard)
    await state.set_state(TrackItem.waiting_for_duration)


@router.callback_query(F.data.startswith('duration_'))
async def handle_duration_callback(callback: CallbackQuery, state: FSMContext):
    duration = callback.data.split('_')[1]
    data = await state.get_data()
    link = data['link']
    price = data['price']

    await callback.message.edit_reply_markup()
    await callback.message.answer(
        f'''Товар добавлен:
            Ссылка: {link}
            Цена: {price}
            Срок: {duration} дней'''
    )
    await callback.message.answer(
        'Выберите следующее действие:', reply_markup=main_menu
    )
    await state.clear()


@router.message(F.text == 'Избранное')
async def show_favorites(message: Message):
    await message.answer('Список избранных товаров:')


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Начать работу'),
        BotCommand(command='menu', description='Главное меню'),
        BotCommand(command='favorite', description='Избранные товары'),
        BotCommand(command='stop', description='Завершить работу')
    ])
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    configure_logging()
    asyncio.run(main())
