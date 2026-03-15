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

    # قائمة مواضيع متنوعة لضمان عدم التكرار
    topics = [
        "ذكر نبوي عن راحة البال", "دعاء قصير ومؤثر", "حديث عن فضل الاستغفار",
        "كلمات ثقيلة في الميزان", "دعاء للمغفرة والرحمة", "حديث عن فضل الصلاة على النبي", 
        "ذكر عن فضل لا حول ولا قوة إلا بالله", "آية قرآنية قصيرة عن الصبر",
        "دعاء لتيسير الأمور", "ذكر فيه أجر عظيم"
    ]
    selected_topic = random.choice(topics)

    # 1. طلب المحتوى مع التركيز على المسافات والجمالية
    print(f"Requesting content for: {selected_topic}")
    prompt = f"""
    اكتب لي {selected_topic} لنشره في قناة تلجرام.
    
    الشروط الجمالية:
    1. المسافات: اترك سطراً فارغاً بين كل جملة وأخرى (ضروري جداً لجمالية الذكر).
    2. التنسيق: وزع الكلام على أسطر متفرقة ولا تجعله كتلة واحدة متراصة.
    3. الرموز: استخدم إيموجيات هادئة وجميلة (🌙، 🤲، 📿، 💎).
    
    الشروط العلمية:
    4. لا تذكر المصدر نهائياً (بدون اسم سورة، بدون رقم آية، وبدون رواة).
    5. ابدأ مباشرة بالنص (قال الله تعالى.. أو قال رسول الله ﷺ.. أو النص مباشرة).
    6. تأكد من صحة النص تماماً.
    7. لا تستخدم الرمز ✨ نهائياً.
    8. اختر ذكراً مختلفاً لضمان عدم التكرار خلال الأسبوع.
    """
    
    response = model.generate_content(prompt)
    adkar_text = response.text.strip()
    
    print(f"Generated Content:\n{adkar_text}")

    # 2. إرسال الرسالة
    bot.send_message(CHANNEL_ID, adkar_text)
    print("✅ SUCCESS: Aesthetic post without source completed!")

except Exception as e:
    print(f"❌ ERROR: {e}")

print("--- End Script ---")
