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