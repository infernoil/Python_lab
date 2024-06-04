def task1(input_str):
    return len(input_str)

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

def task3(number_list):
    max_value = max(number_list)
    return max_value

# Приклади використання з print

# task1 приклад
input_string = "Hello, world!"
length = task1(input_string)
print(f"Length of '{input_string}': {length}")

# task2 приклади
num1, operator, num2 = 10, '+', 5
result = task2(num1, operator, num2)
print(f"Result of {num1} {operator} {num2}: {result}")

num1, operator, num2 = 10, '/', 2
result = task2(num1, operator, num2)
print(f"Result of {num1} {operator} {num2}: {result}")

num1, operator, num2 = 5, '**', 3
result = task2(num1, operator, num2)
print(f"Result of {num1} {operator} {num2}: {result}")

# task3 приклад
number_list = [1, 2, 3, 4, 5]
max_val = task3(number_list)
print(f"Max value in {number_list}: {max_val}")

number_list = [-10, -5, 0, 5, 10]
max_val = task3(number_list)
print(f"Max value in {number_list}: {max_val}")
