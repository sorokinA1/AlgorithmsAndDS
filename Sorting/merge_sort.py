# arr = [2, 3, 4, 5, 6, 8, 9]
# left = arr[:len(arr) // 2]  # first half
# right = arr[len(arr) // 2:]  # second half
# print(left)
# print(right)

# https://www.youtube.com/watch?v=rAqBlKhy_oI
# https://www.youtube.com/watch?v=LCfwxi2RPK4
# https://www.youtube.com/watch?v=3aTfQvs-_hA additional
import random


def merge_sort(seq):
    if len(seq) <= 1:
        return seq

    mid_point = len(seq) // 2

    left = merge_sort(seq[:mid_point])
    right = merge_sort(seq[mid_point:])

    return merge_two_lists(left, right)


def merge_two_lists(list_one, list_two):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(list_one) and right_pointer < len(list_two):

        if list_one[left_pointer] < list_two[right_pointer]:
            result.append(list_one[left_pointer])
            left_pointer += 1

        else:
            result.append(list_two[right_pointer])
            right_pointer += 1

    result.extend(list_one[left_pointer:])
    result.extend(list_two[right_pointer:])

    return result


arr = list({ random.randint(1, 20) for x in range(20) })  # set -> list

print(merge_sort(arr))
