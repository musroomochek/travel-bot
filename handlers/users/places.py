from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.callback_query_handler(Text(equals='walking'))
async def show_walking(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Вот ваши локации')
