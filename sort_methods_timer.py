import random
import timeit
import matplotlib.pyplot as plt


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left+1, right+1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge_s(
        mergesort(left), 
        mergesort(right))


def merge_s(left, right):
    if not left:
        return right
    
    if not right:
        return left
    
    result = []
    left_index = right_index = 0

    # Спочатку об'єднайте менші елементи
    while len(result) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

        # Якщо в лівій або правій половині залишилися елементи,
        # додайте їх до результату
        if right_index == len(right):
            result += left[left_index:]
            break

        if left_index == len(left):
            result += right[right_index:]
            break
    
    return result


def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, (n - 1)))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge_s(
                left = arr[start:mid], 
                right = arr[mid:end + 1]
                )

            arr[start:start+len(merged_array)] = merged_array

        size *= 2
    return arr


def random_number(num):
    lst_random = []
    for _ in range(num):
        lst_random.append(random.randint(0, 10))

    return lst_random


def timer_measurement(arr, sort_function_name):
    # Створюємо словник globals, щоб timeit міг бачити функцію сортування 
    # та масив (як 'arr_to_sort')
    setup_globals = {
        'sort_func': sort_function_name,
        'arr_to_sort': arr
    }
    stmt = "sort_func(arr_to_sort.copy())"
    sort_time = timeit.timeit(
        stmt=stmt, 
        globals=setup_globals,
        number=10
    )
    return sort_time / 10


def pythont_standart_sort(arr):
    arr.sort()
    return arr

if __name__ == '__main__':
    print("HELLO")
    # insertion_sort_lst = []
    merge_sort_lst = []
    tim_sort_lst = []
    pythont_standart_sort_lst = []
    x_axis = []        
    
    for i in range(10, 100000, 10000):
        print(f"******************** {i} ************************")
        x_axis.append(i)

        arr = random_number(i)

        default_s = timer_measurement(arr, pythont_standart_sort)
        print(f"Default sort: {default_s:.6f} sec")
        pythont_standart_sort_lst.append(default_s)

        # insertion_s = timer_measurement(arr, insertion_sort)
        # print(f"Insertion: {insertion_s:.6f} sec")
        # insertion_sort_lst.append(insertion_s)
        
        # Merge Sort (O(n log n))
        merge_st = timer_measurement(arr, mergesort)
        print(f"Merge: {merge_st:.6f} sec") 
        merge_sort_lst.append(merge_st)

        # Timsort (O(n log n))
        tim_s = timer_measurement(arr, tim_sort)
        print(f"Timsort: {tim_s:.6f} sec")
        tim_sort_lst.append(tim_s)

    # Налаштування розміру фігури
    plt.figure(figsize=(12, 7))

    # # Лінія для insertion_sort
    # plt.plot(
    #     x_axis,
    #     insertion_sort_lst,
    #     marker='o',
    #     linestyle='-',
    #     color='red',
    #     label='Insertion sort'
    # )

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
        color='green',
        label='Timsort'
    )
    
    # Лінія для pythont_standart_sort
    plt.plot(
        x_axis,
        pythont_standart_sort_lst,
        marker='o',
        linestyle='--',
        color='black',
        label='Pythont Standart Sort'
    )

    plt.xlabel('Array Length', fontsize=12)
    plt.ylabel('Sort Time (seconds)', fontsize=12)

    # Додавання легенди є КЛЮЧОВИМ для декількох ліній
    plt.legend(loc='upper left') 

    plt.xticks(x_axis) 
    plt.grid(True, linestyle=':', alpha=0.6) 

    # Відображення графіка
    plt.show()