import telebot
import time
import random

TOKEN = '6161165770:AAGfwxooA3C4grNrEuWTYsKuOmel4mW54D8'

bot = telebot.TeleBot(TOKEN)

counter = 0
stopped = True

@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.type != 'private':
		global stopped
		stopped = False
		while not stopped:
			bot.send_message(message.chat.id, "Хахтикс лапочка")
			time.sleep(random.randint(3, 5))
	else:
		bot.send_message(message.chat.id, "Иди нахуй")
				

@bot.message_handler(commands=['stop'])
def stop(message):
    global stopped
    stopped = True

@bot.message_handler(commands=['check'])
def check(message):
    with open('message.txt', 'r') as f:
        counter = int(f.read())
    bot.send_message(message.chat.id, f"Количество сообщений: {counter}")

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)