def is_digit(string: str) -> bool:
    print(string)
    """
    Проверяет, состоит ли строка только из цифр
    после удаления всех пробелов.

    """
    return string.replace(" ", "").isdigit()


def get_valid_input(prompt: str, validator: callable, error_message: str) -> str:
    """
    Функция будет продолжать запрашивать ввод у пользователя до тех пор,
    пока введенные данные не пройдут валидатор.

    - 'prompt' (str): Сообщение, которое будет выведено пользователю для запроса ввода.
    - 'validator' (function): Функция-валидатор, которая будет проверять введенные данные.
      Валидатор должен возвращать 'True', если данные корректны, и 'False', если некорректны.
    - 'error_message' (str): Сообщение, которое будет выведено в случае ошибки (если данные не прошли валидацию).

    """

    while True:
        value = input(prompt)  # Запрашивает ввод у пользователя
        if validator(value):  # Проверяет данные с помощью валидатора
            return " ".join(
                value.split()
            )  # Убирает лишние пробелы и возвращаем корректный ввод
        print(error_message)  # Если данные некорректные, выводит сообщение об ошибке
