from aiogram import types

from keyboards.inline.startInline import mainMenu

from loader import dp


@dp.callback_query_handler(text="about")
async def about_bot(call: types.CallbackQuery):
    msg = 'Используя этот бот Вы можете отслеживать ваш баланс карты лояльности в сети супермаркетов Azia.uz, а также быть в курсе новых акций и событий сети Корзинка.\n\nВсе права защищены ИП ООО "Anglesey Food"'
    logo = 'https://yt3.ggpht.com/iMymvKy9AC0c9Tp8Pp2vtqzsn3GLVkkVfjp9ayyL7sxPkkJv4g7flzZvJjEdqqOUns6tBpJM=s900-c-k-c0x00ffffff-no-rj'
    await call.message.answer_photo(logo, msg, reply_markup=mainMenu)
    await call.message.delete()
    await call.answer(cache_time=60)
    # await message.answer('Tilni tanlang / Выберите язык', reply_markup=startMenu)
