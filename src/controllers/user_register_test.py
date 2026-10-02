from .user_register import UserRegister


class MockUserRepository:
    def __init__(self):
        self.register_user_attributes = {}

    def register_user(self, username, password) -> None:
        self.register_user_attributes["username"] = username
        self.register_user_attributes["password"] = password


def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    username = "admin"
    password = "admin"

    response = controller.registry(username, password)

    assert response["type"] == "user"
    assert response["username"] == username

    assert repository.register_user_attributes["username"] == username
    assert repository.register_user_attributes["password"] is not None
    assert repository.register_user_attributes["password"] != password