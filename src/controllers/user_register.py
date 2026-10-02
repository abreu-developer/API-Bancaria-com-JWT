from src.models.interface.user_repository import UserRepository


class UserRegister(UserRepository):
    def __init__(self, user_repository: UserRepository):
        pass

    def register_user(self, username: str, password: str) -> None:
        pass

