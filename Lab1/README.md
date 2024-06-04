Лабораторна робота №1: Введення в мову програмування Python
___

Мета роботи:
Дізнатися яке використання в повсякденному житті, переваги мови та недоліки
___
Опис завдання:
Завдання лабораторної роботи:
Завдання 0(приклад):
Функція task0 повинна повернути число 4.
Приклад написання коду:
def task0():
    return 4
Завдання 1: операції з рядками
Напишіть функцію task1 з аргументом, аргумент приймає строку (str) на вхід:
Знайти довжину цього відрізка та повернути значення.

	
Завдання 2: математичні оператори
Створіть функцію task2 яка приймає три аргументи(число,строка(+,-,/,//,**,*),число),
Функція має зробити математичну операцію з тих аргументів, приклад: число1 * число2 та повернути значення .

Завдання 3: 
Створіть функцію task3 яка приймає один аргумент (список(list[int]) знайти в цьому списку максимальне значения числа, та повернути це значення.
___
``` python
Виконання роботи:
Структура проекту: my_project/
│
├── main.py
└── README.md

Опис основних функцій та методів з поясненням їх роботи:
def task1(input_str):
    return len(input_str)

Призначення: Функція приймає рядок (string) як вхідний параметр і повертає його довжину.

Параметри:

input_str (string): Вхідний рядок, для якого потрібно визначити довжину.
Повертає: Ціле число (int), що дорівнює довжині вхідного рядка.

Приклад використання:
length = task1("Hello, world!")
print(length)  # Output: 13
Функція task2

def task2(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '**':
        result = num1 ** num2
    else:
        result = None  # У випадку непідтримуваного оператора

    return result
Призначення: Функція приймає два числа та оператор як вхідні параметри і виконує відповідну математичну операцію між цими числами.

Параметри:

num1 (int або float): Перше число.
operator (string): Оператор, який визначає операцію ('+', '-', '*', '/', '//', '**').
num2 (int або float): Друге число.
Повертає: Результат математичної операції або None, якщо оператор не підтримується.

Приклад використання:
result = task2(10, '+', 5)
print(result)  # Output: 15

result = task2(10, '/', 2)
print(result)  # Output: 5.0
Функція task3

def task3(number_list):
    max_value = max(number_list)
    return max_value
Призначення: Функція приймає список чисел і повертає максимальне значення в цьому списку.

Параметри:

number_list (list): Список чисел (int або float).
Повертає: Максимальне число зі списку.

Приклад використання:
max_val = task3([1, 2, 3, 4, 5])
print(max_val)  # Output: 5

max_val = task3([-10, -5, 0, 5, 10])
print(max_val)  # Output: 10
README.md
markdown
```
# Опис проекту

Цей проект містить три основні функції: `task1`, `task2`, і `task3`, які виконують різні задачі.

## Файли

- `main.py`: Містить реалізацію основних функцій.
- `README.md`: Документація проекту.

## Функції

### task1

```python
def task1(input_str):
    return len(input_str)
Приймає рядок і повертає його довжину.

Приклад:
length = task1("Hello, world!")
print(length)  # Output: 13
task2
def task2(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '**':
        result = num1 ** num2
    else:
        result = None

    return result
Приймає два числа та оператор, виконує відповідну математичну операцію.

Приклад:

result = task2(10, '+', 5)
print(result)  # Output: 15

result = task2(10, '/', 2)
print(result)  # Output: 5.0
task3
def task3(number_list):
    max_value = max(number_list)
    return max_value
Приймає список чисел і повертає максимальне значення.

Приклад:

max_val = task3([1, 2, 3, 4, 5])
print(max_val)  # Output: 5

max_val = task3([-10, -5, 0, 5, 10])
print(max_val)  # Output: 10
___
Результати:
Length of 'Hello, world!': 13
Result of 10 + 5: 15
Result of 10 / 2: 5.0
Result of 5 ** 3: 125
Max value in [1, 2, 3, 4, 5]: 5
Max value in [-10, -5, 0, 5, 10]: 10
```
___
Висновки:
Мета роботи була досягнута без видемих проблем.
___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.