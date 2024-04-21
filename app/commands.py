from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from keyboards import main_keyboard, account_keyboard
from user_data import get_user_info, add_referral_bonus, get_user_subscriptions
from states import UserStates, SubscriptionManagementStates
from utils import format_user_info, generate_referral_link, format_subscription_info
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Команда /start
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    await message.answer("Добро пожаловать в VPN сервис! Чтобы начать, выберите команду из меню.", reply_markup=main_keyboard)
    await UserStates.MAIN_MENU.set()

# Команда /account
async def cmd_account(message: types.Message, state: FSMContext):
    """Обработчик команды /account"""
    try:
        user_info = await get_user_info(message.from_user.id)
        formatted_info = format_user_info(user_info)
        await message.answer(f"Личный кабинет:\n{formatted_info}", reply_markup=account_keyboard)
        await UserStates.ACCOUNT.set()
    except Exception as e:
        await message.answer(format_error_message(str(e)))

# Команда /referral
async def cmd_referral(message: types.Message, state: FSMContext):
    """Обработчик команды /referral"""
    try:
        bonus_added = await add_referral_bonus(message.from_user.id)
        if bonus_added:
            await message.answer("Бонус за приглашение друга успешно начислен!")
        else:
            await message.answer("Не удалось начислить бонус. Пожалуйста, попробуйте позже.")
    except Exception as e:
        await message.answer(format_error_message(str(e)))
    finally:
        await state.reset_state()

# Команда /subscriptions
async def cmd_subscriptions(message: types.Message, state: FSMContext):
    """Обработчик команды /subscriptions"""
    try:
        subscriptions = await get_user_subscriptions(message.from_user.id)
        if subscriptions:
            formatted_subs = format_subscription_info(subscriptions)
            await message.answer(f"Ваши подписки:\n{formatted_subs}", reply_markup=subscription_management_keyboard(subscriptions))
        else:
            await message.answer("У вас пока нет активных подписок.")
        await SubscriptionManagementStates.VIEWING_SUBSCRIPTION_DETAILS.set()
    except Exception as e:
        await message.answer(format_error_message(str(e)))

# commands.py
async def cmd_cancel(message: types.Message, state: FSMContext):
    """Обработчик команды /cancel"""
    current_state = await state.get_state()
    if current_state is not None:
        await state.reset_state()
        await message.answer("Действие отменено. Возвращаемся в главное меню.", reply_markup=main_keyboard)
        await UserStates.MAIN_MENU.set()
    else:
        await message.answer("Вы уже находитесь в главном меню.")


def subscription_management_keyboard(subscriptions):
    """Создание клавиатуры для управления подписками."""
    keyboard = InlineKeyboardMarkup()
    for sub in subscriptions:
        keyboard.add(InlineKeyboardButton(f"{sub['name']} - {sub['status']}", callback_data=f"manage_{sub['id']}"))
    keyboard.add(InlineKeyboardButton("Отменить подписку", callback_data="cancel_subscription"))
    return keyboard

# Регистрация команд
def register_commands(dp: Dispatcher):
    """Регистрация обработчиков команд."""
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_account, commands="account", state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_referral, commands="referral", state="*")
    dp.register_message_handler(cmd_subscriptions, commands="subscriptions", state=UserStates.ACCOUNT)
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
from states import SubscriptionManagementStates

@dp.callback_query_handler(Text(startswith='manage_'))
async def handle_manage_subscription(callback_query: types.CallbackQuery, state: FSMContext):
    """Обработчик для управления подпиской."""
    subscription_id = callback_query.data.split('_')[1]
    try:
        # Здесь должна быть логика для управления подпиской
        await callback_query.message.answer(f"Управление подпиской {subscription_id}")
        await SubscriptionManagementStates.CHANGING_SUBSCRIPTION_PLAN.set()
    except Exception as e:
        await callback_query.message.answer(format_error_message(str(e)))

@dp.callback_query_handler(Text(equals='cancel_subscription'), state=SubscriptionManagementStates.VIEWING_SUBSCRIPTION_DETAILS)
async def handle_cancel_subscription(callback_query: types.CallbackQuery, state: FSMContext):
    """Обработчик для отмены подписки."""
    try:
        # Здесь должна быть логика для отмены подписки
        await callback_query.message.answer("Ваша подписка отменена.")
        await state.reset_state()
    except Exception as e:
        await callback_query.message.answer(format_error_message(str(e)))

# Запуск бота
if __name__ == "__main__":
    from aiogram import executor
    from setup import dp  # Убедитесь, что у вас есть этот импорт в setup.py или аналогичном файле

    register_commands(dp)
    executor.start_polling(dp, skip_updates=True)