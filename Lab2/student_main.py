
def task1(number1, znak, number2):
    if znak == '>':
        result = number1 > number2
    elif znak == '<':
        result = number1 < number2
    elif znak == '>=':
        result = number1 >= number2
    elif znak == '<=':
        result = number1 <= number2
    elif znak == '==':
        result = number1 == number2
    elif znak == '!=':
        result = number1 != number2
    print(f"Результат порівняння: {result}")
    return result

def task2(text, number):
    if len(text) > number:
        length = len(text)
    else:
        length = number
    print(f"Довжина тексту: {length}")
    return length

def task3(number1, number2, number3):
    result = number1 == number2 == number3
    print(f"Результат порівняння: {result}")
    return result

# Приклад використання
task1_result = task1(10, '>', 5)
task2_result = task2("Hello, world!", 7)
task3_result = task3(5, 5, 5)