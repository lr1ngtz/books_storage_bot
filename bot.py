import telebot

# token must be always hidden, that's why we take
# the token from hidden file
TOKEN = None
with open('token.txt') as f:
    TOKEN = f.read().strip()


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'books'])
def send_welcome(message):
    bot.reply_to(message, f'Hi {message.from_user.first_name}, I am books_storage_bot.')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    greetings = [
        'hi',
        'hello',
        'hola',
        'привет',
        'здравствуй',
        'guten tag',
        'hallo',
        'こんにちは',
        '你好',
        'cześć',
        'bonjour',
    ]
    if message.text.lower() in greetings:
        if message.text.lower() not in greetings[:2]:
            bot.send_message(message.from_user.id, f'{message.text}, let\'s try in english, pls.')
        else:
            bot.send_message(message.from_user.id, message.text)
    else:
        bot.send_message(message.from_user.id, 'I don\'t understand you.')


bot.polling(none_stop=True, interval=0)
