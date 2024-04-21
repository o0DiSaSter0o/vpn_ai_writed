from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import main_keyboard, account_keyboard, trial_keyboard, buy_keyboard, subscription_types_keyboard
from vpn_api import activate_trial, buy_subscription, get_user_info, add_balance, process_subscription_payment
from user_data import get_user_balance, set_user_balance
from states import UserStates, PurchaseStates, TrialStates, ReferralStates, SubscriptionManagementStates

async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в наш VPN сервис! Выберите опцию в меню:", reply_markup=main_keyboard())
    await UserStates.MAIN_MENU.set()

async def cmd_trial(message: types.Message, state: FSMContext):
    response = await activate_trial(message.from_user.id)
    await message.answer(response)
    await state.reset_state()

async def cmd_buy_subscription_query(message: types.Message, state: FSMContext):
    await message.answer("Выберите тип подписки и произведите оплату.", reply_markup=subscription_types_keyboard())
    await PurchaseStates.WAITING_FOR_SUBSCRIPTION_TYPE.set()

async def handle_subscription_purchase(callback_query: types.CallbackQuery, state: FSMContext):
    subscription_type = callback_query.data.split('_')[1]
    response = await process_subscription_payment(callback_query.from_user.id, subscription_type)
    await callback_query.message.answer(response)
    await state.reset_state(with_data=True)

async def cmd_account(message: types.Message, state: FSMContext):
    user_info = await get_user_info(message.from_user.id)
    balance = await get_user_balance(message.from_user.id)
    await message.answer(f"Личный кабинет:\n{user_info}\nБаланс: {balance}", reply_markup=account_keyboard())
    await UserStates.ACCOUNT.set()

async def cmd_help(message: types.Message, state: FSMContext):
    await message.answer("Как я могу помочь?")
    await state.reset_state()

async def handle_back(message: types.Message, state: FSMContext):
    await message.answer("Возвращаемся в главное меню...", reply_markup=main_keyboard())
    await UserStates.MAIN_MENU.set()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_trial, lambda message: 'Пробный период' in message.text, state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_buy_subscription_query, lambda message: 'Купить подписку' in message.text, state=UserStates.MAIN_MENU)
    dp.register_callback_query_handler(handle_subscription_purchase, Text(startswith='buy_'), state=PurchaseStates.WAITING_FOR_SUBSCRIPTION_TYPE)
    dp.register_message_handler(cmd_account, lambda message: 'Личный кабинет' in message.text, state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_help, lambda message: 'Помощь' in message.text, state="*")
    dp.register_message_handler(handle_back, Text(equals='Назад'), state=UserStates.ACCOUNT)
    # Добавьте другие обработчики по мере необходимости

# В конце файла handlers.py
if __name__ == "__main__":
    from aiogram import executor
    from setup import dp  # Убедитесь, что у вас есть этот импорт в setup.py или аналогичном файле

    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)