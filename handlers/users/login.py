from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('login'))
async def login_cmd(message: types.Message):
    await message.answer('Вы успешно авторизовались')
