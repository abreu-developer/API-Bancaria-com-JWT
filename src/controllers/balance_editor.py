from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.models.interface.user_repository import UserRepository


class BalanceEditor(BalanceEditorInterface):
    def __init__(self, user_repository: UserRepository) -> None:
            self.__user_repository = user_repository


    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__user_repository.edit_balance(user_id, new_balance)
        return{
            "type" :"user",
            "count": 1,
            "new_balance": new_balance
        }