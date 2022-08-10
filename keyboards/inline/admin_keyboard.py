from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Добавить новое место', callback_data='add_place')
                                 ]
                             ])