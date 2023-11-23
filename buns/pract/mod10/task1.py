import re
import doctest


def validate_password(password):
        """
        Примеры:
        >>> validate_password("пароль")
        False
        >>> validate_password("password")
        False
        >>> validate_password("Fпроs2rВ")
        False
        >>> validate_password("qwerty")
        False
        >>> validate_password("1wE^E")
        False
        >>> validate_password("lOngPa$$$W0Rd")
        False
        >>> validate_password("AnotherWeakPassword")
        False
        >>> validate_password("rtG3FG!Tr^e")
        True
        >>> validate_password("aA1!*!1Aa")
        True
        >>> validate_password("oF^a1D@y5e6")
        True
        >>> validate_password("enroi#$rkdeR#$092uWedchf34tguv394h")
        True
        """
        pattern = r"^(?!.*(.)\1{2})(?=.*\d)(?=.*[A-Z])(?=.*[$%^@#&*!?\w])[A-Za-z\d$%^@#&*!?]{6,}$"
        return bool(re.match(pattern, password))

if __name__ == "__main__":
    doctest.testmod()

