from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='TEST', callback_data='empty')
                                ]
                            ])