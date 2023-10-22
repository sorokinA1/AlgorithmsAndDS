class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def __len__(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def display(self):
        if self.head is None:
            print(['[]'])
        else:
            elements = []
            cur_node = self.head
            while cur_node:
                elements.append(cur_node.data)
                cur_node = cur_node.next
            print(elements)

    def extend(self, arr):
        for i in arr:
            self.push(i)
        return self.head
