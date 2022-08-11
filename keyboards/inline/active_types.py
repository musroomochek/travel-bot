from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_active = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Прогулка', callback_data='go_walking_0'),
                                     ],
                                     [
                                         InlineKeyboardButton(text='Физическая нагрузка', callback_data='go_physical_0'),
                                     ],
                                     [
                                         InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                     ],
                                 ])
