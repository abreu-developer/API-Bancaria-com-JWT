from .jwt_handler import JwtHandler


def test_jwt_handler():
    jwt_handler = JwtHandler()

    body = {
        "username": "olamundo",
        "aqui": "estouaqui",
        "lalala": "lalala"
    }

    token = jwt_handler.create_jwt_token(body)
    token_info = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_info["username"] == body["username"]
    assert token_info["lalala"] == body["lalala"]