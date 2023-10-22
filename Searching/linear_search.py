arr = ['Jun', 'Akane', 'Yui', 'Ruby', 'Aqua', 'Ai', 'Sayaka']
arr2 = ['Jun', 'Akane', 'Yui', 'Ruby', 'Aqua', 'Ai']


def linear_search(arr):
    for i in range(len(arr)):
        if arr[i] == 'Sayaka':
            return arr[i]
    return 'not found'


print(linear_search(arr))
print(linear_search(arr2))
