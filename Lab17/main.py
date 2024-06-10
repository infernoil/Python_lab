import itertools


# Task 1: Create a generator to iterate over a list of numbers.
def number_generator(numbers):
    for number in numbers:
        yield number


# Task 2: Develop a generator that yields even numbers from a given range.
def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number


# Task 3: Implement a generator to yield odd numbers within a specified range.
def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number


# Task 4: Write a generator that produces Fibonacci numbers.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Task 5: Create a generator that yields prime numbers up to a given limit.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_number_generator(limit):
    for number in range(2, limit + 1):
        if is_prime(number):
            yield number


# Task 6: Develop a generator to traverse a binary tree in pre-order.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)


# Task 7: Implement a generator for in-order traversal of a binary tree.
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)


# Task 8: Write a generator for post-order traversal of a binary tree.
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val


# Task 9: Create a generator to traverse a graph using depth-first search (DFS).
def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
            stack.extend(reversed(graph[node]))


# Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            yield node
            queue.extend(graph[node])


# Task 11: Implement a generator that yields the keys of a dictionary.
def dict_keys_generator(d):
    for key in d.keys():
        yield key


# Task 12: Write a generator that yields the values of a dictionary.
def dict_values_generator(d):
    for value in d.values():
        yield value


# Task 13: Create a generator to iterate over key-value pairs of a dictionary.
def dict_items_generator(d):
    for item in d.items():
        yield item


# Task 14: Develop a generator that yields lines from a file one by one.
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


# Task 15: Implement a generator to iterate over words in a text file.
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word


# Task 16: Write a generator that yields characters from a string one by one.
def string_chars_generator(s):
    for char in s:
        yield char


# Task 17: Create a generator to yield unique elements from a list.
def unique_elements_generator(lst):
    seen = set()
    for element in lst:
        if element not in seen:
            seen.add(element)
            yield element


# Task 18: Develop a generator that yields elements of a list in reverse order.
def reverse_list_generator(lst):
    for element in reversed(lst):
        yield element


# Task 19: Implement a generator to yield the Cartesian product of two lists.
def cartesian_product_generator(list1, list2):
    for element1 in list1:
        for element2 in list2:
            yield (element1, element2)


# Task 20: Write a generator that yields permutations of a list.
def permutations_generator(lst):
    for perm in itertools.permutations(lst):
        yield perm


# Task 21: Create a generator to yield combinations of a list of elements.
def combinations_generator(lst):
    for i in range(1, len(lst) + 1):
        for comb in itertools.combinations(lst, i):
            yield comb


# Task 22: Develop a generator to iterate over a list of tuples.
def tuple_list_generator(lst):
    for tup in lst:
        yield tup


# Task 23: Implement a generator that yields elements from multiple lists in parallel.
def parallel_lists_generator(*lists):
    for elements in zip(*lists):
        yield elements


# Task 24: Write a generator that yields elements from a nested list (flattening the list).
def flatten_list_generator(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list_generator(element)
        else:
            yield element


# Task 25: Create a generator to yield elements from a nested dictionary.
def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)


# Task 26: Develop a generator to yield powers of 2 up to a given number.
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i


# Task 27: Implement a generator that yields powers of a given base up to a specified limit.
def powers_of_base_generator(base, limit):
    power = 0
    result = 1
    while result <= limit:
        yield result
        power += 1
        result = base ** power


# Task 28: Write a generator to yield the squares of numbers in a given range.
def squares_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 2


# Task 29: Create a generator to yield cubes of numbers in a specified range.
def cubes_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 3


# Task 30: Develop a generator that yields factorials of numbers up to a given limit.
def factorials_generator(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    for number in range(n + 1):
        yield factorial(number)


# Task 31: Implement a generator to yield numbers in the Collatz sequence.
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n


# Task 32: Write a generator that yields numbers in a geometric progression.
def geometric_progression_generator(initial_term, common_ratio, limit):
    term = initial_term
    while term <= limit:
        yield term
        term *= common_ratio


# Task 33: Create a generator to yield numbers in an arithmetic progression.
def arithmetic_progression_generator(initial_term, common_difference, limit):
    term = initial_term
    while term <= limit:
        yield term
        term += common_difference


# Task 34: Develop a generator that yields the running sum of a list of numbers.
def running_sum_generator(lst):
    running_sum = 0
    for number in lst:
        running_sum += number
        yield running_sum


# Task 35: Implement a generator to yield the running product of a list of numbers.
def running_product_generator(lst):
    running_product = 1
    for number in lst:
        running_product *= number
        yield running_product


if __name__ == "__main__":
    # Example usages
    gen = number_generator([1, 2, 3, 4, 5])
    print(next(gen))  # 1
    print(next(gen))  # 2

    gen = even_number_generator(1, 10)
    print(next(gen))  # 2
    print(next(gen))  # 4

    gen = odd_number_generator(1, 10)
    print(next(gen))  # 1
    print(next(gen))  # 3

    gen = fibonacci_generator()
    print(next(gen))  # 0
    print(next(gen))  # 1

    gen = prime_number_generator(10)
    print(next(gen))  # 2
    print(next(gen))  # 3

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    gen = pre_order_traversal(root)
    print(next(gen))  # 1
    print(next(gen))  # 2

    gen = in_order_traversal(root)
    print(next(gen))  # 2
    print(next(gen))  # 1

    gen = post_order_traversal(root)
    print(next(gen))  # 2
    print(next(gen))  # 3

    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
    gen = dfs_traversal(graph, 'A')
    print(next(gen))  # A
    print(next(gen))  # B

    gen = bfs_traversal(graph, 'A')
    print(next(gen))  # A
    print(next(gen))  # B

    d = {'a': 1, 'b': 2, 'c': 3}
    gen = dict_keys_generator(d)
    print(next(gen))  # 'a'
    print(next(gen))  # 'b'

    gen = dict_values_generator(d)
    print(next(gen))  # 1
    print(next(gen))  # 2

    gen = dict_items_generator(d)
    print(next(gen))  # ('a', 1)
    print(next(gen))  # ('b', 2)

    # file_lines_generator and file_words_generator examples assume a file exists at the given path
    # gen = file_lines_generator('example.txt')
    # print(next(gen))
    # print(next(gen))

    # gen = file_words_generator('example.txt')
    # print(next(gen))
    # print(next(gen))

    gen = string_chars_generator("hello")
    print(next(gen))  # 'h'
    print(next(gen))  # 'e'

    gen = unique_elements_generator([1, 2, 2, 3, 4, 4, 5])
    print(next(gen))  # 1
    print(next(gen))  # 2

    gen = reverse_list_generator([1, 2, 3, 4, 5])
    print(next(gen))  # 5
    print(next(gen))  # 4

    gen = cartesian_product_generator([1, 2], ['a', 'b'])
    print(next(gen))  # (1, 'a')
    print(next(gen))  # (1, 'b')

    gen = permutations_generator([1, 2, 3])
    print(next(gen))  # (1, 2, 3)
    print(next(gen))  # (1, 3, 2)

    gen = combinations_generator([1, 2, 3])
    print(next(gen))  # (1,)
    print(next(gen))  # (2,)

    gen = tuple_list_generator([(1, 2), (3, 4), (5, 6)])
    print(next(gen))  # (1, 2)
    print(next(gen))  # (3, 4)

    gen = parallel_lists_generator([1, 2, 3], ['a', 'b', 'c'])
    print(next(gen))  # (1, 'a')
    print(next(gen))  # (2, 'b')

    gen = flatten_list_generator([1, [2, [3, 4], 5], 6])
    print(next(gen))  # 1
    print(next(gen))  # 2

    gen = nested_dict_generator({'a': {'b': 1, 'c': 2}, 'd': 3})
    print(next(gen))  # ('b', 1)
    print(next(gen))  # ('c', 2)

    gen = powers_of_two_generator(4)
    print(next(gen))  # 1
    print(next(gen))  # 2

    gen = powers_of_base_generator(3, 81)
    print(next(gen))  # 1
    print(next(gen))  # 3

    gen = squares_generator(1, 5)
    print(next(gen))  # 1
    print(next(gen))  # 4

    gen = cubes_generator(1, 4)
    print(next(gen))  # 1
    print(next(gen))  # 8

    gen = factorials_generator(4)
    print(next(gen))  # 1
    print(next(gen))  # 1

    gen = collatz_sequence_generator(6)
    print(next(gen))  # 6
    print(next(gen))  # 3

    gen = geometric_progression_generator(2, 3, 20)
    print(next(gen))  # 2
    print(next(gen))  # 6

    gen = arithmetic_progression_generator(2, 3, 20)
    print(next(gen))  # 2
    print(next(gen))  # 5

    gen = running_sum_generator([1, 2, 3, 4])
    print(next(gen))  # 1
    print(next(gen))  # 3

    gen = running_product_generator([1, 2, 3, 4])
    print(next(gen))  # 1
    print(next(gen))  # 2
