# states.py
from aiogram.dispatcher.filters.state import StatesGroup, State

class UserStates(StatesGroup):
    MAIN_MENU = State()
    ACCOUNT = State()
    TRIAL_ACTIVATED = State()
    SUBSCRIPTION_PURCHASED = State()
    HELP = State()

class PurchaseStates(StatesGroup):
    WAITING_FOR_SUBSCRIPTION_TYPE = State()
    WAITING_FOR_PAYMENT_CONFIRMATION = State()

class TrialStates(StatesGroup):
    WAITING_FOR_TRIAL_ACTIVATION = State()

class ReferralStates(StatesGroup):
    WAITING_FOR_REFERRAL_ACTIVATION = State()

class SubscriptionManagementStates(StatesGroup):
    VIEWING_SUBSCRIPTION_DETAILS = State()
    CHANGING_SUBSCRIPTION_PLAN = State()
    CANCELING_SUBSCRIPTION = State()

# Возможно, вам потребуется добавить дополнительные состояния для других функций бота.