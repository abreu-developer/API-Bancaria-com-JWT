from .password_handler import PasswordHandler


def test_encrypt():
    my_pass = "1234"
    password_handler = PasswordHandler()

    hashed_pass = password_handler.encrypt_password(my_pass)
    password_cheker = password_handler.check_password(my_pass,hashed_pass)

    assert password_cheker