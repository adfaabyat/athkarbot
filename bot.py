import os
import telebot
import google.generativeai as genai
import random

# Logs: بداية التشغيل
print("--- Start Script ---")

try:
    # إعداد Gemini 2.5 Flash
    print("Configuring Gemini 2.5 Flash...")
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-2.5-flash')

    # إعداد التليجرام
    BOT_TOKEN = os.environ['BOT_TOKEN']
    CHANNEL_ID = os.environ['CHANNEL_ID']
    bot = telebot.TeleBot(BOT_TOKEN)
    print("Telegram Bot configured.")

    # مواضيع متنوعة لضمان عدم التكرار
    topics = [
        "ذكر نبوي قصير", "دعاء مستجاب", "حديث عن فضل الذكر",
        "آية قرآنية عن الطمأنينة", "كلمات في حب الله", "استغفار وتسبيح"
    ]
    selected_topic = random.choice(topics)

    # 1. طلب المحتوى مع مرونة في التنسيق
    print(f"Requesting content for: {selected_topic}")
    prompt = f"""
    اكتب لي {selected_topic} لنشره في قناة تلجرام.
    
    التعليمات:
    1. التنسيق: وزع الأسطر بذكاء؛ اترك سطراً فارغاً "فقط" إذا كان الذكر طويلاً أو يحتاج لتنظيم (بين الحديث وفضله مثلاً)، أما إذا كان قصيراً جداً فاجعله متصلاً بشكل أنيق.
    2. الرموز: استخدم إيموجيات مناسبة (🌙، 🤲، 📿، 💎).
    3. الصحة: تأكد من صحة النص تماماً.
    4. المصدر: لا تذكر المصدر نهائياً (بدون اسم سورة، بدون رقم، بدون رواة).
    5. لا تستخدم الرمز ✨ نهائياً.
    6. التنويع: اختر شيئاً مختلفاً لضمان عدم التكرار.
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text.strip()
    
    print(f"Generated Content:\n{adkar_text}")

    # 2. إرسال الرسالة
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Smart formatted post completed!")

except Exception as e:
    print(f"❌ ERROR: {e}")

print("--- End Script ---")
