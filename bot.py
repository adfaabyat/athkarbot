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

    # اختيار عشوائي للمصدر لضمان التنوع
    sources = ["آية قرآنية", "حديث نبوي شريف", "ذكر مأثور عن النبي ﷺ"]
    selected_source = random.choice(sources)

    # 1. طلب المحتوى من Gemini مع التركيز على الصحة والجمالية
    print(f"Requesting valid {selected_source}...")
    prompt = f"""
    اريد {selected_source} لنشره في قناة تلجرام مخصصة للأذكار.
    
    الشروط:
    1. تأكد تماماً من صحة الآية (بالتشكيل) أو صحة الحديث النبوي (من الكتب الصحاح).
    2. التنسيق: اترك مسافات كافية بين الأسطر ليكون الكلام مريحاً للقراءة.
    3. الرموز: استخدم إيموجيات إسلامية وجميلة (مثل 🌙، 🤲، 📿، 📖، 💎) لتزيين المنشور.
    4. المحتوى: يجب أن يتضمن المصدر (مثل اسم السورة ورقم الآية، أو الراوي/الكتاب للحديث).
    5. لا تضف أي مقدمات خارج نص المنشور، ولا تستخدم الرمز ✨.
    6. اجعل المنشور قصيراً ومؤثراً.
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text.strip()
    
    print(f"Generated Content:\n{adkar_text}")

    # 2. إرسال الرسالة
    bot.send_message(CHANNEL_ID, adkar_text)
    print(f"✅ SUCCESS: {selected_source} posted successfully!")

except Exception as e:
    print(f"❌ ERROR: {e}")

print("--- End Script ---")
