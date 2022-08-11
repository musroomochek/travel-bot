from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_calm = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='Музей', callback_data='go_museums'),
                                   ],
                                   [
                                       InlineKeyboardButton(text='Кино', callback_data='go_cinema')
                                   ],
                                   [
                                       InlineKeyboardButton(text='Театр', callback_data='go_theater')
                                   ],

                                   [
                                       InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                   ]
                               ])
