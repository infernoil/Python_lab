# Завдання 1
def task1(my_list):
    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append(["Прізвище", "Ім'я"])
    list_length = len(my_list)
    print("Результати для завдання 1:")
    print("my_list:", my_list)
    print("min_element:", min_element)
    print("max_element:", max_element)
    print("list_length:", list_length)
    return my_list, min_element, max_element, list_length

# Завдання 2
def task2(A, B, C):
    total_cost = sum([b * c for b, c in zip(B, C)])
    average_price = sum(C) / len(C)
    max_stock_index = B.index(max(B))
    most_stocked_item = A[max_stock_index]
    return total_cost, average_price, most_stocked_item

# Завдання 3
def task3():
    A1 = [x for x in range(1, 26)]
    A2 = [x for x in range(-25, 0)]
    return A1, A2

# Завдання 4
def task4(my_string):
    count_a = my_string.count('a')
    return count_a

# Завдання 5
def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(my_string.split())
    return modified_str, word_count

# Завдання 6
def task6():
    total_sum = sum(range(1, 6))
    return total_sum

# Завдання 7
def task7(my_list):
    result = [num for num in my_list if num % 7 == 0 and num % 5 == 0]
    return result

# Приклад використання:
if __name__ == "__main__":
    # Завдання 1
    my_list = [0, 1, 2, 3, 4]
    my_list, min_element, max_element, list_length = task1(my_list)
    print("-" * 50)

    # Завдання 2
    A = ["товар1", "товар2", "товар3"]
    B = [10, 20, 30]
    C = [5, 10, 15]
    total_cost, average_price, most_stocked_item = task2(A, B, C)
    print("Результати для завдання 2:")
    print("total_cost:", total_cost)
    print("average_price:", average_price)
    print("most_stocked_item:", most_stocked_item)
    print("-" * 50)

    # Завдання 3
    A1, A2 = task3()
    print("Результати для завдання 3:")
    print("A1:", A1)
    print("A2:", A2)
    print("-" * 50)

    # Завдання 4
    my_string = "Це текст з декількома символами 'a'"
    count_a = task4(my_string)
    print("Результат для завдання 4:")
    print("Кількість символів 'a' у тексті:", count_a)
    print("-" * 50)

    # Завдання 5
    my_string = "GOOD GOOD GOOD GOOD"
    modified_str, word_count = task5(my_string)
    print("Результати для завдання 5:")
    print("modified_str:", modified_str)
    print("word_count:", word_count)
    print("-" * 50)

    # Завдання 6
    total_sum = task6()
    print("Результат для завдання 6:")
    print("total_sum:", total_sum)
    print("-" * 50)

    # Завдання 7
    my_list = [35, 70, 14, 10, 25]
    result = task7(my_list)
    print("Результат для завдання 7:")
    print("result:", result)
    print("-" * 50)

