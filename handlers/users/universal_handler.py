from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.back import go_back
from keyboards.inline.pagination_places import pagination_keyboard
from loader import dp
from utils.db_api.commands.places_cmd import select_place


@dp.callback_query_handler(Text(startswith='go_'))
async def show_active_walking(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data.split('_')[1]
    list_id = call.data.split('_')[2]
    try:
        info = await select_place(data)
        if int(list_id) <= 0:
            list_id = 0

        if int(list_id) >= len(info):
            list_id = 0

        photo_link = info[int(list_id)].split('|')[0]
        desc = info[int(list_id)].split('|')[1]
        link = info[int(list_id)].split('|')[2]

        keyboard = await pagination_keyboard(int(list_id), link=link, category=data)

        await call.message.answer_photo(
            photo=photo_link,
            caption=f'Описание: {desc}',
            reply_markup=keyboard
        )

    except IndexError as error:
        print(error)
        await call.message.edit_text('К сожалению, места с данным выбором пока отсутствуют :(', reply_markup=go_back)
