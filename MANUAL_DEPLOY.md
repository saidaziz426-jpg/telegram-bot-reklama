# Render.com ga joylash uchun to'liq qo'llanma

Sizning kompyuteringizda `git` dasturi o'rnatilmaganligi sababli, men fayllarni avtomatik yuklay olmayman. Lekin xavotir olmang, buni qo'lda qilish juda oson!

Quyidagi qadamlarni birma-bir bajaring:

## 1-qadam: GitHub-da Repository ochish

1.  [GitHub.com](https://github.com) saytiga kiring va profilingizga kiring (Log in).
2.  Yuqoridagi **+** belgisini bosib, **New repository** ni tanlang.
3.  **Repository name** ga `telegram-bot-reklama` deb yozing.
4.  **Public** ni tanlang.
5.  Pastdagi **Create repository** tugmasini bosing.

## 2-qadam: Fayllarni yuklash

1.  Yaratilgan repository sahifasida **"uploading an existing file"** degan havolani toping va bosing.
2.  Mening yaratgan fayllarim joylashgan papkani oching: `c:\Users\User\bot`
3.  Quyidagi fayllarni sudrab (drag & drop) GitHub oynasiga tashlang:
    *   `main.py`
    *   `requirements.txt`
    *   `Procfile`
    *   `README.md`
4.  Pastda **Commit changes** tugmasini bosing.

## 3-qadam: Render.com ga ulash

1.  [Render.com](https://render.com) saytiga kiring.
2.  **New +** -> **Web Service** ni tanlang.
3.  Ro'yxatdan hozirgina ochgan `telegram-bot-reklama` loyihangizni tanlang va **Connect** bosing.
4.  Sozlamalarni tekshiring:
    *   **Name:** `reklama-bot` (yoki o'zingiz xohlagan nom)
    *   **Runtime:** `Python 3`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `python main.py`
5.  Pastga tushib **"Advanced"** bo'limini oching va **"Add Environment Variable"** tugmasini bosing:
    *   **Key:** `BOT_TOKEN`
    *   **Value:** `8350540859:AAERlHPnfgX7aBnxhIqeu2G9n-jOsiOvJX0`
6.  **Create Web Service** tugmasini bosing.

## Tayyor!

Render botni o'rnatishni boshlaydi. Jarayon tugagach (1-2 daqiqa), botingiz telegramda ishlay boshlaydi.

**Muhim:** Render botingizga web manzil beradi (masalan `https://reklama-bot.onrender.com`). Bu manzilga kirib ko'rsangiz "Bot is running" degan yozuv chiqishi kerak.
