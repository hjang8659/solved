"""
    Stack
    LIFO (Last-In First-Out)
"""

class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Empty"
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return "Empty"
    def __str__(self):
        return str(self.stack)
    
b_day = Stack()
b_day.push(6)
b_day.push(14)
b_day.push(1996)

print(b_day.peek())
print(b_day.pop())
print(b_day.pop())
print(b_day.peek())
print(b_day.pop())
print(b_day.pop())
print(b_day.peek())