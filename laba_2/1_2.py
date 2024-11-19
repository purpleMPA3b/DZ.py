import random
import time

"""сортировка пузырьком по убыванию"""
def bubbleteea(arr):
    """Сортирует массив по убыванию с помощью пузырьковой сортировки."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  #Обмен элементов для сортировки по убыванию
    return arr

"""быстрая сортировка с составными ключами"""
def sort_and_key(arr, key_func=lambda x: x, reverse=False):
    """Сортирует массив с использованием быстрой сортировки и составных ключей.
    Аргументы:
    arr: список для сортировки
    key_func: функция для получения ключа сортировки
    reverse: если True, сортирует по убыванию
    """
    if len(arr) <= 1:
        return arr
    pivot = key_func(arr[len(arr) // 2])  # Опорный элемент
    less = [x for x in arr if key_func(x) < pivot] if not reverse else [x for x in arr if key_func(x) > pivot]
    equal = [x for x in arr if key_func(x) == pivot]
    greater = [x for x in arr if key_func(x) > pivot] if not reverse else [x for x in arr if key_func(x) < pivot]
    # Рекурсивная сортировка частей
    return sort_and_key(greater, key_func, reverse) + equal + sort_and_key(less, key_func, reverse)

"""массив случайных чисел от 0 до 1000000, размер 1кк"""
array_size = 10000
test_array = [random.randint(0, 1000000) for _ in range(array_size)]

"""копии массива для разных алгоритмов сортировки"""
array_for_bubble = test_array.copy()
array_for_quick = test_array.copy()

"""time --- пузырьковая сортировка по убыванию"""
start_time = time.time()
bubbleteea = bubbleteea(array_for_bubble)
bubbleteea = time.time() - start_time

"""time --- сортировка с составными ключами"""
start_time = time.time()
sort_and_key = sort_and_key(array_for_quick, key_func=lambda x: x, reverse=True)
sort_and_key = time.time() - start_time


"""результаты"""
print(f"Время быстрой сортировки с составными ключами по убыванию: {sort_and_key:.2f} секунд")
print(f"Время пузырьковой сортировки по убыванию: {bubbleteea:.2f} секунд")