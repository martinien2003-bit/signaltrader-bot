import telebot
import random
import time

# Remplace par TON token de bot Telegram
TOKEN = "8316897859:AAHmXr5diMPjS41L6nihI3jeLfmp5gvgGrI"
bot = telebot.TeleBot(TOKEN)

# Liste de signaux automatiques (tu peux modifier ou ajouter)
signaux = [
    {"actif": "AUD/CAD OTC", "type": "CALL", "temps": 2},
    {"actif": "AUD/CAD OTC", "type": "PUT", "temps": 2}
]
    
    
    



# Quand on envoie /start, le bot démarre et envoie des signaux automatiquement
@bot.message_handler(commands=['start'])
def start_signaux(message):
    bot.send_message(message.chat.id, "🚀 Bienvenue sur ton bot de signaux Pocket Option !")
    bot.send_message(message.chat.id, "📡 Envoi automatique de signaux toutes les 2 minutes...")

    # Envoi automatique de signaux
    for i in range(10):  # 10 signaux
        signal = random.choice(signaux)
        bot.send_message(message.chat.id, f"Signal {i+1} : {signal}")
        time.sleep(120)  # 2 minutes entre chaque signal

    bot.send_message(message.chat.id, "✅ Série de signaux terminée !")

# Démarrer le bot
bot.polling()
