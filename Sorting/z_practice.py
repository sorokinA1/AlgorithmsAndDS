arr = [4, 2, 1, 3, 8, 5, 9, 7, 6]


def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(len(seq) - i - 1):
            if seq[j + 1] < seq[j]:
                seq[j + 1], seq[j] = seq[j], seq[j + 1]
    return seq


def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq


def insertion_sort(seq):
    for i in range(1, len(seq)):
        temp = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > temp:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = temp
    return seq


def bucket_sort(seq):
    result = []
    num_of_buckets = len(seq) // 2
    buckets = [[] for x in range(num_of_buckets)]
    max_el, min_el = max(seq), min(seq)
    bucket_size = (max_el - min_el) / num_of_buckets

    for element in seq:
        index = int((element - min_el) / bucket_size)
        if element == max_el: index -= 1
        buckets[index].append(element)

    for bucket in buckets:
        result.extend(insertion_sort(bucket))

    return result


def merge_sort(seq):
    if len(seq) <= 1:
        return seq

    mid_point = len(seq) // 2

    left = merge_sort(seq[:mid_point])
    right = merge_sort(seq[mid_point:])

    return merge_two_lists(left, right)


def merge_two_lists(list1, list2):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(list1) and right_pointer < len(list2):
        if list1[left_pointer] < list2[right_pointer]:
            result.append(list1[left_pointer])
            left_pointer += 1

        else:
            result.append(list2[right_pointer])
            right_pointer += 1

    result.extend(list1[left_pointer:])
    result.extend(list2[right_pointer:])

    return result


def partition(seq, low, high):
    i = low - 1
    pivot = seq[high]

    for j in range(low, high):
        if seq[j] <= pivot:
            i += 1
            seq[j], seq[i] = seq[i], seq[j]
    seq[i + 1], seq[high] = seq[high], seq[i + 1]

    return i + 1


def quick_sort(seq, low=0, high=None):
    if high is None:
        high = len(seq) - 1

    if low < high:
        pivot_index = partition(seq, low, high)
        quick_sort(seq, low, pivot_index - 1)
        quick_sort(seq, pivot_index + 1, high)

    return seq


def heapify(arr, upper, el_index):
    largest = el_index
    left = 2 * el_index + 1
    right = 2 * el_index + 2

    if left < upper and arr[left] > arr[largest]:
        largest = left

    if right < upper and arr[right] > arr[largest]:
        largest = right

    if el_index != largest:
        arr[largest], arr[el_index], = arr[el_index], arr[largest]
        heapify(arr, upper, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# print(bubble_sort(arr))
# print(selection_sort(arr))
# print(bucket_sort(arr))
# print(merge_sort(arr))
# print(quick_sort(arr))
print(heap_sort(arr))
