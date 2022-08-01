from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.cities import array
from keyboards.inline.hobby_keyboard import hobby
from loader import dp
from states.select_city import GetMessage


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'<b>Привет, {message.from_user.first_name}!</b>\n\n'
                         f'Нечем заняться на досуге? <b>Я тебе помогу!</b>\n\n'
                         f'Для начала введи свой город :)')
    await GetMessage.city.set()


@dp.message_handler(state=GetMessage.city)
async def get_city_from_user(message: types.Message, state: FSMContext):
    city = message.text
    if city.title() in array:
        await message.answer(f'Хорошо, твой город - <b>{city.title()}</b>\n\n'
                             f'Выбери на клавиатуре свой интерес.', reply_markup=hobby)
        await state.reset_state()

    else:
        await message.answer('Такого города не существует.\n'
                             'Попробуй еще раз.')
