import telebot
import re
from flask import Flask
import threading
import os
from supabase import create_client, Client

# --- Supabase Setup ---
# URL နဲ့ Key ကို အဟောင်းအတိုင်း ပြန်သုံးထားပါတယ်
SUPABASE_URL = "https://onenfdaddikacglvayvg.supabase.co"
SUPABASE_KEY = "sb_publishable_H4vO1GVW223MHhBz6wxTvA_g6rd9o2J"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

TOKEN = '8562810091:AAGhEOMmuNmuy_g5towNjmt2i3sFwkLuXU0'
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Online!"

def save_user(message):
    """User အချက်အလက်ကို calc_users table ထဲ သိမ်းမယ်"""
    try:
        user_id = message.from_user.id
        username = message.from_user.username or "No Username"
        data = {"user_id": user_id, "username": username}
        # Table နာမည်ကို calc_users လို့ ပေးထားပါတယ်
        supabase.table("calc_users").upsert(data).execute()
    except Exception as e:
        print(f"DB Error: {e}")

@bot.message_handler(commands=['start'])
def start(message):
    save_user(message) # User ကို database ထဲမှတ်မယ်
    bot.reply_to(message, "သင်္ချာပုစ္ဆာတစ်ခုခု ရိုက်ထည့်လိုက်ပါ (ဥပမာ- 1+1)")

@bot.message_handler(commands=['stats'])
def show_stats(message):
    """User အရေအတွက်ကို Bot ထဲမှာတင် စစ်ကြည့်ဖို့ command"""
    try:
        response = supabase.table("calc_users").select("*", count="exact").execute()
        count = response.count
        bot.reply_to(message, f"📊 Calculator Bot အသုံးပြုသူ စုစုပေါင်း: {count} ယောက် ရှိပါတယ်။")
    except Exception as e:
        bot.reply_to(message, "Error: စာရင်းယူလို့ မရနိုင်သေးပါ။")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    save_user(message) # စာရိုက်တိုင်း User ကို database ထဲ update လုပ်မယ်
    try:
        match = re.search(r'(\d+[\+\-\*//]\d+)', message.text)
        if match:
            expression = match.group(1)
            # Eval မသုံးခင် လုံခြုံရေးအရ ဂဏန်းနဲ့ လက္ခဏာပဲ ပါတာ သေချာအောင် စစ်တာပိုကောင်းပါတယ်
            answer = eval(expression)
            bot.reply_to(message, f"ရလဒ်: {answer}")
    except:
        pass

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    threading.Thread(target=run).start()
    print("Calculator Bot is starting...")
    bot.infinity_polling()
