from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.hobby import Places


async def add_place(category, picture, description, link):
    try:
        async with async_sessionmaker() as session:
            await session.merge(Places(category=category, picture=picture, description=description, link=link))
            await session.commit()
    except IntegrityError:
        return True


async def select_place(category):
    array = []
    async with async_sessionmaker() as session:
        sql = select(Places).where(Places.category == category)
        result = await session.execute(sql)
        for row in result.scalars():
            array.append(f'{row.picture}|{row.description}|{row.link}')
    return array
