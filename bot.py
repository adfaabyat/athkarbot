import os
import telebot
import google.generativeai as genai

# Logs: بداية التشغيل
print("--- Start Script ---")

try:
    # إعداد Gemini
    print("Configuring Gemini...")
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-2.5-flash')

    # إعداد التليجرام
    BOT_TOKEN = os.environ['BOT_TOKEN']
    CHANNEL_ID = os.environ['CHANNEL_ID']
    bot = telebot.TeleBot(BOT_TOKEN)
    print("Telegram Bot configured.")

    # 1. طلب الأذكار مع تنسيق المسافات الجديد
    print("Requesting Adkar from Gemini...")
    prompt = """
    أعطني رسالة منظمة للأذكار بنفس التنسيق التالي تماماً مع ضرورة ترك سطر فارغ بين كل قسم:

    📿 (اسم القسم مثلاً: استغفار أو تسبيح)
    
    اسم الذكر الأول
    اسم الذكر الثاني
    اسم الذكر الثالث
    اسم الذكر الرابع
    
    💎 ذكر بسيط… وأجر عظيم

    ملاحظات هامة:
    1. اترك سطراً فارغاً بعد العنوان (الذي بجانبه مسبحة).
    2. اترك سطراً فارغاً قبل الجملة الختامية (ذكر بسيط...).
    3. لا تستخدم الرمز ✨ نهائياً.
    4. لا تضف أي مقدمات مثل "إليك الأذكار" أو "تم التوليد".
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text
    print(f"Adkar generated successfully:\n{adkar_text}")

    # 2. إرسال الرسالة
    print(f"Attempting to post to Channel ID: {CHANNEL_ID}...")
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Adkar posted to Telegram!")

except Exception as e:
    print(f"❌ ERROR: Something went wrong: {e}")

print("--- End Script ---")
