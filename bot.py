# bot.py
import os
import telebot
from dotenv import load_dotenv
from utils import get_daily_horoscope

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No Telegram Bot Token provided in the environment variables.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = ("What's your zodiac sign?\n"
            "Choose one: *Aries*, *Taurus*, *Gemini*, *Cancer*, *Leoo*, *Virgo*, "
            "*Libra*, *Scorpio*, *Sagittarious*, *Capricorn*, *Aquarius*, and *Pisces*.")
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    sign = message.text
            "Choose one: *Present*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD.")
    text = ("What do you want to know?\n"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())

def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
