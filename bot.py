from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os

# 🔑 Твой токен (вставь свой)
API_TOKEN = "8031283770:AAG3eNz7mSRjmaGJ1MDDdVZdo0tKEX5Ktis"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- Главное меню ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Контакты")],
    ],
    resize_keyboard=True
)

# --- Команда /start ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Привет! Я юридический помощник сервиса proDolgi.\n\n"
        "Скоро, используя этот бот ты сможешь получить помощь по исполнительным надписям нотариуса.\n\n"
        "Выбери нужный пункт в меню 👇",
        reply_markup=main_menu
    )

# --- Кнопка «Контакты» ---
@dp.message(lambda message: message.text == "📞 Контакты")
async def send_contacts(message: types.Message):
    await message.answer(
        "📌 Контакты сервиса proDolgi:\n\n"
        "Тел: +77770558008\n"
	"Tik Tok: prodolgi.kz\n"  
	"Instagram: @prodolgi.online\n"
        "💬 WhatsApp: (https://wa.me/77770558008)\n"
    )

# --- Запуск бота ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
