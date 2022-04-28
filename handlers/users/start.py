from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.startInline import langMenu, mainMenu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    msg = 'Добро пожаловать в телеграм бот Azia.uz. Тут вы можете узнать баланс карты, получить информацию о скидках и акциях.'
    await message.answer(msg)
    # await message.answer_contact('Отаправьте свой контакт что б мы могли придоставить вам заказ', )
    await message.reply_contact(9869486, 'fist name')
    await message.answer('Меню', reply_markup=mainMenu)
