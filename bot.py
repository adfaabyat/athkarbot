import os
import telebot
import google.generativeai as genai

# Configuration dyal Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-2.5-flash')

# Configuration dyal Telegram
BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']
bot = telebot.TeleBot(BOT_TOKEN)

def get_adkar():
    prompt = "أعطني ذكرين قصيرين من أذكار المسلم (مثلاً تسبيح أو دعاء) مع تشكيل الحروف. اجعل كل ذكر في سطر منفصل وبدون أي مقدمات أو خاتمة."
    response = model.generate_content(prompt)
    return response.text

def main():
    try:
        adkar_text = get_adkar()
        bot.send_message(CHANNEL_ID, adkar_text)
        print("Adkar posted successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
