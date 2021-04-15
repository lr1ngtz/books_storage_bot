import telebot

# token must be always hidden, that's why we take
# the token from hidden file
TOKEN = None
with open('token.txt') as f:
    TOKEN = f.read().strip()


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    bot.send_message(
        message.chat.id,
        f'Hi {message.from_user.first_name}, I am books_storage_bot.\n\n'
        f'/books - will print the list of all files.'
    )


@bot.message_handler(commands=['books'])
def books_command(message):
    pass


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
            bot.send_message(
                message.from_user.id,
                f'{message.text}, let\'s try in english, pls.\n'
                f' If you want to see a list of all files please use /books.'
            )
        else:
            bot.send_message(
                message.from_user.id,
                f'{message.text}, If you want to see a list of all files please use /books.'
            )
    else:
        bot.send_message(
            message.from_user.id,
            'Unfortunately I can only greet you and show'
            ' you all files if you use /books.'
        )


bot.polling(none_stop=True, interval=0)
