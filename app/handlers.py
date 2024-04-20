from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import main_keyboard, account_keyboard
from vpn_api import activate_trial, buy_subscription, get_user_info, add_balance
from user_data import get_user_balance, set_user_balance

class UserStates(StatesGroup):
    MAIN_MENU = State()
    ACCOUNT = State()

async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в наш VPN сервис! Выберите опцию в меню:", reply_markup=main_keyboard())
    await UserStates.MAIN_MENU.set()

async def cmd_trial(message: types.Message, state: FSMContext):
    response = await activate_trial(message.from_user.id)
    await message.answer(response)
    await state.finish()

async def cmd_buy_subscription(message: types.Message, state: FSMContext):
    response = await buy_subscription(message.from_user.id)
    await message.answer(response, reply_markup=account_keyboard())
    await UserStates.ACCOUNT.set()

async def cmd_account(message: types.Message, state: FSMContext):
    user_info = await get_user_info(message.from_user.id)
    balance = await get_user_balance(message.from_user.id)
    await message.answer(f"Личный кабинет:\n{user_info}\nБаланс: {balance}", reply_markup=account_keyboard())
    await UserStates.ACCOUNT.set()

async def cmd_help(message: types.Message, state: FSMContext):
    await message.answer("Как я могу помочь?")
    await state.finish()

def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_trial, lambda message: 'Пробный период' in message.text, state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_buy_subscription, lambda message: 'Купить подписку' in message.text, state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_account, lambda message: 'Личный кабинет' in message.text, state=UserStates.MAIN_MENU)
    dp.register_message_handler(cmd_help, lambda message: 'Помощь' in message.text, state="*")
# Продолжение файла handlers.py

@router.message(Text(equals='Назад'), state=UserStates.ACCOUNT)
async def handle_back(message: types.Message, state: FSMContext):
    await message.answer("Возвращаемся в главное меню...", reply_markup=main_keyboard())
    await UserStates.MAIN_MENU.set()

# handlers.py
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from states import UserStates, PurchaseStates, TrialStates
from keyboards import main_keyboard, account_keyboard, trial_keyboard, buy_keyboard
from vpn_api import activate_trial, buy_subscription, get_user_info, add_balance
from user_data import get_user_balance, set_user_balance

# ... (предыдущий код)

@router.message(Text(equals='Активировать пробный период'), state=UserStates.MAIN_MENU)
async def handle_activate_trial(message: types.Message, state: FSMContext):
    await TrialStates.WAITING_FOR_TRIAL_ACTIVATION.set()
    # Здесь должна быть логика активации пробного периода
    await message.answer("Пробный период активирован на 2 дня. Инструкции отправлены вам в сообщении.", reply_markup=main_keyboard())
    await state.finish()

@router.message(Text(equals='Оплатить подписку'), state=UserStates.MAIN_MENU)
async def handle_buy_subscription(message: types.Message, state: FSMContext):
    await PurchaseStates.WAITING_FOR_SUBSCRIPTION_TYPE.set()
    # Здесь должна быть логика выбора типа подписки и перехода к оплате
    await message.answer("Выберите тип подписки и произведите оплату.", reply_markup=buy_keyboard())

# ... (добавление других обработчиков)

def register_handlers_main(dp: Dispatcher):
    # ... (регистрация обработчиков)

# handlers.py
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import main_keyboard, subscription_types_keyboard
from vpn_api import process_subscription_payment
from states import UserStates, PurchaseStates

# ... (предыдущий код)

@router.callback_query(Text(startswith='buy_'))
async def handle_subscription_purchase(callback_query: types.CallbackQuery, state: FSMContext):
    subscription_type = callback_query.data.split('_')[1]
    response = await process_subscription_payment(callback_query.from_user.id, subscription_type)
    await callback_query.message.answer(response)
    await state.finish()

# ... (добавление других обработчиков)