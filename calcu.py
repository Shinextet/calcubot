import telebot
import re

TOKEN = '8562810091:AAF774c8Es0zv0nGRSQ1xIZjZqhvd3LPh7I' # ဒီနေရာမှာ သင့် Bot Token ထည့်ပါ
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "သင်္ချာပုစ္ဆာတစ်ခုခု ရိုက်ထည့်လိုက်ပါ (ဥပမာ- 1+1)")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        text = message.text
        # သင်္ချာလက္ခဏာ (+, -, *, /) ရဲ့ ရှေ့နဲ့နောက်မှာရှိတဲ့ ဂဏန်းတွေကို ရှာတဲ့ Regular Expression
        # ဥပမာ - 5750*2 ဆိုတာကို ရှာထုတ်ပေးမှာပါ
        match = re.search(r'(\d+[\+\-\*//]\d+)', text)
        
        if match:
            expression = match.group(1)
            # ရှာတွေ့တဲ့ အပိုင်းကိုပဲ တွက်ချက်မယ်
            answer = eval(expression)
            bot.reply_to(message, f"ရလဒ်: {answer}")
        else:
            bot.reply_to(message, "တွက်ချက်ဖို့ သင်္ချာပုံစံ (ဥပမာ 1*2) ရှာမတွေ့ပါဘူး။")
            
    except Exception:
        bot.reply_to(message, "တွက်ချက်မှု မှားယွင်းနေပါတယ်။")

bot.infinity_polling()
