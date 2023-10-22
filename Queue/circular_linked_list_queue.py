# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#     def __str__(self):
#         return str(self.data)
#
#
# class LinkedList:
#     def __init__(self, head=None, end=None):
#         self.head = head
#         self.end = end
#
#     def __str__(self):
#         elements = []
#         cur_node = self.head
#         while cur_node:
#             elements.append(cur_node.data)
#             cur_node = cur_node.next
#         return f'{elements}'
#
#     def __iter__(self):
#         cur_node = self.head
#         while cur_node:
#             yield cur_node
#             cur_node = cur_node.next
#
#
# class Queue:
#     def __init__(self):
#         self.linked_list = LinkedList()
#
#     def __str__(self):
#         values = [str(x) for x in self.linked_list]
#         return f'{values}'
#
#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.linked_list.head is None:
#             self.linked_list.head = new_node
#             self.linked_list.end = new_node
#         else:
#             self.linked_list.end.next = new_node
#             self.linked_list.end = new_node
#
#
# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(my_queue)


############################################################
############ Circular Queue with limited size ##############
############################################################
# None -> 1 -> 2 -> 3 -> None
#
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


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

    def __len__(self):
        count = 0
        cur_node = self.start.next
        while cur_node.next:
            cur_node = cur_node.next
            count += 1
        return count

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
            self.start.next = self.start.next.next
            self.start.next.prev = self.start
            self.space += 1

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

#
#
# my_queue = Queue(3)
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(my_queue)
# print(len(my_queue))
# my_queue.dequeue()
# print(my_queue)

# https://www.youtube.com/watch?v=aBbsfn863oA&t=919s



