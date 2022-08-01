from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("cool"))
async def cool_cmd(message: types.Message):
    await message.answer("ты крутой")