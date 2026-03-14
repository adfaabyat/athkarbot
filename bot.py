import os
import telebot
import google.generativeai as genai

# Configuration dyal Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

# Configuration dyal Telegram
BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']
bot = telebot.TeleBot(BOT_TOKEN)

def get_adkar():
    # الـ Prompt الجديد بدون رمز النجمة
    prompt = """
    أعطني رسالة منظمة للأذكار بنفس التنسيق التالي تماماً:

    📿 تسبيح
    
    اسم التسبيح (مثال: سبحان الله) ×33
    اسم التسبيح (مثال: الحمد لله) ×33
    اسم التسبيح (مثال: الله أكبر) ×34

    💎 دقيقة واحدة من وقتك قد تكون سببًا في رفعة درجتك عند الله.

    🤲 دعاء
    
    (اكتب هنا دعاء قصير وجميل من سطرين أو ثلاثة)
    (مثال: اللهم اجعلنا من الذاكرين الشاكرين...)

    ملاحظة: 
    1. استخدم الرموز التعبيرية الإسلامية المناسبة مثل (📿، 🤲، 💎، 🌙).
    2. لا تستخدم رمز النجمة (✨).
    3. لا تضف أي مقدمات أو خاتمة، فقط النص المطلوب.
    """
    response = model.generate_content(prompt)
    return response.text

def main():
    try:
        adkar_text = get_adkar()
        bot.send_message(CHANNEL_ID, adkar_text)
        print("Adkar posted with new safe emojis!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
