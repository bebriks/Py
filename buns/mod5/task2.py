class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        if self.start is None:
            raise Exception("Очередь пуста")
        val = self.start.data
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        else:
            self.start.pref = None
        return val


    def push(self, val):
        new_node = Node(val)
        new_node.nref = None
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            for _ in range(n - 1):
                current = current.nref
                if current is None:
                    raise Exception("Индекс вне диапазона")
            new_node.nref = current.nref
            current.nref = new_node
            new_node.pref = current
            if new_node.nref is None:
                self.end = new_node
            else:
                new_node.nref.pref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()
myQ = Queue()
myQ.push(2)
myQ.push(4)
myQ.push(6)
myQ.push(8)
myQ.push(10)
myQ.push(12)
myQ.insert(2, 34)
myQ.pop()
myQ.print()