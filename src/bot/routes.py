from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards import main_menu_keyboard, tracking_duration_keyboard
from core.constants import MARKETPLACE_URLS, TRACKING_DURATION

router = Router()


class TrackItem(StatesGroup):
    waiting_for_link = State()
    waiting_for_price = State()
    waiting_for_duration = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'''Привет, {message.from_user.first_name}!
            Бот помогает отслеживать изменение цен товаров маркетплейсов''',
        reply_markup=main_menu_keyboard
    )


@router.message(Command('menu'))
async def cmd_menu(message: Message):
    await message.answer('Главное меню:', reply_markup=main_menu_keyboard)


@router.message(Command('favorite'))
async def cmd_favorite(message: Message):
    await message.answer('Ваши избранные товары:')


@router.message(F.text == 'Добавить товар')
async def add_item(message: Message, state: FSMContext):
    await message.answer('Отправьте ссылку на товар:')
    await state.set_state(TrackItem.waiting_for_link)


@router.message(TrackItem.waiting_for_link)
async def get_link(message: Message, state: FSMContext):
    link = message.text.strip().split('?')[0]
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

    await message.answer(
        'Пожалуйста, выберите срок отслеживания товара из списка ниже:',
        reply_markup=tracking_duration_keyboard
    )
    await state.set_state(TrackItem.waiting_for_duration)


@router.message(TrackItem.waiting_for_duration)
async def get_duration(message: Message, state: FSMContext):
    if message.text not in TRACKING_DURATION:
        await message.answer(
            'Пожалуйста, выберите срок отслеживания товара из списка ниже:',
            reply_markup=tracking_duration_keyboard
        )
        return
    data = await state.get_data()
    link = data['link']
    price = data['price']
    duration = int(message.text.split()[0])

    await message.answer(
        f'''Товар добавлен:
            Ссылка: {link}
            Цена: {price} ₽
            Срок: {duration} дней
            Ваш Telegram ID: {message.from_user.id}''',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(F.text == 'Избранное')
async def show_favorites(message: Message):
    await message.answer('Список избранных товаров:')
