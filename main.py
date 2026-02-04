import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiohttp import web

# Bot tokeni
# Xavfsizlik uchun tokeni Environment Variable dan olamiz, yoki to'g'ridan-to'g'ri yozamiz (agar local bo'lsa)
TOKEN = os.getenv("BOT_TOKEN", "8350540859:AAERlHPnfgX7aBnxhIqeu2G9n-jOsiOvJX0")

dp = Dispatcher()

DEFAULT_FORBIDDEN = [
    "http://",
    "https://",
    "t.me/",
    "telegram.me/",
    "www.",
    ".com",
    ".uz",
    ".ru",
    "reklama",
    "sotiladi",
    "kanalga obuna",
]

def get_forbidden_words():
    extra = os.getenv("FORBIDDEN_WORDS", "")
    extra_list = [w.strip().lower() for w in extra.split(",") if w.strip()]
    return DEFAULT_FORBIDDEN + extra_list

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    /start buyrug'iga javob
    """
    await message.answer(f"Salom! Men guruhlarda reklama va linklarni o'chiruvchi botman. Meni guruhga qo'shing va admin huquqini bering.")

@dp.message()
async def check_messages(message: Message) -> None:
    """
    Barcha xabarlarni tekshiradi va reklama yoki link borligini aniqlaydi.
    """
    if message.chat.type not in ["group", "supergroup"]:
        return

    found_ads = False
    
    # 1. Matndagi entitylarni tekshirish
    entities = message.entities or []
    if message.caption_entities:
        entities.extend(message.caption_entities)
        
    for entity in entities:
        if entity.type in ["url", "text_link", "mention", "email"]:
            found_ads = True
            break
            
    # 2. Kalit so'zlarni tekshirish
    if not found_ads:
        text = (message.text or message.caption or "").lower()
        forbidden_words = get_forbidden_words()
        if any(word in text for word in forbidden_words):
            found_ads = True

    if found_ads:
        try:
            await message.delete()
        except Exception as e:
            logging.error(f"Xabarni o'chirishda xatolik: {e}")

async def health_check(request):
    return web.Response(text="Bot is running")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Web server started on port {port}")

async def main() -> None:
    # Web serverni fon rejimida ishga tushirish (Render kabi platformalar uchun kerak)
    await start_web_server()
    
    # Botni ishga tushirish
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
