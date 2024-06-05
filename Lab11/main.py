import math  # task10


def task1(arr):
    return sum(x ** 2 for x in arr)


def task2(arr):
    if not arr:
        return 0
    avg = sum(arr) / len(arr)  #
    return sum(num for num in arr if num >= avg)


def task3(arr):
    if not arr:
        return []
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))

    return sorted_arr


def task4(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number


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


def task6(nums, k):
    if not nums:
        return []

    k %= len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums


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


def task8(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


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


def task10(points, k):
    distances = [(point, math.sqrt(point[0] ** 2 + point[1] ** 2)) for point in points]

    distances.sort(key=lambda x: x[1])
    return [point[0] for point in distances[:k]]
print(task1([1, 2, 3]))  # Output: 14
print(task2([1, 2, 3, 4, 5]))  # Output: 12
print(task3([4, 4, 3, 3, 3, 2, 1]))  # Output: [3, 3, 3, 4, 4, 1, 2]
print(task4([1, 2, 4, 5, 6]))  # Output: 3
print(task5([100, 4, 200, 1, 3, 2]))  # Output: 4
print(task6([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
print(task7([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(task9(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

