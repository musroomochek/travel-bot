from aiogram.dispatcher.filters.state import State, StatesGroup


class GetMessage(StatesGroup):
    info = State()
