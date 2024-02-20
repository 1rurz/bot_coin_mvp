from aiogram.types import( 
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "coin price" ),
            InlineKeyboardButton(text="share price "),
        ],
        [
            InlineKeyboardButton(text="help the project"),
            InlineKeyboardButton(text="useful links")
        ],
    ]
)



indo_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton (text="tg", url="https://t.me/cryptostock_and_stock"),
        ]
    ],
    resize_keyboard=True,
)




