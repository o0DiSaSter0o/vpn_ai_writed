def format_user_info(user_info):
    """Форматирование информации о пользователе для вывода."""
    return f"Активные подписки: {user_info['subscriptions']}\nТариф: {user_info['tariff']} 💵 в день\nБаланс: {user_info['balance']} 💵"

# Добавьте другие вспомогательные функции по мере необходимости.