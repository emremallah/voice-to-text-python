import speech_recognition as sr

# ایجاد یک شیء شناسایی
r = sr.Recognizer()

# استفاده از میکروفون به عنوان منبع ورودی
with sr.Microphone() as source:
    print("در حال گوش دادن...")
    # خواندن داده‌های صوتی از میکروفون پیش فرض
    audio_data = r.record(source, duration=10)
    print("در حال شناسایی...")
    # تبدیل سخن به متن با استفاده از API شناسایی سخن گوگل
    text = r.recognize_google(audio_data, language='fa-IR')
    print(text)

# ذخیره متن در یک فایل با استفاده از کدک utf-8
with open('output1.txt', 'w', encoding='utf-8') as file:
    file.write(text)
