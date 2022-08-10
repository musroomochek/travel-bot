from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hobby = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[

                                 [
                                     InlineKeyboardButton(text="активный отдых", callback_data='active'),
                                 ],
                                 [
                                     InlineKeyboardButton(text='спокойный отдых', callback_data='calm'),
                                 ],
                                 [
                                     InlineKeyboardButton(text='назад', callback_data='back')
                                 ]
                             ])
