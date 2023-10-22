# class Queue:
#     def __init__(self, maxSize):
#         pass
#
#     def enqueue(self, value):
#         pass
#
#     def dequeue(self):
#         pass
#
#     def isEmpty(self):
#         pass
#
#     def isFull(self):
#         pass
#
#     def showFront(self):
#         pass
#
#     def showRear(self):
#         pass
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, space):
        self.space = space
        self.start = Node()
        self.end = Node(prev=self.start)
        self.start.next = self.end

    def __str__(self):
        elements = []
        cur_node = self.start.next
        while cur_node.next:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return f'{elements}'

    def enqueue(self, value):
        if self.isFull:
            return 'Queue is full'
        else:
            new_node = Node(value, next=self.end, prev=self.end.prev)
            self.end.prev.next = new_node
            self.end.prev = new_node
            self.space -= 1

    def dequeue(self):
        if self.isEmpty:
            return '[]'
        else:
            temp = self.start.next
            self.start.next = self.start.next.next
            self.start.next.prev = self.start
            self.space += 1
            return temp

    @property
    def isEmpty(self):
        return self.start.next == self.end

    @property
    def isFull(self):
        return self.space == 0

    def showFront(self):
        if not self.isEmpty:
            return self.start.next.data
        else:
            return -1

    def showRear(self):
        if not self.isEmpty:
            return self.end.prev.data
        else:
            return -1

# my_queue = Queue(3)
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(my_queue)
# print(my_queue.dequeue())
