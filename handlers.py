import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID

def start(update, context):
    update.message.reply_text(WELCOME_MESSAGE)

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"""
📞 Connected {user_info}.
        """,
    )


def forward_to_chat(update, context):
    """{ 
        'message_id': 5, 
        'date': 1605106546, 
        'chat': {'id': 49820636, 'type': 'private', 'username': 'danokhlopkov', 'first_name': 'Daniil', 'last_name': 'Okhlopkov'}, 
        'text': 'TEST QOO', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


def forward_to_user(update, context):
    """{
        'message_id': 10, 'date': 1605106662, 
        'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
        'reply_to_message': {
            'message_id': 9, 'date': 1605106659, 
            'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
            'forward_from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'danokhlopkov': 'okhlopkov', 'language_code': 'en'}, 
            'forward_date': 1605106658, 
            'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 
            'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
            'from': {'id': 1440913096, 'first_name': 'SUPPORT', 'is_bot': True, 'username': 'lolkek'}
        }, 
        'text': 'ggg', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 
        'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    user_id = update.message.reply_to_message.forward_from.id
    context.bot.copy_message(
        message_id=update.message.message_id,
        chat_id=user_id,
        from_chat_id=update.message.chat_id
    )


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp

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
