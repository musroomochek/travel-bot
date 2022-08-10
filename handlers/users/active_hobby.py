from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.link_keyboard import link_kb
from loader import dp
from utils.db_api.commands.places_cmd import select_place


@dp.callback_query_handler(Text(equals='walking'))
async def show_active_walking(call: types.CallbackQuery):
    info = await select_place('walking')
    data = info[0].split('|')
    photo_link = data[0]
    keyboard = await link_kb(data[2])

    await call.message.answer_photo(
        photo=photo_link,
        caption=f'Описание места:\n'
                f'{data[1]}',
        reply_markup=keyboard
    )
