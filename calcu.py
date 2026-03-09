import telebot

# Bot Token ကို ဒီမှာ ထည့်ပါ
TOKEN = '8562810091:AAF774c8Es0zv0nGRSQ1xIZjZqhvd3LPh7I'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "သင်္ချာပုစ္ဆာတစ်ခုခု ရိုက်ထည့်လိုက်ပါ (ဥပမာ- 1+1)")

import telebot
import re

TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # User ပို့တဲ့စာထဲကနေ ဂဏန်းတွေနဲ့ သင်္ကေတ (+, -, *, /) တွေကိုပဲ ရှာထုတ်မယ်
        expression = "".join(re.findall(r'[0-9+\-*/.]+', message.text))
        
        if expression:
            # ထုတ်ယူထားတဲ့ သင်္ချာပုစ္ဆာကို တွက်မယ်
            answer = eval(expression)
            # မူရင်းစာသား = အဖြေ ပုံစံနဲ့ ပြန်ဖြေမယ်
            bot.reply_to(message, f"{message.text} = {answer}")
        else:
            bot.reply_to(message, "တွက်ချက်ဖို့ ဂဏန်းရှာမတွေ့ပါဘူး။")
            
    except Exception:
        bot.reply_to(message, "တွက်လို့မရတဲ့ format ဖြစ်နေပါတယ်။")

print("Bot is running...")
bot.infinity_polling()
