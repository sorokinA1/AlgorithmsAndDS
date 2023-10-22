# https://www.youtube.com/watch?v=kZH0vWXs
# https://www.youtube.com/watch?v=EwjnF7rFLns&t=87s
# n^2
def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]

    print(seq)


arr = [3, 4, 2, 1, 5]
# arr = [4, 2, 1, 3, 8, 5, 9, 7, 6]

selection_sort(arr)
