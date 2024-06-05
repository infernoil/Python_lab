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
