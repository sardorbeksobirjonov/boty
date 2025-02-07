import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = '7737973800:AAEOgsgLadLiTB1G-h7gZTLaupOFID51HVg'  # O'z tokeningizni shu yerga kiriting

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Kanalga link qo'yish
CHANNEL_LINK = "https://t.me/workiing_about_it"  # Kanalni shu yerga qo'ying

# Admin bilan bog'lanish uchun link
ADMIN_USERNAME = "@MuhammadSolih_web"  # Adminni shu yerga qo'ying

# Foydalanuvchilarni saqlash uchun fayl (buni ma'lumotlar bazasi bilan almashtirish mumkin)
users_file = 'users.txt'

# Foydalanuvchilarni fayldan o'qish
def get_users():
    if os.path.exists(users_file):
        with open(users_file, 'r') as file:
            return set(file.read().splitlines())
    else:
        return set()

# Foydalanuvchini faylga qo'shish
def add_user(user_id):
    with open(users_file, 'a') as file:
        file.write(f"{user_id}\n")

# Foydalanuvchilar ro'yxatini olish
def get_user_count():
    return len(get_users())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_id = str(message.from_user.id)

    # Foydalanuvchini faylga qo'shish
    if user_id not in get_users():
        add_user(user_id)

    welcome_text = f"""👋 Assalomu alaykum! Botga xush kelibsiz!

Hozirda botda {get_user_count()} ta foydalanuvchi mavjud.

Iltimos, kanalga qo'shiling: {CHANNEL_LINK}

Mana buyruqlarni tanlashingiz mumkin:

1️⃣ */Menudan tanlang*
2️⃣ *Telegram bot yaratish*
3️⃣ *Web sayt yaratish*

Iltimos, tanlovingizni yuboring! 😊
"""
    await message.reply(welcome_text)

@dp.message_handler(lambda message: any(word in message.text.lower() for word in ['menu', 'меню' ,'мену', 'boshqa buyurtma', 'другие заказы']))
async def reply_menu(message: types.Message):
    menu_text = """📌 *Xizmatlar ro‘yxati:*
    
💻 *Web sayt yaratish*  
🤖 *Telegram bot kerak*  
📄 *PDF qilish kerak*  
📇 *Vizitka kerak*  
📊 *Slayde kerak*  
🎨 *Logo kerak*  
🖼 *Ismga rasm kerak*  
🔠 *Telegram nik kerak*  
🎥 *Ismga video kerak*  
🎬 *Video montaj*  
🎤 *Audio montaj*

qande yozilgan bolsa shunde yozing namuna 👇🏻
 
Logo kerak

Agar xohlasangiz, admin bilan bog'lanish uchun *@MuhammadSolih_web* bilan bog'laning.
"""
    await message.reply(menu_text, parse_mode="Markdown")

@dp.message_handler(lambda message: any(word in message.text.lower() for word in ['web sayt kerak','sayt kerak', 'bot kerak', 'telegram bot kerak', 'pdf qilish kerak', 'vizitka kerak', 'slayde kerak', 'logo kerak', 'ismga rasm kerak', 'telegram nik kerak', 'ismga video kerak', 'video montaj', 'audio montaj', 'создание веб-сайта', 'нужен telegram bot', 'нужно pdf', 'визитка', 'слайды', 'логотип', 'нужна картинка', 'telegram ник', 'нужен видеоролик', 'видеомонтаж', 'аудиомонтаж']))
async def contact_admin(message: types.Message):
    """
    Agar foydalanuvchi "Web sayt yaratish" yoki "Telegram bot kerak" deb yozsa,
    admin bilan bog'lanish uchun xabar jo'natiladi.
    """
    await message.reply(f"Sizning so'rovingiz bo'yicha, admin bilan bog'laning: {ADMIN_USERNAME}")

@dp.message_handler()
async def unknown_command(message: types.Message):
    await message.reply("Iltimos, menyudan biror tanlov qiling.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
