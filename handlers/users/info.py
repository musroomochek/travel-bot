from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("info"))
async def info_command(message: types.Message):
    await message.answer(f" <b> Имя пользователя:</b> {message.from_user.first_name}\n"
                         f" <strong> Фамилия пользователя:</strong> {message.from_user.last_name}\n"
                         f" <i> Ник пользователя:</i> {message.from_user.username}\n"
                         f"<s> ID пользователя:</s>  {message.from_user.id}")