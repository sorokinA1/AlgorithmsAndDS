# https://interviewnoodle.com/sorting-algorithms-explained-using-python-bucket-sort-e606a818cf3

import math
import random


def insertion_sort(seq):
    """Algorithm for sorting the buckets."""
    for i in range(1, len(seq)):
        temp = seq[i]
        j = i - 1
        while j >= 0 and temp < seq[j]:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = temp
    return seq


def bucket_sort(seq):
    """Main sorting algorithm function."""
    # variable initialization
    # num_of_buckets can be an input arg instead of local var
    result = []
    num_of_buckets = len(seq) // 2

    buckets = [[] for i in range(num_of_buckets)]
    max_elem, min_elem = max(seq), min(seq)
    bucket_size = (max_elem - min_elem) / num_of_buckets

    # distribute elements in corresponding buckets
    for element in seq:
        index = int((element - min_elem) / bucket_size)

        if element == max_elem: index -= 1
        # index -= 1 if element == max_elem else 0
        buckets[index].append(element)

    # sort the buckets one by one, then add them to the result
    for bucket in buckets:
        result.extend(insertion_sort(bucket))

    print(buckets)

    return result


list_1 = [9, 7, 5, 4, 0, 1, 2, 3, 6, 8, -1]
list_2 = [-9, 7, 5, -4, 0, 1, 2, -3, 6, -8]
list_3 = set([random.randint(1, 40) for x in range(40)])
# print(bucket_sort(list_2))
# print(bucket_sort(list_1))
print(bucket_sort(list_3))
