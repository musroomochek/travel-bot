from aiogram.dispatcher.filters.state import State, StatesGroup


class GetMessage(StatesGroup):
    city = State()
