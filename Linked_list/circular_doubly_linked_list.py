class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class CircularDoubleLinkedList:
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

    def reverse(self):
        if self.head is None:
            print('[]')
        else:
            elements = []
            cur_node = self.end
            while cur_node:
                elements.append(cur_node.data)
                cur_node = cur_node.prev
                if cur_node == self.end:
                    break
            print(elements)

    @property
    def length(self):
        total = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            total += 1
            if cur_node == self.head:
                break
        return total

    def unshift(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.end
            self.head.prev = new_node
            self.head = new_node
            self.end.next = new_node

    def push(self, data):
        if self.head is None:
            self.unshift(data)
        else:
            new_node = Node(data, prev=self.end, next=self.head)
            self.end.next = new_node
            self.head.prev = new_node
            self.end = new_node

    def insert(self, index, data):
        if index < -1 or index > self.length:
            raise IndexError
        elif index == 0:
            self.unshift(data)
        elif index == -1 or index == self.length:
            self.push(data)
        else:
            count = 0
            cur_node = self.head
            while count < index - 1:
                cur_node = cur_node.next
                count += 1
            new_node = Node(data, prev=cur_node, next=cur_node.next)
            cur_node.next = new_node
            new_node.next.prev = new_node

    def remove_beg(self):
        if self.head is None:
            print('[]')
        elif self.head == self.end:
            self.head.next = None
            self.head.prev = None
            self.head = None
            self.end = None
        else:
            self.head = self.head.next
            self.head.prev = self.end
            self.end.next = self.head

    def remove_end(self):
        if self.head is None:
            print('[]')
        elif self.head == self.end:
            self.remove_beg()
        else:
            self.end = self.end.prev
            self.end.next = self.head
            self.head.prev = self.end

    def remove(self, index):
        if index < -1 or index > self.length:
            raise IndexError
        elif index == 0:
            self.remove_beg()
        elif index == -1 or index == self.length:
            self.remove_end()
        else:
            count = 0
            cur_node = self.head
            while count < index - 1:
                cur_node = cur_node.next
                count += 1
            cur_node.next = cur_node.next.next
            cur_node.next.prev = cur_node

    def clear(self):
        if self.head is None:
            print('[]')
        else:
            self.end.next = None
            cur_node = self.head
            while cur_node:
                cur_node.prev = None
                cur_node = cur_node.next
            self.head = None
            self.end = None
            

my_list = CircularDoubleLinkedList()
my_list.unshift('Druid')
my_list.unshift('Warrior')
my_list.unshift('Warlock')
my_list.insert(2, 'Dk')
my_list.display()
my_list.reverse()
my_list.remove(1)
my_list.display()
my_list.reverse()
my_list.clear()
my_list.display()
my_list.push('hi')
my_list.display()
print(my_list.length)
