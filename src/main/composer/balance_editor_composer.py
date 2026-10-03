from src.models.settings.db_connection_handler import db_connect_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.balance_editor import BalanceEditor
from src.views.balance_edit_view import BalanceEditView

def balance_editor_composer():
    conn = db_connect_handler.get_connect()
    model = UserRepository(conn)
    controller = BalanceEditor(model)
    view = BalanceEditView(controller)
    return view