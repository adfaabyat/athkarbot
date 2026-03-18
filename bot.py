import os
import telebot
import google.generativeai as genai
import random

print("--- Start Script ---")

try:
    # إعداد Gemini
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-2.5-flash')

    # إعداد التليجرام
    BOT_TOKEN = os.environ['BOT_TOKEN']
    CHANNEL_ID = os.environ['CHANNEL_ID']
    bot = telebot.TeleBot(BOT_TOKEN)

    print("Telegram Bot configured.")

    # مواضيع متنوعة
    topics = [
        "ذكر نبوي قصير",
        "دعاء جميل",
        "كلمات طيبة",
        "ذكر بسيط",
        "تسبيح وتحميد",
        "دعاء من القلب"
    ]

    selected_topic = random.choice(topics)

    # 🔥 برومبت قوي لمنع التكرار
    prompt = f"""
اكتب {selected_topic} لنشره في قناة تلجرام.

⚠️ مهم جداً:
- لا تكرر الأذكار المشهورة مثل: سبحان الله وبحمده سبحان الله العظيم
- كل مرة يجب أن يكون النص مختلف تماماً
- لا تعيد نفس الجمل أو الصياغة
- اجعل الذكر متنوع وغير تقليدي

الشروط:
1. الطول: من سطرين إلى 5 أسطر فقط
2. التنسيق: جميل ومرتب
3. بدون ذكر المصدر نهائياً
4. النص صحيح 100%
5. استخدم إيموجيات هادئة (🌙 🤲 📿 💎)
6. لا تستخدم ✨
7. ابدأ مباشرة بالنص
"""

    # 🔁 إعادة المحاولة إذا تكرر
    previous_texts = []

    for _ in range(3):  # يحاول 3 مرات
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.9,
                "top_p": 0.95
            }
        )

        adkar_text = response.text.strip()

        if adkar_text not in previous_texts:
            break

    previous_texts.append(adkar_text)

    print(f"Generated Content:\n{adkar_text}")

    # إرسال الرسالة
    bot.send_message(CHANNEL_ID, adkar_text)

    print("✅ SUCCESS: Unique post sent!")

except Exception as e:
    print(f"❌ ERROR: {e}")

print("--- End Script ---")
