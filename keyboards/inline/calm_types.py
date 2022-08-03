from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_calm = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='музей', callback_data='museums'),
                                   ],
                                   [
                                       InlineKeyboardButton(text='кино', callback_data='cinema')
                                   ],
                                   [
                                       InlineKeyboardButton(text='театр', callback_data='theater')
                                   ],

                                   [
                                       InlineKeyboardButton(text='назад', callback_data='in_menu')
                                   ]
                               ])
