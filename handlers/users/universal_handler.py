from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.back import go_back
from keyboards.inline.link_keyboard import link_kb
from loader import dp
from utils.db_api.commands.places_cmd import select_place


@dp.callback_query_handler(Text(startswith='go_'))
async def show_active_walking(call: types.CallbackQuery):
    data = call.data.split('_')[1]
    try:
        info = await select_place(data)
        data = info[0].split('|')
        photo_link = data[0]
        keyboard = await link_kb(data[2])

        await call.message.answer_photo(
            photo=photo_link,
            caption=f'Описание места:\n'
                    f'{data[1]}',
            reply_markup=keyboard
        )
    except IndexError as error:
        print(error)
        await call.message.edit_text('К сожалению, места с данным выбором пока отсутствуют :(', reply_markup=go_back)
