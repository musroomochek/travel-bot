from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("menue"))
async def menue_cmd(message: types.Message):
    await message.answer("вы попали в меню")