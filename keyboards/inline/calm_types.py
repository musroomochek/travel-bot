from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_calm = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='Музей', callback_data='museums'),
                                   ],
                                   [
                                       InlineKeyboardButton(text='Кино', callback_data='cinema')
                                   ],
                                   [
                                       InlineKeyboardButton(text='Театр', callback_data='theater')
                                   ],

                                   [
                                       InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                   ]
                               ])
