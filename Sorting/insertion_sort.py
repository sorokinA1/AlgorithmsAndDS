# https://www.youtube.com/watch?v=nKzEJWbkPbQ
# https://www.youtube.com/watch?v=K0zTIF3rm9s
# https://www.youtube.com/watch?v=8mJ-OhcfpYg&t=191s bro code
def insertion_sort(seq):
    for i in range(1, len(seq)):
        temp = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > temp:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = temp

    print(seq)


arr = [1, 2, 4, 8, 3]
# arr = [4, 2, 1, 3, 8, 5, 9, 7, 6]

insertion_sort(arr)
