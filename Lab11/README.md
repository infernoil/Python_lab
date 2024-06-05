Лабораторна робота № 11: Advanced Working with Arrays of Numbers in Python
___
Мета роботи: Розв'язок завдань на масиви та матриці
___
Опис завдання:
```Python
Task 1: Sum of Squares
Create a function sum_of_squares that accepts an array of numbers and returns the sum of the squares of each number.
Example of function usage:
print(sum_of_squares([1, 2, 3])) # Output: 14 

Task 2: Filter and Sum
Create a function filter_and_sum that accepts an array of numbers and returns the sum of all the elements that are greater or equal than the average of the array.
Example of function usage:
print(filter_and_sum([1, 2, 3, 4, 10])) # Output: 14 

Task 3: Sort by Frequency
Create a function sort_by_frequency that sorts an array of numbers based on the frequency of each element from highest to lowest. If two numbers have the same frequency, the smaller number should come first.
Example of function usage:
print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6])) # Output: [4, 4, 4, 6, 6, 6, 2] 

Task 4: Find Missing Number
Create a function find_missing_number that finds the missing number in an array containing all integers from 1 to n except one. Assume the array has no duplicates.
Example of function usage:
print(find_missing_number([1, 2, 4, 5])) # Output: 3 

Task 5: Longest Consecutive Sequence
Create a function longest_consecutive that finds the length of the longest consecutive elements sequence in an unsorted array.
Example of function usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2])) # Output: 4 
Task 6: Rotate Array

Create a function rotate_array that rotates the array to the right by k steps, where k is non-negative.
Example of function usage:
print(rotate_array([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3] 
Task 7: Array of Products
Create a function array_of_products that calculates an array of products of all numbers except the one at the current index without using division.
Example of function usage:
print(array_of_products([1, 2, 3, 4])) # Output: [24, 12, 8, 6]
 
Task 8: Maximum Subarray Sum
Create a function max_subarray_sum that finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
Example of function usage:
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])) # Output: 6 

Task 9: Spiral Order Matrix
Create a function spiral_order that returns all elements of a 2D matrix in spiral order.
Example of function usage:
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5] 

Task 10: K Closest Points to Origin
Create a function k_closest_points that finds the k closest points to the origin (0, 0) in a 2D plane, given an array of coordinate points.
Example of function usage:
print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2)) # Output: [(1, 1), (1, 2)] :
```
___
Виконання роботи:
```Python
def task1(arr):
    return sum(x ** 2 for x in arr)
print(task1([1, 2, 3]))  # Output: 14
def task2(arr):
    if not arr:
        return 0
    avg = sum(arr) / len(arr)
    return sum(num for num in arr if num >= avg)
print(task2([1, 2, 3, 4, 5]))  # Output: 12
def task3(arr):
    if not arr:
        return []
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))
    return sorted_arr
print(task3([4, 4, 3, 3, 3, 2, 1]))  # Output: [3, 3, 3, 4, 4, 1, 2]
def task4(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number
print(task4([1, 2, 4, 5, 6]))  # Output: 3
def task5(nums):
    if not nums:
        return 0
    nums_set = set(nums)
    longest_streak = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak
print(task5([100, 4, 200, 1, 3, 2]))  # Output: 4
def task6(nums, k):
    if not nums:
        return []
    k %= len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums
print(task6([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    return result
print(task7([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
def task8(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
print(task8([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
def task9(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(task9(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
import math

def task10(points, k):
    distances = [(point, math.sqrt(point[0] ** 2 + point[1] ** 2)) for point in points]
    distances.sort(key=lambda x: x[1])
    return [point[0] for point in distances[:k]]
points = [(1, 3), (3, 4), (2, -1)]
k = 2
print(task10(points, k))  # Output: [(2, -1), (1, 3)]
# Проект: Розв'язок завдань на масиви та матриці

## Опис

Цей проект містить функції для виконання різних операцій з масивами та матрицями. Метою було реалізувати базові та розширені алгоритми для обробки даних.

## Вміст

1. **main.py** - Основний файл з функціями `task1` - `task10`.

## Функції

### task1

- **Призначення**: Обчислює суму квадратів елементів масиву.
```
___
Структура проекту: my_project/
│
├── main.py
└── README.md
___
Результати:
```Python
14
12
[3, 3, 3, 4, 4, 1, 2]
3
4
[5, 6, 7, 1, 2, 3, 4]
[24, 12, 8, 6]
[1, 2, 3, 6, 9, 8, 7, 4, 5]

```
___
Висновки:
Цей проект демонструє використання базових та розширених алгоритмів для обробки масивів та матриць у Python. Функції можуть бути використані в інших проектах для реалізації специфічних алгоритмічних рішень.
___
Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.