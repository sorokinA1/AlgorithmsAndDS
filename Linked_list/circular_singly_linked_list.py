# https://www.youtube.com/watch?v=t8lyrfPStN0
# https://www.youtube.com/watch?v=EuP2hHJ36Kg
# https://www.youtube.com/watch?v=TZoKsJsCMD4

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def display(self):
        if self.head is None:
            print('[]')
        else:
            elements = []
            cur_node = self.head
            while cur_node:
                elements.append(cur_node.data)
                cur_node = cur_node.next
                if cur_node == self.head:
                    break
            print(elements)

    @property
    def length(self):
        total = 0
        cur_node = self.head
        while cur_node:
            total += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return total

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            new_node.next = self.head
            self.end = new_node

    def unshift(self, data):
        if self.head is None:
            self.push(data)
        else:
            new_node = Node(data, self.head)
            self.head = new_node
            self.end.next = self.head

    def insert(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError('oops')
        elif index == 0:
            self.unshift(data)
        elif index == self.length:
            self.push(data)
        else:
            cur_node = self.head
            count = 0
            while cur_node:
                if count == index - 1:
                    cur_node.next = Node(data, cur_node.next)
                    break
                cur_node = cur_node.next
                count += 1
                if cur_node == self.head:
                    break

    def delete_beg(self):
        if self.head is not None:
            aft_head = self.head.next
            self.end.next = aft_head
            self.head = aft_head
        else:
            raise ValueError('List is empty')

    def delete_end(self):
        if self.head is not None:
            cur_node = self.head
            # find node before last node
            while cur_node.next.next != self.head:
                cur_node = cur_node.next
            # reassign
            self.end = cur_node
            cur_node.next = self.head
        else:
            raise ValueError('oops')

    def del_mid(self, index):
        if index < 0 or index > self.length:
            raise IndexError('oops')
        elif index == 0:
            self.delete_beg()
        elif index == self.length:
            self.delete_end()
        else:
            cur_node = self.head
            count = 0
            while cur_node:
                if count == index - 1:
                    cur_node.next = cur_node.next.next
                    break
                cur_node = cur_node.next
                count += 1

    def clear(self):
        self.head = None
        self.end.next = None
        self.end = None

###########################################################
