from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_active = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Прогулка', callback_data='go_walking'),
                                     ],
                                     [
                                         InlineKeyboardButton(text='Физическая нагрузка', callback_data='go_physical'),
                                     ],
                                     [
                                         InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                     ],
                                 ])
