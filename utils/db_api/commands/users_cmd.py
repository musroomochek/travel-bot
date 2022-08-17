from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.users import Users


async def add_user(telegram_id, username, name):
    try:
        async with async_sessionmaker() as session:
            await session.merge(Users(telegram_id=telegram_id, username=username, name=name))
            await session.commit()
    except IntegrityError:
        return True


async def select_all_users():
    array = []
    try:
        async with async_sessionmaker() as session:
            sql = select(Users.telegram_id)
            result = await session.execute(sql)
            for row in result.scalars():
                array.append(row)
        return array
    except IntegrityError:
        return True
