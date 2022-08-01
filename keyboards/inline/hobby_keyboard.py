from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hobby = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Гулять', callback_data='walking'),
                                 ],
                                 [
                                     InlineKeyboardButton(text='Музеи', callback_data='museums')
                                 ]
                             ])
