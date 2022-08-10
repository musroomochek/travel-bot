import sqlalchemy.orm
from sqlalchemy import Column, Integer, String

from utils.db_api.base import Base


class Places(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)

    category = Column(String)
    picture = Column(String)
    description = Column(String)
    link = Column(String)

    query: sqlalchemy.orm.Query
