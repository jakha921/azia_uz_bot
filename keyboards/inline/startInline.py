from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# contact
contact = InlineKeyboardMarkup(row_width=1)
get_contact = InlineKeyboardButton(text='Отправить контакт', callback_data='get_contact', )
contact.insert(get_contact)

# language
langMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿O`zbek tili", callback_data="uzb"),
            InlineKeyboardButton(text="🇷🇺Русский язык", callback_data="rus"),
        ]
    ]
)

# startMenu
mainMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💳Карта лояльности", callback_data="card"),
            InlineKeyboardButton(text="💸Скидки", url='https://t.me/korzinka_uz/12'),
        ],
        [
            InlineKeyboardButton(text="🇺🇿O`zbek tili / 🇷🇺Русский язык", callback_data="lang"),
            
        ],
        [
            InlineKeyboardButton(text="🤖О боте", callback_data="about"),
        ]
    ]
)

