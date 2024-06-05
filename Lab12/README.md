Лабораторна робота № 12: Lab12
___

Мета роботи: Використання вкладених списків для створення двовимірних структур даних і керування ними.
___
Опис завдання:
```Python
Task 1: Create a Matrix
Create a Python class Matrix that initializes a two-dimensional list with zeros.
The constructor should accept two parameters: rows and columns, indicating the
dimensions of the matrix.
Example of class usage:
Task 2: Add Elements to Matrix
Extend the Matrix class by adding a method add_element that adds an element
at a specific position (row, column).
Example of class usage:
Task 3: Sum of Rows
Add a method sum_of_rows to the Matrix class that returns a list of sums of
each row in the matrix.
Example of class usage:
matrix = Matrix(2, 3)
print(matrix.data) # [[0, 0, 0], [0, 0, 0]]
matrix = Matrix(2, 3)
matrix.add_element(1, 2, 10)
print(matrix.data) # [[0, 0, 10], [0, 0, 0]]
matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
Task 4: Matrix Transposition
Create a method transpose in the Matrix class that returns a new Matrix
object, which is the transpose of the original matrix.
Example of class usage:
Task 5: Multiply Matrices
Implement a method multiply_by in the Matrix class that accepts another
Matrix object and returns a new Matrix object that is the result of the multiplication
of the two matrices.
Example of class usage:
Task 6: Check Symmetric Matrix
Add a method is_symmetric to the Matrix class that checks if the matrix is
symmetric (i.e., the matrix is equal to its transpose).
Example of class usage:
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows()) # [15, 20]
matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data) # [[0, 0], [1, 0], [0, 2]]
matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data) # [[14, 0], [0, 0]]
Task 7: Rotate Matrix
Implement a method rotate_right in the Matrix class that rotates the matrix
90 degrees to the right.
Example of class usage:
Task 8: Flatten Matrix
Create a method flatten in the Matrix class that returns a single list containing
all elements of the matrix.
Example of class usage:
Task 9: Matrix from List
Add a static method from_list to the Matrix class that creates a matrix object
from a given list of lists.
Example of class usage:
matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric()) # True
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data) # [[3, 1], [4, 2]]
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten()) # [1, 2, 3, 4]
Task 10: Extract Diagonal
Create a method diagonal in the Matrix class that extracts the diagonal of a
square matrix as a list.
Example of class usage:
python
list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data) # [[1, 2], [3, 4]]
matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal()) # [1, 2, 3]
```
___
Виконання роботи:
```Python
class Matrix:
    #1 Task
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]
    #2 Task
    def add_element(self, row, column, value):
        self.data[row][column] = value
    #3 Task
    def sum_of_rows(self):
        return [sum(row) for row in self.data]
    #4 Task
    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows)
    #5 Task
    def multiply_by(self, other_matrix):
        if self.columns != other_matrix.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix")

        result = Matrix(self.rows, other_matrix.columns)
        for i in range(self.rows):
            for j in range(other_matrix.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other_matrix.data[k][j]
        return result
    #6 Task
    def is_symmetric(self):
        return self == self.transpose()
    #7 Task
    def rotate_right(self):
        self.data = [list(row) for row in zip(*self.data[::-1])]
        self.rows, self.columns = self.columns, self.rows
    #8 Task
    def flatten(self):
        return [element for row in self.data for element in row]
    #9 Task
    def diagonal(self):
        if self.rows != self.columns:
            raise ValueError("Matrix must be square to extract diagonal")
        return [self.data[i][i] for i in range(self.rows)]
    #10 Task
    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.add_element(i, j, list_of_lists[i][j])
        return matrix

m = Matrix(3, 3)
m.add_element(1, 1, 5)
sums = m.sum_of_rows()
t = m.transpose()
m1 = Matrix(2, 3)
m2 = Matrix(3, 2)
result = m1.multiply_by(m2)
symmetric = m.is_symmetric()
m.rotate_right()
flat_list = m.flatten()
diag = m.diagonal()
list_of_lists = [[1, 2], [3, 4]]
m = Matrix.from_list(list_of_lists)

# Проект: Клас Matrix

## Опис

Цей проект містить клас `Matrix`, який реалізує різноманітні операції з матрицями, такі як додавання елементів, обчислення сум рядків, транспонування, множення матриць, перевірка на симетричність, обертання, розгортання у список, отримання діагоналі та створення матриці з списку списків.

## Вміст

1. **main.py** - Основний файл з класом `Matrix`.

## Функції

### `__init__(self, rows, columns)`

- Ініціалізує матрицю заданих розмірів з нулями.
```
___
Структура проекту: my_project/
│
├── main.py
└── README.md
___
Результати:
___
Висновки:
Цей проект демонструє реалізацію класу Matrix та його методів для роботи з матрицями у Python. Клас може бути використаний для різноманітних обчислювальних задач та алгоритмів, що включають роботу з матрицями.
___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.