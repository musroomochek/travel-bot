from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.hobby_keyboard import hobby
from loader import dp
from utils.db_api.commands.users_cmd import add_user


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):

    await add_user(
        telegram_id=message.chat.id,
        username=message.from_user.username,
        name=message.from_user.first_name
    )
    await message.answer(f'<b>Привет, {message.from_user.first_name}!</b>\n\n'
                         f'Нечем заняться на досуге? <b>Я тебе помогу!</b>\n\n'
                         f'Выбери тип отдыха :)', reply_markup=hobby)
