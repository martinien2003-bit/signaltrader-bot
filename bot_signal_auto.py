import telebot
import random
from flask import Flask, request

# Ton token ici
TOKEN = TOKEN = "8316897859:AAHmXr5diMPjS41L6nihI3jeLfmp5gvgGrI"

bot = telebot.TeleBot(TOKEN)

# App Flask pour Render
app = Flask(__name__)

# Liste des paires
pairs = ["AUD/CAD OTC", "EUR/USD OTC", "USD/JPY OTC", "GBP/USD OTC"]

# Commande /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for pair in pairs:
        markup.add(pair)
    bot.send_message(message.chat.id, "👋 Bienvenue sur le bot de signaux !\nChoisis une paire pour analyser :", reply_markup=markup)

# Quand l’utilisateur clique sur une paire
@bot.message_handler(func=lambda message: message.text in pairs)
def send_signal(message):
    signal_type = random.choice(["BUY SIGNAL 🚀", "SELL SIGNAL 🔻"])
    bot.send_message(
        message.chat.id,
        f"{signal_type}\n📊 {message.text}\nEnter NOW 🔥"
    )

# Flask route pour Render (obligatoire)
@app.route("/")
def index():
    return "Bot en ligne !"

# Lancer le bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
