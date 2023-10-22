# https://www.youtube.com/watch?v=Vtckgz38QHs bro !!! the best
# https://www.youtube.com/watch?v=1Mx5pEeTp3A

# inplace quicksort
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low=0, high=None):  # allow us pass only array in function
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)  # partition around pivot
        quick_sort(arr, low, pivot_index - 1)  # sort lower half
        quick_sort(arr, pivot_index + 1, high)  # sort upper half

    return arr


arr = [9, 7, 5, 4, 0, 1, 2, 3, 6, 8, -1]

print(quick_sort(arr))
