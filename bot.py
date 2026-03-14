import os
import telebot
import google.generativeai as genai

# Logs: Nbdawo l-khdma
print("--- Start Script ---")

try:
    # Configuration
    print("Configuring Gemini...")
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-1.5-flash')

    BOT_TOKEN = os.environ['BOT_TOKEN']
    CHANNEL_ID = os.environ['CHANNEL_ID']
    bot = telebot.TeleBot(BOT_TOKEN)
    print("Telegram Bot configured.")

    # 1. Jib l-adkar men Gemini
    print("Requesting Adkar from Gemini...")
    prompt = """
    أعطني رسالة منظمة للأذكار بنفس التنسيق تماماً:
    📿 تسبيح
    اسم التسبيح ×33
    اسم التسبيح ×33
    اسم التسبيح ×34
    💎 دقيقة واحدة من وقتك قد تكون سببًا في رفعة درجتك عند الله.
    🤲 دعاء
    (دعاء قصير)
    ملاحظة: لا تستخدم رمز ✨ ولا تضف مقدمات.
    """
    response = model.generate_content(prompt)
    adkar_text = response.text
    print(f"Adkar generated successfully:\n{adkar_text}")

    # 2. Sift l-adkar l-Telegram
    print(f"Attempting to post to Channel ID: {CHANNEL_ID}...")
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Adkar posted to Telegram!")

except Exception as e:
    print(f"❌ ERROR: Something went wrong: {e}")

print("--- End Script ---")
