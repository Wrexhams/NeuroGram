from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    
    buttons = [
        KeyboardButton("ℹ️ Информация"),
        KeyboardButton("🔧 Настройки"),
        KeyboardButton("🔄 Обновить"),
        KeyboardButton("❓ Помощь")
    ]
    
    keyboard.add(*buttons)
    return keyboard
