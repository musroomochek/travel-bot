from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.commands.places_cmd import get_categories, get_description

admin = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Рассылка', callback_data='mailing')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Добавить новое место', callback_data='add_place')
                                 ],
                                 [
                                     InlineKeyboardButton(text='Удалить место', callback_data='delete_place')
                                 ]
                             ])


async def categories_kb():
    categories = InlineKeyboardMarkup(row_width=3)

    data = await get_categories()

    for row in data:
        btn = InlineKeyboardButton(text=row, callback_data=f'del_{row}')
        categories.add(btn)

    return categories


async def description_kb(category):
    data = await get_description(category)

    desc = InlineKeyboardMarkup(row_width=3)

    for row in data:
        btn = InlineKeyboardButton(text=row, callback_data=f'get_{row}')
        desc.add(btn)

    return desc
