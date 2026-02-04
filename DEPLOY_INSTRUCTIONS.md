# Render.com ga joylash uchun qo'llanma

Botni bepul va oson ishga tushirish uchun **Render.com** platformasidan foydalanamiz.

## 1-qadam: GitHub-ga yuklash

Agar hali GitHub akkountingiz bo'lmasa, [github.com](https://github.com) saytidan ro'yxatdan o'ting.

1.  GitHub-da yangi **Repository** yarating (nomini masalan `telegram-bot-reklama` deb qo'ying).
2.  Ushbu bot fayllarini o'sha repositoryga yuklang.

## 2-qadam: Render.com da ro'yxatdan o'tish

1.  [render.com](https://render.com) saytiga kiring.
2.  "Get Started" tugmasini bosing va **GitHub** orqali kiring.

## 3-qadam: Web Service yaratish

1.  Render panelida **"New +"** tugmasini bosib, **"Web Service"** ni tanlang.
2.  Ro'yxatdan GitHub-dagi `telegram-bot-reklama` loyihangizni tanlang.
3.  Sozlamalarni quyidagicha to'ldiring:
    *   **Name:** (bot nomi)
    *   **Region:** Frankfurt (yoki o'zingizga yaqin joy)
    *   **Branch:** main (yoki master)
    *   **Root Directory:** (bo'sh qoldiring)
    *   **Runtime:** Python 3
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `python main.py`
    *   **Instance Type:** Free (bepul variantni tanlang)

4.  **"Create Web Service"** tugmasini bosing.

## Tayyor!

Render loyihangizni quradi (build) va ishga tushiradi. Bir necha daqiqadan so'ng botingiz "Live" holatiga o'tadi va Telegramda ishlay boshlaydi.

**Eslatma:** Bepul versiyada Render botni vaqti-vaqti bilan "uxlatib" qo'yishi mumkin (agar murojaat bo'lmasa). Lekin biz kodga maxsus "Web Server" qo'shdik, bu botning o'chib qolmasligiga yordam beradi. Render botingizga https://sizning-botingiz.onrender.com kabi adres beradi. Shu adresga har 5-10 daqiqada "ping" berib turadigan xizmatlardan (masalan, UptimeRobot) foydalansangiz, botingiz hech qachon uxlamaydi.
