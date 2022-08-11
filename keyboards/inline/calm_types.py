from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_calm = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='Музей', callback_data='go_museums_0'),
                                   ],
                                   [
                                       InlineKeyboardButton(text='Кино', callback_data='go_cinema_0')
                                   ],
                                   [
                                       InlineKeyboardButton(text='Театр', callback_data='go_theater_0')
                                   ],

                                   [
                                       InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                   ]
                               ])
