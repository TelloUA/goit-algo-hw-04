import timeit
from random import randint

def merge_sort(arr):
    # Якщо довжина масиву менше або дорівнює 1, повертаємо масив як є
    if len(arr) <= 1:
        return arr

    # Визначаємо середину масиву
    mid = len(arr) // 2
    # Ділимо масив на ліву і праву половини
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Зливаємо дві відсортовані половини
    return merge(left_half, right_half)

# Функція злиття двох відсортованих масивів
def merge(left, right):
    result = []  # Результуючий масив
    left_index, right_index = 0, 0  # Індекси для лівого і правого масивів

    # Зливаємо масиви, порівнюючи елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з обох масивів
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  # Повертаємо злитий масив

def insertion_sort(lst):
    for i in range(1, len(lst)):  # Починаємо з другого елемента масиву
        key = lst[i]  # Зберігаємо поточний елемент як ключ
        j = i - 1  # Починаємо порівнювати з попереднім елементом
        while j >= 0 and key < lst[j]:  # Поки не дійшли до початку масиву і ключ менший за поточний елемент
            lst[j + 1] = lst[j]  # Зсуваємо поточний елемент вправо
            j -= 1  # Переміщаємось на одну позицію вліво
        lst[j + 1] = key  # Вставляємо ключ на правильну позицію
    return lst  # Повертаємо відсортований масив

test_array = list()
array_len = 50_000
for _ in range(array_len):
    test_array.append(randint(0, array_len))

def wrapper(sorting_type):
    sorting_type(test_array.copy())

# По підрахункам відносна кількість операцій
# n=50000
# Timsort(sorted), best = O(n) = 50_000
# merge_sort = Timsort(sorted) = O(n * log n) = 780_000
# insertion_sort = O(n^2) = 2_500_000_000
# timsort може бути швидше за merged в 1-15 разів, merged швидша за insertion приблизно в 3200 разів
# merged швидша за insertion (фактично виходить в 400 разів)

algos = {
    'core': sorted,
    'merge': merge_sort,
    'insertion': insertion_sort,
}
prev_execution_time = 0
for type, function in algos.items():
    execution_time = timeit.timeit(lambda: wrapper(function), number=1)
    print(f"Execution time for {type} algorithm: {execution_time}")
    if prev_execution_time != 0:
        print(f"Slowest that previous in {execution_time / prev_execution_time}")
    prev_execution_time = execution_time
