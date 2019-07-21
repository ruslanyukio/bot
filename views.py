import telebot

bot = telebot.TeleBot("670299637:AAFm_IQBb4H0AQtGXwNjO_F_vlhEZ1XQuac")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.polling( none_stop = True )