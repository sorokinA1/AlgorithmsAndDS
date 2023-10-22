class Stack:
    def __init__(self, max_length):
        self.arr = []
        self.max_length = max_length

    def __str__(self):
        # self.arr.reverse()
        return f'{self.arr}'

    @property
    def is_empty(self):
        return True if not self.arr else False

    @property
    def is_full(self):
        return True if len(self.arr) == self.max_length else False

    def push(self, data):
        if self.is_full:
            raise IndexError
        else:
            self.arr.append(data)

    def extend(self, arr):
        for i in arr:
            if self.is_full:
                raise IndexError
            else:
                self.arr.append(i)

    def pop(self):
        if self.is_empty:
            print('[]')
        else:
            return self.arr.pop()

    def peek(self):
        if self.is_empty:
            print('[]')
        else:
            return self.arr[-1]

    def clear(self):
        self.arr = None


new_stack = Stack(5)
print(new_stack.is_empty)
new_stack.extend(['Sayaka', 'Sakura', 'Ayaka'])
new_stack.extend(['Akari', 'Ren'])
new_stack.push('May')
print(new_stack)
new_stack.pop()
print(new_stack)
print(new_stack.peek())
