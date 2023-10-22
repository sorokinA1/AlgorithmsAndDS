# The best exp! https://www.youtube.com/watch?v=hkyzcLkmoBY&t=709s
class MinHeap:

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    # get indexes
    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    # has parent or has children
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    # get data
    def parent(self, index):
        return self.storage[self.get_parent_index(index)]

    def left_child(self, index):
        return self.storage[self.get_left_child_index(index)]

    def right_child(self, index):

        return self.storage[self.get_right_child_index(index)]

    def is_full(self):

        return self.size == self.capacity

    def swap(self, index1, index2):

        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):

        if self.is_full():
            print('Heap is Full')

        self.storage[self.size] = data
        self.size += 1

        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        # > min heap |--| < max heap
        if self.has_parent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.get_parent_index(index), index)
            self.heapify_up(self.get_parent_index(index))

    def remove_min(self):
        if self.size == 0:
            print('Heap is empty')

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage.pop()
        self.size -= 1

        # always starting with root

        self.heapify_down(0)

        return data

    def heapify_down(self, index):

        smallest = index
        if self.has_left_child(index) and self.storage[smallest] > self.left_child(index):
            smallest = self.get_left_child_index(index)

        if self.has_right_child(index) and self.storage[smallest] > self.right_child(index):
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(smallest, index)
            self.heapify_down(smallest)

    def level_order_print(self):
        for i in range(self.size):
            print(self.storage[i], end='-')


heap = MinHeap(5)
heap.insert(4)
heap.insert(5)
heap.insert(1)
heap.insert(2)
heap.level_order_print()
print('\n')
heap.remove_min()
heap.level_order_print()
print('\n')
heap.insert(0)
heap.level_order_print()
