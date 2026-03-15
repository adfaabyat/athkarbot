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
        "ذكر نبوي قصير", "دعاء من القرآن", "فضل الاستغفار",
        "تسبيح وتحميد", "صلاة على النبي ﷺ", "كلمات طيبة"
    ]
    selected_topic = random.choice(topics)

    # 1. طلب المحتوى مع تحديد عدد الأسطر
    print(f"Requesting content for: {selected_topic}")
    prompt = f"""
    اكتب لي {selected_topic} لنشره في قناة تلجرام.
    
    التعليمات الأساسية:
    1. الطول: يجب أن يكون المنشور قصيراً جداً (ما بين سطرين إلى خمسة أسطر فقط).
    2. التنسيق: اترك سطراً فارغاً "فقط" إذا كان ذلك سيجعل الذكر أكثر تنظيماً وجمالاً.
    3. المصدر: لا تذكر المصدر نهائياً (بدون اسم سورة، بدون رقم آية، وبدون رواة).
    4. الصحة: تأكد من صحة النص تماماً.
    5. الرموز: استخدم إيموجيات هادئة (🌙، 🤲، 📿، 💎).
    6. لا تستخدم الرمز ✨ نهائياً.
    7. ابدأ مباشرة بالنص (مثل: قال رسول الله ﷺ.. أو النص مباشرة).
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text.strip()
    
    # التأكد من طول النص (اختياري برمجياً ولكن Gemini سيلتزم بالبرومبت)
    print(f"Generated Content:\n{adkar_text}")

    # 2. إرسال الرسالة
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Short & smart post completed!")

except Exception as e:
    print(f"❌ ERROR: {e}")

print("--- End Script ---")
