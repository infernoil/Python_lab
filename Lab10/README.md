Лабораторна робота 10 №: OOP in Python
___

Мета роботи:
Pay Attention
In this lab, you need to create classes instead of functions
___
Опис завдання:
```Python
Task 1: Class Creation
Create a Python class named “Student” with the following attributes: - name -
age - grade
Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
Task 2: Create Method
Add a method named display_info() to the Student class that prints the
student’s name, age, and grade in the format “Name: [name], Age: [age],
Grade: [grade]”.
Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info()) # Name: Ivan, Age: 30, Grade: 2
Task 3: Inheritance
Create two classes: Animal and Dog. Animal should have attributes name
and sound. Add a make_sound() method to Animal that returns the string
“[name]: [sound]”. Dog should inherit from Animal and have an additional
attribute breed.
Example of class usage:
animal = Animal(name="Lala", sound="
```
___
Виконання роботи:
```Python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
student = Student("Alice", 20, "A")
print(student.display_info())  # Name: Alice, Age: 20, Grade: A
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed
dog = Dog("Buddy", "Woof", "Labrador")
print(dog.make_sound())  # Buddy: Woof
class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"
sparrow = Sparrow()
penguin = Penguin()
print(sparrow.fly())  # Sparrow flies high
print(penguin.fly())  # Penguin cannot fly
class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected
obj = Encapsulation("public", "private", "protected")
print(obj.public)  # public
# print(obj._private)  # Неправильно: Це вважається приватним атрибутом
# print(obj.__protected)  # Неправильно: Це вважається захищеним атрибутом
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(4, 5)
print(rectangle.calculate_perimeter())  # 18
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)
calculator = AverageCalculator([1, 2, 3, 4, 5])
print(calculator.calculate_average())  # 3.0

# Проект: Основи ООП

## Опис

Цей проект демонструє основні принципи об'єктно-орієнтованого програмування (ООП) за допомогою Python.

## Структура проекту

- `main.py`: Основний файл проекту, який містить всі класи та їх методи.

## Класи та їх методи

### 1. Клас `Student`
- `__init__(self, name, age, grade)`: Ініціалізує атрибути студента.
- `display_info(self)`: Повертає рядок з інформацією про студента.

### 2. Клас `Animal` та його підклас `Dog`
- `__init__(self, name, sound)`: Ініціалізує атрибути тварини.
- `make_sound(self)`: Повертає рядок з звуком, який видає тварина.
- `super().__init__(name, sound)`: Викликає конструктор базового класу для ініціалізації атрибутів `name` та `sound`.

### 3. Класи `Bird`, `Sparrow` та `Penguin`
- `fly(self)`: Абстрактний метод в базовому класі `Bird`.

### 4. Клас `Encapsulation`
- `__init__(self, public, _private, __protected)`: Ініціалізує атрибути з різними рівнями доступу.

### 5. Клас `Rectangle`
- `__init__(self, width, height)`: Ініціалізує атрибути ширини та висоти.
- `calculate_perimeter(self)`: Обчислює периметр прямокутника.

### 6. Клас `AverageCalculator`
- `__init__(self, numbers)`: Ініціалізує атрибут списку чисел.
- `calculate_average(self)`: Обчислює середнє значення списку чисел.

## Приклади використання

### Student
```python
student = Student("Alice", 20, "A")
print(student.display_info())  # Name: Alice, Age: 20, Grade: A
```
___
Структура проекту: my_project/
│
├── main.py
└── README.md
___
Результати:
```Python
Buddy: Woof
Sparrow flies high
Penguin cannot fly
public
18
3.0
```
___
Висновки:
Цей проект демонструє використання об'єктно-орієнтованих принципів у Python. Класи та методи можуть бути легко використані в інших проектах для реалізації базових ООП-концепцій.
___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.