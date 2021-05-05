var TelegramBot = require('node-telegram-bot-api');
var bot = new TelegramBot(telegramToken, { polling: true });
bot.on("polling_error", (m) => console.log(m));
bot.sendMessage('Привет, хабр!', messageOptions);
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
    bot.sendMessage('Some message', messageOptions);
});


bot.on('callback_query', function (message) {
    var clientId = message.hasOwnProperty('chat') ? message.chat.id : message.from.id;
    // То что мы записали в callback_data у кнопок приходит в message.data
    if(message.data === 'do_something'){
        bot.sendMessage(clientId, 'Button clicked!', messageOptions);
    }
});
var buttons = [
    botUtils.buildDefaultButton('Кнопка', 'button1'),
    botUtils.buildShareButton('Поделиться', 'url'),
    botUtils.buildUrlButton('Ссылка', 'link')
];

var messageOptions = botUtils.buildMessageOptions(buttons);
