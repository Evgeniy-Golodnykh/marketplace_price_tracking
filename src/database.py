import datetime as dt

from sqlalchemy import (
    Column, Date, Integer, String, UniqueConstraint, create_engine,
)
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, declarative_base

from configs import DATABASE

Base = declarative_base()

current_date = dt.date.today()


class Item(Base):
    """Marketplace item model."""

    __tablename__ = 'item'
    __table_args__ = (
        UniqueConstraint('url', 'telegram_id', name='uix_url_telegram_id'),
    )

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    name = Column(String(300))
    url = Column(String(300))
    target_price = Column(Integer)
    create_date = Column(Date, default=current_date)
    expiry_date = Column(Date)

    def __repr__(self):
        return self.name


def get_session():
    """Open a session for database access"""

    engine = create_engine(URL.create(**DATABASE))
    Base.metadata.create_all(engine)
    return Session(engine)


def close_session(session):
    """Close the database access session"""
    session.close()


def add_to_db(session, telegram_id, name, url, target_price, days):
    """Add Item instance to database."""

    if session.query(Item).filter(
        Item.url == url,
        Item.telegram_id == telegram_id
    ).count():
        return False
    session.add(Item(
        telegram_id=telegram_id,
        name=name,
        url=url,
        target_price=target_price,
        expiry_date=current_date + dt.timedelta(days)
    ))
    session.commit()
    return True
