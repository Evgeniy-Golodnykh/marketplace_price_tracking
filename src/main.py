import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import MenuButtonCommands

from bot.buttons import FAVORITE_CMD, INFO_CMD, MENU_CMD, START_CMD
from bot.routes import router
from core.configs import configure_logging
from core.constants import TELEGRAM_TOKEN

# from core.database import init_models


async def main():
    bot = Bot(
        token=TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())
    await bot.set_my_commands([START_CMD, MENU_CMD, FAVORITE_CMD, INFO_CMD])
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())
    dp.include_router(router)
    # await init_models()
    await dp.start_polling(bot)


if __name__ == '__main__':
    configure_logging()
    asyncio.run(main())
