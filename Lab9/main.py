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
