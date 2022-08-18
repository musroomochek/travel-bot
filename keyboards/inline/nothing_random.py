from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def noting_random(link):
    go_nothing = InlineKeyboardMarkup(row_width=3,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Подробнее', url=link)
                                          ],
                                          [
                                              InlineKeyboardButton(text='Назад', callback_data='in_menu')
                                          ],
                                      ])
    return go_nothing