from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.callback_query_handler(Text(equals='walking'))
async def show_walking(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Вот места которые могут быть вам интерессны!')



@dp.callback_query_handler(Text(equals='museums'))
async def show_museums(call: types.CallbackQuery):
    await call.message.edit_text('Вот музеи которые могут быть вам интерессны!')