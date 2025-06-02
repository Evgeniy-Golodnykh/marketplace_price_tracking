import datetime as dt
from contextlib import asynccontextmanager

from sqlalchemy import (
    Column, Date, Integer, String, UniqueConstraint, delete, select,
)
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.configs import DATABASE

Base = declarative_base()


class Item(Base):
    """Marketplace item model."""

    __tablename__ = 'item'
    __table_args__ = (
        UniqueConstraint('url', 'telegram_id', name='uix_url_telegram_id'),
    )

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    marketplace = Column(String(50))
    url = Column(String(500))
    target_price = Column(Integer)
    create_date = Column(Date, default=dt.date.today)
    expiry_date = Column(Date)

    def __repr__(self):
        return self.name


engine = create_async_engine(URL.create(**DATABASE), echo=False)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session


async def get_all_items(session, telegram_id=None):
    """Get all or Telegram user Item instances."""

    if telegram_id:
        result = await session.execute(
            select(Item).where(Item.telegram_id == telegram_id)
        )
    else:
        result = await session.execute(select(Item))
    return result.scalars().all()


async def create_item(
        session,
        telegram_id,
        url,
        marketplace,
        target_price,
        days,
):
    """Add Item instance to database with uniqueness check."""

    uniq_check = await session.execute(
        select(Item).where(Item.url == url, Item.telegram_id == telegram_id)
    )
    if uniq_check.scalar():
        return False

    item = Item(
        telegram_id=telegram_id,
        url=url,
        marketplace=marketplace,
        target_price=target_price,
        expiry_date=dt.date.today() + dt.timedelta(days=days)
    )

    session.add(item)
    try:
        await session.commit()
        return True
    except IntegrityError:
        await session.rollback()
        return False


async def delete_item(session, telegram_id, url):
    """Delete a Item instance."""

    stmt = delete(Item).where(Item.telegram_id == telegram_id, Item.url == url)
    result = await session.execute(stmt)
    await session.commit()
    return result.rowcount > 0


'''
async def main():
    await init_models()  # Только один раз при запуске

    async with get_session() as session:
        success = await add_to_db(
            session, 12345, "https://example.com", 1000, 30
        )


if __name__ == "__main__":
    asyncio.run(main())
'''
