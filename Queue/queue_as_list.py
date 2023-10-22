class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        # elements = [str(x) for x in self.items]
        # return ', '.join(elements)
        return f'{self.items}'

    @property
    def is_empty(self):
        return True if not self.items else False

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty:
            return self.items.pop(0)
        else:
            raise ValueError

    def peek(self):
        if not self.is_empty:
            return self.items[0]

    def clear(self):
        self.items = None

# my_queue = Queue()
# my_queue.enqueue('T-34')
# my_queue.enqueue('ELC Even')
# my_queue.enqueue('Setter')
# print(my_queue)
# print(len(my_queue))
# my_queue.dequeue()
# print(my_queue)
# print(my_queue.peek())
