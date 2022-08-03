from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.start import start_cmd
from keyboards.inline.back import go_back
from loader import dp


@dp.callback_query_handler(Text(equals='walking'))
async def show_walking(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Вот места которые могут быть вам интересны!', reply_markup=go_back)


@dp.callback_query_handler(Text(equals='museums'))
async def show_museums(call: types.CallbackQuery):
    await call.message.edit_text('Вот музеи которые могут быть вам интересны!')


@dp.callback_query_handler(Text(equals='back'))
async def go_back_in_menu(call: types.CallbackQuery):
    await call.message.delete()
    await start_cmd(message=call.message)
