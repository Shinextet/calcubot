import telebot
import re
from flask import Flask
import threading
import os

TOKEN = '8562810091:AAF774c8Es0zv0nGRSQ1xIZjZqhvd3LPh7I' # ဒီနေရာမှာ သင့် Token ကို သေချာထည့်ပါ
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Online!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "သင်္ချာပုစ္ဆာတစ်ခုခု ရိုက်ထည့်လိုက်ပါ (ဥပမာ- 1+1)")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # စာသားတွေကြားထဲက ဂဏန်းနဲ့ သင်္ချာလက္ခဏာကိုပဲ ရှာထုတ်မယ်
        # ဥပမာ - 5750*2 ကိုပဲ ဆွဲထုတ်ပါမယ်
        match = re.search(r'(\d+[\+\-\*//]\d+)', message.text)
        if match:
            expression = match.group(1)
            answer = eval(expression)
            bot.reply_to(message, f"ရလဒ်: {answer}")
    except:
        pass

def run():
    # Render အတွက် Port 8080 ကို ဖွင့်ပေးခြင်း
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    # Web server ကို background မှာ run ပြီး Bot ကို စတင်မယ်
    threading.Thread(target=run).start()
    bot.infinity_polling()
