import telebot
import time
from background import keep_alive  # импорт функции для поддержки работоспособности
import subprocess
import random

subprocess.Popen(['python3', 'banword.py'])

TOKEN = '6014563918:AAHCgSrapD91i7Mj5bFm0tKyEMpZgBlDSZk'

bot = telebot.TeleBot(TOKEN)

counter = 0
stopped = True

@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.type != 'private':
		global stopped
		stopped = False
		while not stopped:
			bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAI-mmQxFQ5Nh_6eH1Q2Twy6Bv-i-DOBAAJ0AgACv4lgRqs4lF4N46YTLwQ")
			bot.send_message(message.chat.id, "Дуров лапочка")
			time.sleep(random.randint(5, 7))
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

# Запускаем бота
keep_alive()
bot.polling(none_stop=True, interval=0)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)