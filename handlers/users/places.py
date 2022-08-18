import random

from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.start import start_cmd
from keyboards.inline import nothing_random
from keyboards.inline.active_types import go_active
from keyboards.inline.calm_types import go_calm
from keyboards.inline.hobby_keyboard import hobby
from keyboards.inline.nothing_random import noting_random
from loader import dp
from utils.db_api.commands.places_cmd import select_all_places


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
    await call.message.delete()
    await call.message.answer('Выбери на клавиатуре свой интерес.', reply_markup=hobby)


@dp.callback_query_handler(Text(equals='nothing'))
async def show_nothing(call: types.CallbackQuery):
    data = await select_all_places()
    current_info = data[
        random.randint(0, len(data) - 1)
    ].split('|')
    keyboard = await noting_random(link=current_info[2])
    await call.message.delete()
    await call.message.answer_photo(
        photo=current_info[0],
        caption=current_info[1],
        reply_markup=keyboard
    )
