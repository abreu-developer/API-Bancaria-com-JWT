from src.models.settings.db_connection_handler import db_connect_handler

from .user_repository import UserRepository


def test_repository():
    db_connect_handler.connect()

    conn = db_connect_handler.get_connect()
    repo = UserRepository(conn)

    username = "admin1"
    password = "admin1"

    repo.register_user(username, password)

    user = repo.get_user_by_username(username)

    print()
    print("Usuário antes da alteração:")
    print(user)

    repo.edit_balance(user[0], 6672.10)

    user_updated = repo.get_user_by_username(username)

    print()
    print("Usuário depois da alteração:")
    print(user_updated)