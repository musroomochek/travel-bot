from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.cities import array
from keyboards.inline.hobby_keyboard import hobby
from loader import dp
from states.select_city import GetMessage


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    """
    Переменная <msg> нам нужна для получения message_id в переменную <message_id>
    Переменная <state>, в ней мы получаем состояние пользователя на данный момент
    <state.set_state> используется для обозначения нового состояния для пользователя (в нашем случае GetMessage.city)
    <state.update_data> необходима нам для добавления информации в наше состояние (в нашем случае id сообщения)
    """
    msg = await message.answer(f'<b>Привет, {message.from_user.first_name}!</b>\n\n'
                               f'Нечем заняться на досуге? <b>Я тебе помогу!</b>\n\n'
                               f'Для начала введи свой город :)')

    message_id = msg.message_id
    state = dp.current_state(chat=message.chat.id, user=message.chat.id)
    await state.set_state(GetMessage.city)
    await state.update_data(
        {
            'message_id': message_id
        }
    )


@dp.message_handler(state=GetMessage.city)
async def get_city_from_user(message: types.Message, state: FSMContext):
    """
    Переменная <data> нам необходима для того, чтобы получить информацию, которую мы вносили (в нашем случае id сообщения)
    Переменную <message_id> мы получаем из нашей переменной <data>, воспользовавшись методом <get()>,
    в которой указываем ключ для словаря, по которому мы ищем информацию.

    <await dp.bot.delete_message()> необходим для удаления сообщения у пользователя принимает в себя два значения:
    - message_id - id сообщения
    - chat_id - id чата с пользователем

    <await message.delete> удаляет сообщение пользователя (в нашем случае город)
    """

    data = await state.get_data()
    message_id = data.get('message_id')
    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message_id
    )
    await message.delete()
    city = message.text
    if city.title() in array:
        await message.answer(f'Хорошо, твой город - <b>{city.title()}</b>\n\n'
                             f'Выбери на клавиатуре свой интерес.', reply_markup=hobby)
        await state.reset_state()

    else:
        await message.answer('Такого города не существует.\n'
                             'Попробуй еще раз.')
