import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID
var TelegramBot = require('My_favorit_new_client');
var bot = new TelegramBot(telegramToken, { polling: true });
bot.on("polling_error", (m) => console.log(m));
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


bot.sendMessage(clientId, 'Привет, хабр!', messageOptions);
var messageOptions = {
    parse_mode: "HTML",
    disable_web_page_preview: false,
    reply_markup: JSON.stringify({
        inline_keyboard: [[{
            text: 'Название кнопки',
            callback_data: 'do_something'
        }]]
    })
}
bot.onText(new RegExp('\/start'), function (message, match) {
    // вытаскиваем id клиента из пришедшего сообщения
    var clientId = message.hasOwnProperty('chat') ? message.chat.id : message.from.id;
    // посылаем ответное сообщение
    bot.sendMessage(clientId, 'Some message', messageOptions);
});
bot.on('callback_query', function (message) {
    var clientId = message.hasOwnProperty('chat') ? message.chat.id : message.from.id;
    // То что мы записали в callback_data у кнопок приходит в message.data
    if(message.data === 'do_something'){
        bot.sendMessage(clientId, 'Button clicked!', messageOptions);
    }
});
function buildDefaultButton(text, callback_data) {
    return [{
        text: text,
        callback_data: callback_data
    }]
}

function buildUrlButton(text, url) {
    return [{
        text: text,
        url: url
    }]
}

function buildShareButton(text, shareUrl) {
    return [{
        text: text,
        url: 'https://telegram.me/share/url?url=' + shareUrl
    }]
}

function buildMessageOptions(buttons) {
    return {
        parse_mode: "HTML",
        disable_web_page_preview: false,
        reply_markup: JSON.stringify({
            inline_keyboard: buttons
        })
    }
}
var buttons = [
    botUtils.buildDefaultButton('Кнопка', 'button1'),
    botUtils.buildShareButton('Поделиться', 'url'),
    botUtils.buildUrlButton('Ссылка', 'link')
];

var messageOptions = botUtils.buildMessageOptions(buttons);
