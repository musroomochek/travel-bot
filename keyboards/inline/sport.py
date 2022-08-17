from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sport=InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Велопрогулка', callback_data='go_bike_0')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Плавание', callback_data='go_swim_0')
                                     ]

                                     ])