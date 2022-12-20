from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum


class Chars(Enum):

    btn_lower = ascii_lowercase
    btn_upper = ascii_uppercase
    btn_digits = digits
    btn_special = punctuation


CHARACTER_NUMBER = {'btn_lower': len(Chars.btn_lower.value), 'btn_upper': len(Chars.btn_upper.value), 'btn_digits': len(Chars.btn_digits.value),'btn_special': len(Chars.btn_special.value)
}

GENERATE_PASSWORD = (
    'btn_refresh', 'btn_lower', 'btn_upper', 'btn_digits', 'btn_special'
)
