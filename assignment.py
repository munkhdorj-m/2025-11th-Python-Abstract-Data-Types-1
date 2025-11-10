# solutions.py

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def decimal_to_binary(n):
    stack = Stack()

    if n == 0:
        return "0"

    while n > 0:
        remainder = n % 2
        stack.push(remainder)
        n //= 2

    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())

    return binary



class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


def bank_simulation(customers):
    q = Queue()

    for name in customers:
        q.enqueue(name)

    output = ""
    while not q.is_empty():
        output += f"Serving: {q.dequeue()}\n"

    return output.strip()
