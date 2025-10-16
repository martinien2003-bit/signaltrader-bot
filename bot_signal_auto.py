import telebot
import time
from tradingview_ta import TA_Handler, Interval, Exchange

# Ton token de bot Telegram
TOKEN = "8316897859:AAHmXr5diMPjS41L6nihI3jeLfmp5gvgGrI"
bot = telebot.TeleBot(TOKEN)

# Configuration de l'analyse TradingView
analyse = TA_Handler(
    symbol="AUDCAD",
    screener="forex",
    exchange="FX_IDC",
    interval=Interval.INTERVAL_2_MINUTES  # Analyse toutes les 2 minutes
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔍 Analyse en cours sur AUD/CAD (TradingView)...")
    while True:
        try:
            data = analyse.get_analysis()
            signal = data.summary["RECOMMENDATION"]

            if signal == "STRONG_BUY" or signal == "BUY":
                msg = "📈 SIGNAL: CALL (Achat) sur AUD/CAD OTC"
            elif signal == "STRONG_SELL" or signal == "SELL":
                msg = "📉 SIGNAL: PUT (Vente) sur AUD/CAD OTC"
            else:
                msg = "⚖️ SIGNAL: Neutre, pas d'entrée maintenant"

            bot.send_message(message.chat.id, msg)
            time.sleep(120)  # Attend 2 minutes avant la prochaine analyse

        except Exception as e:
            bot.send_message(message.chat.id, f"Erreur: {e}")
            time.sleep(60)

bot.polling()
