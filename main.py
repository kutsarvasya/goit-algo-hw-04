import timeit
import random
import matplotlib.pyplot as plt

# Алгоритм сортування вставками


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

# Алгоритм сортування злиттям


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
            # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Timsort (використовує вбудований sorted)


def timsort(arr):
    return sorted(arr)


# Параметри тестування
sizes = [100, 500, 1000, 2000, 3000]
insertion_times, merge_times, timsort_times = [], [], []

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]

    insertion_times.append(timeit.timeit(
        lambda: insertion_sort(data.copy()), number=1))
    merge_times.append(timeit.timeit(
        lambda: merge_sort(data.copy()), number=1))
    timsort_times.append(timeit.timeit(lambda: timsort(data.copy()), number=1))

# Побудова графіка
plt.plot(sizes, insertion_times, label='Insertion Sort')
plt.plot(sizes, merge_times, label='Merge Sort')
plt.plot(sizes, timsort_times, label='Timsort (sorted)')
plt.xlabel('Кількість елементів у списку')
plt.ylabel('Час виконання (сек)')
plt.title('Порівняння алгоритмів сортування')
plt.legend()
plt.grid(True)
plt.savefig("sorting_comparison.png")
plt.show()
