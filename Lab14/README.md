Лабораторна робота №14: Boolean Expressions and Conditional
Statements
___
Мета роботи:
```
In this lab, you will write a script to analyze Boolean expressions and use
conditional statements to solve various problems. Each task will require you to
manipulate and evaluate Boolean conditions in different contexts.
```
___
Опис завдання:
```Python
Task 1: Basic Boolean Operations
Write a function check_truth that takes three boolean parameters ( a , b , c )
and returns the result of the expression (a and b) or c .
Example of function usage:
Task 2: Logical Equivalence
Write a function logical_equivalence that takes two boolean parameters and
returns True if they are logically equivalent, otherwise False .
Example of function usage:
Task 3: Exclusive Or (XOR)
Write a function xor that takes two boolean arguments and returns True if
exactly one of the arguments is True .
Example of function usage:
print(check_truth(True, False, True)) # True
print(logical_equivalence(True, True)) # True
print(logical_equivalence(True, False)) # False
Task 4: Conditional Greeting
Write a function greet that takes a boolean value. If True , the function should
return "Hello, World!", otherwise it should return "Goodbye, World!".
Example of function usage:
Task 5: Nested Conditions
Write a function nested_condition that takes three integers ( x , y , z ). The
function should return "All same" if all three are equal, "All different" if they are all
different, and "Neither" otherwise.
Example of function usage:
Task 6: Conditional Counting
Write a function count_true that accepts a list of boolean values and returns the
count of how many are True .
Example of function usage:
print(xor(True, False)) # True
print(xor(True, True)) # False
print(greet(True)) # Hello, World!
print(greet(False)) # Goodbye, World!
print(nested_condition(3, 3, 3)) # All same
print(nested_condition(3, 4, 5)) # All different
Task 7: Boolean Parity
Write a function parity that accepts an integer and returns True if the number
of 1 s in the binary representation of the number is even, otherwise False .
Example of function usage:
Task 8: Majority Vote
Write a function majority_vote that takes three boolean inputs and returns
True if more than half of them are True , otherwise False .
Example of function usage:
Task 9: Boolean Switch
Write a function switch that takes a boolean value and returns its opposite.
Example of function usage:
Task 10: Ternary Operator Simulation
Write a function ternary_check that simulates a ternary operator. It takes three
parameters: a boolean condition, a result if true, and a result if false. It returns the
print(count_true([True, False, True, False, True])) # 3
print(parity(3)) # False (binary 11)
print(majority_vote(True, True, False)) # True
print(switch(True)) # False
corresponding result based on the condition.
Example of function usage:
Task 11: Validate Combination
Write a function validate that takes three booleans ( x , y , z ) and returns
True if x is True or both y and z are True , otherwise False .
Example of function usage:
Task 12: Condition Chain
Write a function chain_check that evaluates a sequence of conditions. It takes
three integers and returns "Increasing" if they are in strictly increasing order,
"Decreasing" if in strictly decreasing order, or "Neither" otherwise.
Example of function usage:
Task 13: Boolean Filter
Write a function filter_true that takes a list of boolean values and returns a
new list containing only the True values.
Example of function usage:
print(ternary_check(True, "Yes", "No")) # Yes
print(validate(True, False, True)) # True
print(chain_check(1, 2, 3)) # Increasing
print(chain_check(3, 2, 1)) # Decreasing
Task 14: Conditional Multiplexer
Write a function multiplexer that takes four parameters: three boolean inputs
and one integer. If the first boolean is True , return double the integer. If the
second is True , return triple the integer. If the third is True , return the integer
minus five. If none are True , return the integer unchanged.
Example of function usage:
print
 
(filter_true([True, False, True, False])) # [True, True]
print(multiplexer(False, False, True, 10)) # 5
```
___
Виконання роботи:
```Python
# Task 1: Basic Boolean Operations
def check_truth(a, b, c):
    return (a and b) or c

print(check_truth(True, False, True))  # Output: True
print(check_truth(False, False, True))  # Output: True
print(check_truth(False, False, False))  # Output: False

# Task 2: Logical Equivalence
def logical_equivalence(a, b):
    return a == b

print(logical_equivalence(True, True))  # Output: True
print(logical_equivalence(True, False))  # Output: False

# Task 3: Exclusive Or (XOR)
def xor(a, b):
    return a != b

print(xor(True, False))  # Output: True
print(xor(True, True))  # Output: False

# Task 4: Conditional Greeting
def greet(boolean_value):
    if boolean_value:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

print(greet(True))  # Output: Hello, World!
print(greet(False))  # Output: Goodbye, World!

# Task 5: Nested Conditions
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"

print(nested_condition(1, 1, 1))  # Output: All same
print(nested_condition(1, 2, 3))  # Output: All different
print(nested_condition(1, 2, 1))  # Output: Neither

# Task 6: Conditional Counting
def count_true(boolean_list):
    return sum(boolean_list)

print(count_true([True, False, True, True]))  # Output: 3
print(count_true([False, False, False]))  # Output: 0

# Task 7: Boolean Parity
def parity(number):
    return bin(number).count('1') % 2 == 0

print(parity(3))  # Output: False (11 in binary has odd number of 1's)
print(parity(4))  # Output: True (100 in binary has even number of 1's)

# Task 8: Majority Vote
def majority_vote(a, b, c):
    return sum([a, b, c]) > 1

print(majority_vote(True, False, True))  # Output: True
print(majority_vote(False, False, True))  # Output: False

# Task 9: Boolean Switch
def switch(boolean_value):
    return not boolean_value

print(switch(True))  # Output: False
print(switch(False))  # Output: True

# Task 10: Ternary Operator Simulation
def ternary_check(condition, result_if_true, result_if_false):
    if condition:
        return result_if_true
    else:
        return result_if_false

print(ternary_check(True, "Yes", "No"))  # Output: Yes
print(ternary_check(False, "Yes", "No"))  # Output: No

# Task 11: Validate Combination
def validate(x, y, z):
    return x or (y and z)

print(validate(False, True, True))  # Output: True
print(validate(False, False, True))  # Output: False

# Task 12: Condition Chain
def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

print(chain_check(1, 2, 3))  # Output: Increasing
print(chain_check(3, 2, 1))  # Output: Decreasing
print(chain_check(1, 3, 2))  # Output: Neither

# Task 13: Boolean Filter
def filter_true(boolean_list):
    return [item for item in boolean_list if item]

print(filter_true([True, False, True, False]))  # Output: [True, True]

# Task 14: Conditional Multiplexer
def multiplexer(bool1, bool2, bool3, integer):
    if bool1:
        return integer * 2
    elif bool2:
        return integer * 3
    elif bool3:
        return integer - 5
    else:
        return integer

print(multiplexer(True, False, False, 10))  # Output: 20
print(multiplexer(False, True, False, 10))  # Output: 30
print(multiplexer(False, False, True, 10))  # Output: 5
print(multiplexer(False, False, False, 10))  # Output: 10

```
___
Структура проекту: my_project/
│
├── main.py
└── README.md
___
Результати:
```Python
True
True
False
True
False
True
False
Hello, World!
Goodbye, World!
All same
All different
Neither
3
0
True
False
True
False
False
True
Yes
No
True
False
Increasing
Decreasing
Neither
[True, True]
20
30
5
10
```
___
Висновки:
Проект включає набір завдань, що охоплюють різні аспекти логічних операцій, умовних перевірок та булевих операцій в Python. Кожне завдання реалізоване у вигляді окремої функції, що спрощує розуміння та тестування коду.
___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.