from password import create, is_password_correct
from string import ascii_lowercase, ascii_uppercase, digits


def test_password_generation():
    alphabets = [
        ascii_lowercase,
        ascii_uppercase
    ]
    password = create(32, alphabets)

    assert len(password) == 32


def test_password_not_correct():
    password = "123456a"

    assert not is_password_correct(password, [
        ascii_uppercase,
        ascii_lowercase,
        digits
    ])

def test_password_correct():
    password = "1234aB"

    assert is_password_correct(password, [
        ascii_uppercase,
        ascii_lowercase,
        digits
    ])