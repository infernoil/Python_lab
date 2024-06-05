# Task 1: Class Creation
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Task 2: Create Method
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Task 3: Inheritance
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

# Task 4: Polymorphism
class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

# Task 5: Encapsulation
class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected

# Task 6: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Task 7: AverageCalculator
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

    dog = Dog("Buddy", "Woof", "Labrador")
    print(dog.make_sound())  # Buddy: Woof
sparrow = Sparrow()
penguin = Penguin()
print(sparrow.fly())  # Sparrow flies high
print(penguin.fly())  # Penguin cannot fly
obj = Encapsulation("public", "private", "protected")
print(obj.public)  # public
rectangle = Rectangle(4, 5)
print(rectangle.calculate_perimeter())  # 18
calculator = AverageCalculator([1, 2, 3, 4, 5])
print(calculator.calculate_average())  # 3.0
