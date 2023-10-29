class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            raise Exception("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        current = self.end
        while current is not None:
            print(current.data, end=" ")
            current = current.pref
        print()
myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.pop()
myStack.pop()
myStack.print()