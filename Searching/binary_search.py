# Iterative: https://www.youtube.com/watch?v=3OIHMTe_Tcg
# Recursive https://www.youtube.com/watch?v=7nbatZEehyo

# O(logn):
# https://www.youtube.com/watch?v=wjDY5RbILno
# https://www.youtube.com/watch?v=K3NluEdHkao&t=89s

arr = [11, 23, 37, 41, 56, 62, 79, 83, 92]


def binary_search_iter(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid_point = (left + right) // 2

        if arr[mid_point] > target:
            right = mid_point - 1
        elif arr[mid_point] < target:
            left = mid_point + 1
        else:
            return mid_point

    return -1


print(binary_search_iter(arr, 79))


# Recursive
def binary_search_rec(data, low, high, item):
    if low <= high:
        mid_point = (low + high) // 2

        if data[mid_point] == item:
            return mid_point
        elif item < data[mid_point]:
            return binary_search_rec(data, low, mid_point - 1, item)
        else:
            return binary_search_rec(data, mid_point + 1, high, item)

    return -1


print(binary_search_rec(arr, 0, len(arr) - 1, 83))
