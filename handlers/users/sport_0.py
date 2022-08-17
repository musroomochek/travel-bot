from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.sport import sport
from loader import dp


@dp.callback_query_handler(Text(equals='physical'))
async def show_active(call: types.CallbackQuery):
    await call.message.edit_text('Супер! Выберете вид активного отдыха!', reply_markup=sport)
