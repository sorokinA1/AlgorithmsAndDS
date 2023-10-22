# https://www.youtube.com/watch?v=vY-cCiPf8ow&t=4s
# n^2
def bubble_sort(seq):
    # go through the list once per element
    for i in range(len(seq)):
        # i -> elements that are already sorted
        for j in range(len(seq) - i - 1):
            # compare pairs of elements that are not sorted yet
            if seq[j] > seq[j + 1]:
                # swap elements
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    print(seq)


arr = [3, 4, 2, 1, 5]
# arr = [4, 2, 1, 3, 8, 5, 9, 7, 6]

bubble_sort(arr)
