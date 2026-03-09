import telebot

# Bot Token ကို ဒီမှာ ထည့်ပါ
TOKEN = '8562810091:AAF774c8Es0zv0nGRSQ1xIZjZqhvd3LPh7I'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "သင်္ချာပုစ္ဆာတစ်ခုခု ရိုက်ထည့်လိုက်ပါ (ဥပမာ- 1+1)")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # User ရိုက်တဲ့စာကို တွက်ချက်ခြင်း
        question = message.text
        answer = eval(question)
        
        # ၁+၁=၂ ပုံစံမျိုး ပြန်ဖြေခြင်း
        bot.reply_to(message, f"{question} = {answer}")
    except:
        # မှားယွင်းတာ ရိုက်ရင် ဘာမှပြန်မလုပ်ပါ (သို့မဟုတ် Error ပြပါ)
        bot.reply_to(message, "တွက်လို့မရတဲ့ format ဖြစ်နေပါတယ်")

print("Bot is running...")
bot.infinity_polling()