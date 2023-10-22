# https://www.youtube.com/watch?v=2DmK_H7IdTo&t=191s
# https://www.youtube.com/watch?v=laYrbOAmuvQ
# https://www.guru99.com/heap-sort.
# https://www.youtube.com/watch?v=kU4KBD4NFtw&t=783s c++ bext exp
# https://www.youtube.com/watch?v=0NwapWP_dKs&t=480s


def heapify(arr, upper, el_index):
    largest = el_index
    left = 2 * el_index + 1
    right = 2 * el_index + 2

    #  > asc | < desc
    if left < upper and arr[left] > arr[largest]:
        largest = left

    if right < upper and arr[right] > arr[largest]:
        largest = right

    if largest != el_index:
        arr[el_index], arr[largest] = arr[largest], arr[el_index]
        heapify(arr, upper, largest)


def heapsort(arr):
    n = len(arr)

    # build a heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # i -> last elem
        heapify(arr, i, 0)  # i -> cur size of heap

    return arr


arr = [4, 2, 1, 3, 8, 5, 9, 7, 6]

print(heapsort(arr))
