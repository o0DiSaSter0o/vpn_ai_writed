# keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton('Пробный период'))
main_keyboard.add(KeyboardButton('Купить подписку'))
main_keyboard.add(KeyboardButton('Личный кабинет'))
main_keyboard.add(KeyboardButton('Помощь'))

# Клавиатура личного кабинета
account_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
account_keyboard.add(KeyboardButton('Мои подписки'))
account_keyboard.add(KeyboardButton('Мой баланс'))
account_keyboard.add(KeyboardButton('Назад'))

# Inline клавиатура для пробного периода
trial_keyboard = InlineKeyboardMarkup()
trial_keyboard.add(InlineKeyboardButton('Активировать пробный период', callback_data='activate_trial'))

# Inline клавиатура для оплаты подписки
buy_keyboard = InlineKeyboardMarkup()
buy_keyboard.add(InlineKeyboardButton('Оплатить подписку', callback_data='buy_subscription'))

def subscription_types_keyboard():
    """Создание клавиатуры с вариантами типов подписок."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('1 месяц - 300 монет', callback_data='buy_1_month'))
    keyboard.add(InlineKeyboardButton('3 месяца - 800 монет', callback_data='buy_3_months'))
    keyboard.add(InlineKeyboardButton('1 год - 2500 монет', callback_data='buy_1_year'))
    return keyboard