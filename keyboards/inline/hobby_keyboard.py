from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hobby = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[

                                 [
                                     InlineKeyboardButton(text="Активный отдых", callback_data='active'),
                                 ],
                                 [
                                     InlineKeyboardButton(text='Спокойный отдых', callback_data='calm'),
                                 ],
                             ])
