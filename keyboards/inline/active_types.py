from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_active = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='прогулка', callback_data='walking'),
                                 ],
                                 [
                                     InlineKeyboardButton(text='физическая нагрузка', callback_data='pphysical'),
                                 ],
                                 [
                                     InlineKeyboardButton(text='назад', callback_data='in_menu')
                                 ],
                                 ])
