from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def pagination_keyboard(list_id, link, category):
    pagination = InlineKeyboardMarkup(row_width=5,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Подробнее', url=link)
                                          ],
                                          [
                                              InlineKeyboardButton(text='<-', callback_data=f'go_{category}_{list_id - 1}'),
                                              InlineKeyboardButton(text='Назад', callback_data='back'),
                                              InlineKeyboardButton(text='->', callback_data=f'go_{category}_{list_id + 1}')
                                          ]
                                      ])

    return pagination
