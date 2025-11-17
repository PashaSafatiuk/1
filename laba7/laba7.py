import os
from dotenv import load_dotenv
import telebot

# Завантажуємо токен з .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

# Ехо-функція: бот надсилає назад те, що отримав
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

print(TOKEN)
bot.infinity_polling()
