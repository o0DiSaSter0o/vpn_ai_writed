from database import execute, fetch

async def get_user_balance(user_id):
    """Получение баланса пользователя."""
    query = "SELECT balance FROM users WHERE id = $1"
    result = await fetch(query, user_id)
    if result:
        return result[0]['balance']
    return 0

async def set_user_balance(user_id, amount):
    """Установка баланса пользователя."""
    query = "UPDATE users SET balance = $1 WHERE id = $2"
    await execute(query, amount, user_id)

async def update_user_subscription(user_id, subscription_data):
    """Обновление данных о подписке пользователя."""
    query = "INSERT INTO subscriptions (user_id, name, status, expires) VALUES ($1, $2, $3, $4)"
    await execute(query, user_id, subscription_data['name'], subscription_data['status'], subscription_data['expires'])

async def add_referral_bonus(user_id):
    """Начисление бонуса пользователю за приглашение друга."""
    query = "UPDATE users SET referral_bonus = referral_bonus + 100 WHERE id = $1"
    await execute(query, user_id)
    return True

async def get_referral_bonus(user_id):
    """Получение суммы реферального бонуса пользователя."""
    query = "SELECT referral_bonus FROM users WHERE id = $1"
    result = await fetch(query, user_id)
    if result:
        return result[0]['referral_bonus']
    return 0

async def get_user_subscriptions(user_id):
    """Получение активных подписок пользователя."""
    query = "SELECT name, status, expires FROM subscriptions WHERE user_id = $1"
    result = await fetch(query, user_id)
    return [dict(row) for row in result]