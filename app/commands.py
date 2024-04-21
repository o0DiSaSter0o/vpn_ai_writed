from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from keyboards import main_keyboard, account_keyboard
from user_data import add_referral_bonus, get_user_info
from states import UserStates
from utils import format_user_info

# Команда /start
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в VPN сервис! Чтобы начать, выберите команду из меню.", reply_markup=main_keyboard())
    await UserStates.MAIN_MENU.set()

# Регистрация команд
def register_commands_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")

# Команда /account
async def cmd_account(message: types.Message, state: FSMContext):
    user_info = await get_user_info(message.from_user.id)
    formatted_info = format_user_info(user_info)
    await message.answer(f"Личный кабинет:\n{formatted_info}", reply_markup=account_keyboard())
    await UserStates.ACCOUNT.set()

# Команда /referral
async def cmd_referral(message: types.Message, state: FSMContext):
    bonus_added = await add_referral_bonus(message.from_user.id)
    if bonus_added:
        await message.answer("Бонус за приглашение друга успешно начислен!")
    else:
        await message.answer("Не удалось начислить бонус. Пожалуйста, попробуйте позже.")
    await state.reset_state()

# Команда /subscriptions
async def cmd_subscriptions(message: types.Message, state: FSMContext):
    subscriptions = await get_user_subscriptions(message.from_user.id)
    if subscriptions:
        await message.answer("Ваши подписки:", reply_markup=subscription_management_keyboard(subscriptions))
    else:
        await message.answer("У вас пока нет активных подписок.")
    await SubscriptionManagementStates.VIEWING_SUBSCRIPTION_DETAILS.set()
    
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def subscription_management_keyboard(subscriptions):
    keyboard = InlineKeyboardMarkup()
    for sub in subscriptions:
        keyboard.add(InlineKeyboardButton(f"{sub['name']} - {sub['status']}", callback_data=f"manage_{sub['id']}"))
    keyboard.add(InlineKeyboardButton("Отменить подписку", callback_data="cancel_subscription"))
    return keyboard

# Регистрация команд
def register_commands_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_account, commands="account", state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_referral, commands="referral", state="*")
    dp.register_message_handler(cmd_subscriptions, commands="subscriptions", state=UserStates.ACCOUNT)
from states import SubscriptionManagementStates

@router.callback_query(Text(startswith='manage_'))
async def handle_manage_subscription(callback_query: types.CallbackQuery, state: FSMContext):
    subscription_id = callback_query.data.split('_')[1]
    # Здесь должна быть логика для управления подпиской
    await callback_query.message.answer(f"Управление подпиской {subscription_id}")
    await SubscriptionManagementStates.CHANGING_SUBSCRIPTION_PLAN.set()

@router.callback_query(Text(equals='cancel_subscription'), state=SubscriptionManagementStates.VIEWING_SUBSCRIPTION_DETAILS)
async def handle_cancel_subscription(callback_query: types.CallbackQuery, state: FSMContext):
    # Здесь должна быть логика для отмены подписки
    await callback_query.message.answer("Ваша подписка отменена.")
    await state.reset_state()
# Запуск бота
if __name__ == "__main__":
    from aiogram import executor
    from setup import dp  # Убедитесь, что у вас есть этот импорт в setup.py или аналогичном файле

    register_commands_main(dp)
    executor.start_polling(dp, skip_updates=True)