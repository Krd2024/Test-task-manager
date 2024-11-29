def is_digit(string: str) -> bool:
    print(string)
    """
    Проверяет, состоит ли строка только из цифр
    после удаления всех пробелов.

    """
    return string.replace(" ", "").isdigit()
