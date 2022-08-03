from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_back = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='назад', callback_data='back'),
                                   ]
                               ])
