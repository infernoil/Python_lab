Лабораторна робота №9: Регулярні вирази
___
Мета роботи: Дослідити як працюють регулярни вирази
___
Опис завдання:
```Python
Write a def(task1) regular expression that matches a string containing only lowercase letters and digits. Input: "hello123" Output: True
Write a def(task2) regular expression that matches a string containing at least one uppercase letter. Input: "Hello" Output: True
Write a def(task3) regular expression that matches a string containing a valid IPv4 address. Input: "192.168.1.1" Output: True
Write a def(task4) regular expression that matches a string containing a valid time in the format of "HH:MM:SS". Input: "12:34:56" Output: True
Write a def(task5) regular expression that matches a string containing a valid US postal code in the format of "NNNNN" or "NNNNN-NNNN". Input: "12345" or "12345-6789" Output: True
Write a def(task6) regular expression that matches a string containing a valid username, with the following criteria: only contains lowercase letters, numbers, underscores, and hyphens, and is between 6 and 12 characters long. Input: "john_doe-123" Output: True
Write a def(task7) regular expression that matches a string containing a valid credit card number (either 15 or 16 digits, starting with either 4, 5, or 6). Input: "4512-3456-7890-1234" Output: True
Write a def(task8) regular expression that matches a string containing a valid social security number (in the format of ###-##-####). Input: "123-45-6789" Output: True
Write a def(task9) regular expression that matches a string containing a valid password, with the following criteria: at least one uppercase letter, one lowercase letter, one digit, one special character (@, #, $, or %), and at least 8 characters long. Input: "Passw0rd#" Output: True
Write a def(task10) regular expression that matches a string containing a valid IPv6 address. Input: "2001:0db8:85a3:0000:0000:8a2e:0370:7334" Output: True.
```
___
Виконання роботи:
```Python
import re

def task1(s):
    return bool(re.match("^[a-z0-9]+$", s))

def task2(s):
    return bool(re.search("[A-Z]", s))

def task3(s):
    return bool(re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s))

def task4(s):
    return bool(re.match("^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", s))

def task5(s):
    return bool(re.match(r"^\d{5}(-\d{4})?$", s))

def task6(s):
    return bool(re.match("^[a-z0-9_-]{6,12}$", s))

def task7(s):
    return bool(re.match(r"^(4|5|6)\d{3}-?\d{4}-?\d{4}-?\d{4}$", s.replace("-", "")))

def task8(s):
    return bool(re.match(r"^\d{3}-\d{2}-\d{4}$", s))

def task9(s):
    return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$", s))
print(task1("abc123"))  # True
print(task1("ABC123"))  # False
print(task2("abc"))     # False
print(task2("Abc"))     # True
print(task3("192.168.1.1"))  # True
print(task3("256.256.256.256"))  # False
print(task4("23:59:59"))  # True
print(task4("24:00:00"))  # False
print(task5("12345"))      # True
print(task5("12345-6789")) # True
print(task5("123456"))     # False
print(task6("abc123"))   # True
print(task6("abc"))      # False
print(task6("abc1234567890"))  # False
print(task7("4123-4567-8901-2345"))  # True
print(task7("5123456789012345"))     # True
print(task7("3123456789012345"))     # False
print(task8("123-45-6789"))  # True
print(task8("123-456-789"))  # False
print(task9("Password1@"))  # True
print(task9("password"))    # False

# Проект з перевірки рядків за допомогою регулярних виразів

## Опис

Цей проект містить функції для перевірки рядків за допомогою регулярних виразів. Кожна функція перевіряє, чи відповідає заданий рядок певному шаблону.

## Структура проекту

- `main.py`: Основний файл проекту, який містить всі функції перевірки рядків.

## Функції

1. `task1(s)`: Перевіряє, чи містить рядок лише малі літери та цифри.
2. `task2(s)`: Перевіряє, чи містить рядок хоча б одну велику літеру.
3. `task3(s)`: Перевіряє, чи є рядок дійсною IPv4-адресою.
4. `task4(s)`: Перевіряє, чи є рядок дійсним часом у форматі HH:MM:SS.
5. `task5(s)`: Перевіряє, чи є рядок дійсним поштовим індексом США.
6. `task6(s)`: Перевіряє, чи відповідає рядок шаблону: малі літери, цифри, нижнє підкреслення або дефіс, довжина від 6 до 12 символів.
7. `task7(s)`: Перевіряє, чи відповідає рядок шаблону номера кредитної картки.
8. `task8(s)`: Перевіряє, чи є рядок дійсним номером соціального страхування США.
9. `task9(s)`: Перевіряє, чи відповідає рядок шаблону пароля.
```
Структура проекту: my_project/
│
├── main.py
└── README.md
___
Результати:
```Python
True
False
False
True
True
False
True
False
True
True
False
True
False
False
True
True
False
True
False
True
False
___
Висновки:
Цей проект демонструє використання регулярних виразів для перевірки відповідності рядків певним шаблонам. Функції легко використовувати та інтегрувати в інші проекти для валідації даних.


___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.