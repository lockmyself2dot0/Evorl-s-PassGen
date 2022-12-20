from enum import IntEnum
from typing import List
from math import log2
import secrets


class StrengthToEntropy(IntEnum):
    Pathetic = 0
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120


def create(length: int, char_list: List[str]) -> str:
    """Генерация паоля и проверка на наличие символов из всех списков

    Args:
        length (int): длина пароля
        char_list (List[str]): список словарей, символы из которых надо использовать

    Returns:
        str: сгенерированный, проверенный пароль
    """
    password = ''.join(secrets.choice("".join(char_list)) for _ in range(length))
    while not is_password_correct(password, char_list):
        password = ''.join(secrets.choice("".join(char_list)) for _ in range(length))
    return password

def is_password_correct(password: str, char_list: List[str]) -> bool:
    """ Проверка пароля на наличие символов из всех списков

    Args:
        password (str): пароль
        char_list (List[str]): список словарей, знаки из которых надо использовать

    Returns:
        bool: правильный пароль или нет
    """
    for char in char_list:
        is_correct = False
        for value in char:
            if value in password:
                is_correct = True
                break
        if not is_correct:
            return False
    return True


def get_entro(length: int, char_numb: int) -> float:
    """Считает энтропию пароля

    Args:
        length (int): длина пороля
        char_numb (int): размер словоря из которого использованны символы

    Returns:
        float: количество бит энтропии
    """
    try:
        entro = length * log2(char_numb)
    except ValueError:
        return 0.0
    return round(entro, 2)