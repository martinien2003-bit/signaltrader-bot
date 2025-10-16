import telebot
import time
from tradingview_ta import TA_Handler, Interval, Exchange

# === Configuration du bot Telegram ===
TOKEN = "8316897859:AAHmXr5diMPjS4lL7kMiRrKQcnk0WeXl0Pg"  # Ton token de bot
bot = telebot.TeleBot(TOKEN)

# === Configuration de l'analyse TradingView ===
analyse = TA_Handler(
    symbol="AUDCAD",
    screener="forex",
    exchange="FX_IDC",   # Marché Forex
    interval=Interval.INTERVAL_5_MINUTES  # Analyse toutes les 5 minutes
)

# === Fonction pour obtenir le signal TradingView ===
def get_signal():
    try:
        result = analyse.get_analysis()
        signal = result.summary
        recommendation = signal.get('RECOMMENDATION', 'UNKNOWN')
        return recommendation
    except Exception as e:
        return f"Erreur d’analyse : {e}"

# === Commande /start ===
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🤖 Bot d’analyse TradingView activé pour AUD/CAD OTC !")
    bot.reply_to(message, "Je vais te donner une recommandation toutes les 5 minutes 📊")

    while True:
        signal = get_signal()
        bot.send_message(message.chat.id, f"📈 Recommandation actuelle pour AUD/CAD : {signal}")
        time.sleep(300)  # toutes les 5 minutes

# === Lancement du bot ===
print("✅ Bot lancé et connecté à Telegram...")
bot.polling(non_stop=True)
# === Commande /start ===
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🚀 Analyse TradingView activée pour AUD/CAD OTC !")
    signal = get_signal()
    bot.send_message(message.chat.id, f"📊 Signal actuel : {signal}")

# === Boucle principale ===
while True:
    try:
        signal = get_signal()
        print(f"Signal TradingView : {signal}")
        time.sleep(300)  # met à jour toutes les 5 minutes
    except Exception as e:
        print(f"Erreur : {e}")
        time.sleep(60)
