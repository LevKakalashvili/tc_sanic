from app.models import InactiveUser


def clear_inactive_user_table():
    """Очистка таблицы не активных пользователей."""
    InactiveUser.clear()
