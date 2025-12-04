import random
import timeit
import matplotlib.pyplot as plt


def insertion_sort(l, left=0, right=None):
    if right is None:
        right = len(l) - 1

    for i in range(left+1, right+1):
        key = l[i]
        j = i-1
        while j >= left and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l


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


def tim_sort(l):
    min_run = 32
    n = len(l)

    for i in range(0, n, min_run):
        insertion_sort(l, i, min((i+min_run-1), (n-1)))

        size = min_run
        while size < n:
            for s in range(0, n, size*2):
                mid = s + size-1
                end = min((s+size*2-1), (n-1))

                merged = merge(left=l[s:mid+1], right=l[mid+1:end+1])

                l[s:s+len(merged)] = merged

        size *= 2
    return l


def random_number(num):
    lst_random = []
    for _ in range(num):
        lst_random.append(random.randint(0, 10))

    return lst_random

# [random.randint(0, 10) for _ in range(5)]
        


if __name__ == '__main__':
    # numbers = [random.randint(0, 10) for _ in range(5)] # 5-10-15-20-25-30-35-40-45-50-55-60-65-70-75-80-85-90-95-100

    # print("Hello")
    insertion_sort_lst = []
    merge_sort_lst = []
    tim_sort_lst = []
    x_axis = []

    for i in range(10, 100, 10):
        x_axis.append(i)

        insertion_sort_time = timeit.timeit(
            f"insertion_sort({random_number(i)})", setup="from __main__ import insertion_sort")
        insertion_sort_lst.append(insertion_sort_time)

        merge_sort_time = timeit.timeit(
            f"merge_sort({random_number(i)})", setup="from __main__ import merge_sort")
        merge_sort_lst.append(merge_sort_time)

        tim_sort_time = timeit.timeit(
            f"tim_sort({random_number(5)})", setup="from __main__ import tim_sort")
        tim_sort_lst.append(tim_sort_time)

# Налаштування розміру фігури
plt.figure(figsize=(10, 6))

# # Дані для осі X (спільні для всіх ліній)
# x_data = x_axis

# # Дані для insertion_sort
# y1_data = insertion_sort_lst

# # Дані для merge_sort
# y2_data = merge_sort_lst

# # Дані для tim_sort
# y3_data = tim_sort_lst

# Лінія для insertion_sort
plt.plot(
    x_axis,
    insertion_sort_lst,
    marker='o',
    linestyle='-',
    color='red',
    label='Insertion sort'
)

# Лінія для merge_sort
plt.plot(
    x_axis,
    merge_sort_lst,
    marker='x',
    linestyle='--',
    color='blue',
    label='Merge sort'
)

# Лінія для tim_sort
plt.plot(
    x_axis,
    tim_sort_lst,
    marker='+',
    linestyle='--',
    color='blue',
    label='Timsort'
)

plt.xlabel('Array Length', fontsize=12)
plt.ylabel('Sort Time', fontsize=12)

# Додавання легенди є КЛЮЧОВИМ для декількох ліній
plt.legend(loc='upper left') 

plt.xticks(x_axis) 
plt.grid(True, linestyle=':', alpha=0.6) 

# Відображення графіка
plt.show()