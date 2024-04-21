# utils.py

def format_user_info(user_info):
    """Форматирование информации о пользователе для вывода."""
    return f"Активные подписки: {user_info['subscriptions']}\nТариф: {user_info['tariff']} 💵 в день\nБаланс: {user_info['balance']} 💵"

def format_subscription_info(subscriptions):
    """Форматирование информации о подписках пользователя для вывода."""
    if not subscriptions:
        return "У вас нет активных подписок."
    subscription_lines = []
    for sub in subscriptions:
        line = f"{sub['name']}: {sub['status']} до {sub['expires']}"
        subscription_lines.append(line)
    return "\n".join(subscription_lines)

def generate_referral_link(user_id, base_url="http://your-vpn-service.com/referral"):
    """Генерация реферальной ссылки для пользователя."""
    return f"{base_url}?referral_id={user_id}"

def is_valid_referral_code(referral_code):
    """Проверка валидности реферального кода."""
    # Это просто пример. Вам нужно будет реализовать логику проверки в соответствии с вашей системой.
    return len(referral_code) == 8 and referral_code.isdigit()

def format_error_message(error):
    """Форматирование сообщения об ошибке."""
    return f"⚠️ Произошла ошибка: {error}"

# Добавьте другие вспомогательные функции по мере необходимости.