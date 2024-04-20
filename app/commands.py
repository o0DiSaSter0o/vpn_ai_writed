from aiogram import Dispatcher, types
from keyboards import main_keyboard

async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Чтобы начать, выберите команду из меню.", reply_markup=main_keyboard())

def register_commands_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")

# Продолжение файла commands.py

@router.message(Command('account'), state=UserStates.MAIN_MENU)
async def cmd_account(message: types.Message):
    user_info = await get_user_info(message.from_user.id)
    await message.answer(format_user_info(user_info), reply_markup=account_keyboard())
    await UserStates.ACCOUNT.set()

# commands.py
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from user_data import add_referral_bonus

# ... (предыдущий код)

@router.message(Command('referral'))
async def cmd_referral(message: types.Message):
    # Предположим, что функция add_referral_bonus добавляет бонусы пользователю, который пригласил друга
    bonus_added = await add_referral_bonus(message.from_user.id)
    if bonus_added:
        await message.answer("Бонус за приглашение друга успешно начислен!")
    else:
        await message.answer("Не удалось начислить бонус. Пожалуйста, попробуйте позже.")

def register_commands_main(dp: Dispatcher):
    # ... (регистрация обработчиков команд)