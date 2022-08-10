from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.start import start_cmd
from keyboards.inline.active_types import go_active
from keyboards.inline.calm_types import go_calm
from keyboards.inline.hobby_keyboard import hobby
from loader import dp


@dp.callback_query_handler(Text(equals='active'))
async def show_active(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Выберете вид активного отдыха!', reply_markup=go_active)


@dp.callback_query_handler(Text(equals='calm'))
async def show_calm(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Выберете вид спокойного отдыха!', reply_markup=go_calm)


@dp.callback_query_handler(Text(equals='back'))
async def go_back_in_menu(call: types.CallbackQuery):
    await call.message.delete()  # удаляем сообщение, чтобы не было ошибок
    await start_cmd(message=call.message)


@dp.callback_query_handler(Text(equals='in_menu'))
async def in_menu(call: types.CallbackQuery):
    await call.message.edit_text('Выбери на клавиатуре свой интерес.', reply_markup=hobby)
