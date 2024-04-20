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