import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID

def info(update, context):
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
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp


from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################
def start(update, context):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Option 1', callback_data='m1')],
              [InlineKeyboardButton('Option 2', callback_data='m2')],
              [InlineKeyboardButton('Option 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

############################# Handlers #########################################
updater = Updater('YOUR_TOKEN_HERE', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

updater.start_polling()
