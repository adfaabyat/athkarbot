import os
import telebot
import google.generativeai as genai

# Logs: بداية التشغيل
print("--- Start Script ---")

try:
    # إعداد Gemini 2.5 Flash (الأحدث لعام 2026)
    print("Configuring Gemini 2.5 Flash...")
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-2.5-flash')

    # إعداد التليجرام
    BOT_TOKEN = os.environ['BOT_TOKEN']
    CHANNEL_ID = os.environ['CHANNEL_ID']
    bot = telebot.TeleBot(BOT_TOKEN)
    print("Telegram Bot configured.")

    # 1. طلب الذكر القصير جداً مع المسافات
    print("Requesting Short Adkar from Gemini 2.5 Flash...")
    prompt = """
    أعطني ذكراً أو حديثاً نبوياً قصيراً جداً، بنفس التنسيق التالي تماماً مع ترك سطر فارغ بين كل سطر:

    💎 ذكر عظيم

    قال رسول الله ﷺ:

    "نص الحديث أو الذكر هنا"

    (جملة الفضل أو الأجر هنا باختصار)

    ملاحظات هامة:
    1. اترك سطراً فارغاً بين كل قسم كما في المثال.
    2. لا تستخدم الرمز ✨ نهائياً.
    3. النص يجب أن يكون قصيراً جداً ومؤثراً.
    4. لا تضف أي مقدمات أو خاتمة.
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text
    print(f"Adkar generated successfully:\n{adkar_text}")

    # 2. إرسال الرسالة
    print(f"Attempting to post to Channel ID: {CHANNEL_ID}...")
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Post complete using Gemini 2.5 Flash!")

except Exception as e:
    print(f"❌ ERROR: Something went wrong: {e}")

print("--- End Script ---")
