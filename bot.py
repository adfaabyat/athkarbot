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

    # قائمة متنوعة جداً لضمان عدم التكرار
    topics = [
        "ذكر نبوي عن راحة البال", "دعاء قصير من القرآن", "حديث عن فضل الاستغفار",
        "ذكر من أذكار الصباح النادرة", "كلمات خفيفة على اللسان ثقيلة في الميزان",
        "دعاء للمغفرة والرحمة", "حديث عن فضل الصلاة على النبي", 
        "ذكر عن فضل لا حول ولا قوة إلا بالله", "آية قرآنية عن الصبر",
        "دعاء لتيسير الأمور", "ذكر فيه أجر عظيم وبسيط في الحروف"
    ]
    selected_topic = random.choice(topics)

    # 1. طلب المحتوى من Gemini بدون مصدر وبدون تكرار
    print(f"Requesting content for: {selected_topic}")
    prompt = f"""
    اكتب لي {selected_topic} لنشره في قناة تلجرام.
    
    الشروط:
    1. لا تذكر المصدر نهائياً (لا تذكر اسم السورة، رقم الآية، الراوي، أو كتاب الحديث).
    2. ابدأ مباشرة بالنص (مثلاً: قال الله تعالى.. أو قال رسول الله ﷺ.. أو مباشرة بالذكر).
    3. تأكد من صحة النص تماماً.
    4. التنسيق: اترك مسافة (سطر فارغ) بين الجمل ليكون المنشور منسقاً وجميلاً.
    5. الرموز: استخدم إيموجيات متنوعة (مثل 🌙، 🤲، 📿، 💎) لتزيين الكلام.
    6. التنوع: اختر ذكراً مختلفاً تماماً عما هو مشهور، لضمان عدم التكرار خلال هذا الأسبوع.
    7. لا تستخدم الرمز ✨ نهائياً، ولا تضف أي مقدمات خارج نص المنشور.
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text.strip()
    
    print(f"Generated Content:\n{adkar_text}")

    # 2. إرسال الرسالة
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Unique post without source completed!")

except Exception as e:
    print(f"❌ ERROR: {e}")

print("--- End Script ---")
