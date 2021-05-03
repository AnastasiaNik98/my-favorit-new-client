import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = os.getenv("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "👋")

@My_favorit_new_client(commands=['info', 'help'])
def category(message):
    keyboard_category = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_1_1 = types.KeyboardButton('1_1')
    keyboard_category.add(key_1_1)

    bot.reply_to(message, "Привет! Я помогу подобрать товар!", reply_markup=keyboard_category)


@My_favorit_new_client(content_types=['text'])
def subcategory(message):
    if message.text == "1_1":
        keyboard_subcategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_2_1 = types.KeyboardButton('2_1')
        keyboard_subcategory.add(key_2_1)  # key_2_1 не использовалась

        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=keyboard_subcategory)

    elif message.text == "2_1":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('3_1')
        keyboard_tovar.add(key_3_1)  # key_3_1 не использовалась

        bot.send_message(message.chat.id, 'Выберите товар по названию и я пришлю вам подробности',
                         reply_markup=keyboard_tovar)

    elif message.text == "3_1":  # потеряли двоеточие
        bot.send_message(message.chat.id, "Описание товара")
        bot.send_photo(message.chat.id, 'https://cs13.pikabu.ru/images/big_size_comm/2020-06_3/159194100716237333.jpg')  # просто укажите ссылку на картинку


bot.polling()
