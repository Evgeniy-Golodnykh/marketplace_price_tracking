from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from bot import text
from bot.keyboards import main_menu_keyboard, tracking_duration_keyboard
from core.constants import MARKETPLACE_URLS, TRACKING_DURATION
from core.database import get_items, get_session

router = Router()


class TrackItem(StatesGroup):
    waiting_for_link = State()
    waiting_for_price = State()
    waiting_for_duration = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text.START_MESSAGE.format(name=message.from_user.first_name),
        reply_markup=main_menu_keyboard
    )


@router.message(Command(text.MENU))
async def cmd_menu(message: Message):
    await message.answer(text.MENU_MESSAGE, reply_markup=main_menu_keyboard)


@router.message(Command(text.FAVORITE))
async def cmd_favorite(message: Message):
    async with get_session() as session:
        items = await get_items(session, message.from_user.id)
        text_items = [f'{count + 1}. {items[count]}' for count in len(items)]
    await message.answer(text.FAVORITE_MESSAGE + '\n'.join(text_items))


@router.message(Command(text.INFO))
async def cmd_info(message: Message):
    await message.answer(text.INFO_MESSAGE, reply_markup=main_menu_keyboard)


@router.message(F.text == text.ADD_ITEM_MESSAGE)
async def add_item(message: Message, state: FSMContext):
    await message.answer(text.GET_LINK_MESSAGE)
    await state.set_state(TrackItem.waiting_for_link)


@router.message(TrackItem.waiting_for_link)
async def get_link(message: Message, state: FSMContext):
    link = message.text.strip().split('?')[0]
    if all([url not in link for url in MARKETPLACE_URLS]):
        await message.answer(text.ERROR_LINK_MESSAGE)
        return
    await state.update_data(link=link)
    await message.answer(text.GET_PRICE_MESSAGE)
    await state.set_state(TrackItem.waiting_for_price)


@router.message(TrackItem.waiting_for_price)
async def get_price(message: Message, state: FSMContext):
    try:
        price = int(message.text.strip())
        if price < 1:
            raise ValueError
    except ValueError:
        await message.answer(text.ERROR_PRICE_MESSAGE)
        return
    await state.update_data(price=price)

    await message.answer(
        text.GET_DURATION_MESSAGE, reply_markup=tracking_duration_keyboard
    )
    await state.set_state(TrackItem.waiting_for_duration)


@router.message(TrackItem.waiting_for_duration)
async def get_duration(message: Message, state: FSMContext):
    if message.text not in TRACKING_DURATION:
        await message.answer(
            text.GET_DURATION_MESSAGE, reply_markup=tracking_duration_keyboard
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


@router.message(F.text == text.FAVORITE_DESC)
async def show_favorites(message: Message):
    await cmd_favorite(message)
