class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def remove(self, index):
        if self.head is not None:
            value = self.head
            count = 0
            prev = None
            if index < 0:
                return
            if index == 0:
                self.head = self.head.next
            while value and count < index:
                prev = value
                value = value.next
                count += 1
            if value:
                prev.next = value.next
    def get(self, index):
        if self.head is not None:
            value = self.head
            count = 0
            if index < 0:
                return None
            while value and count < index:
                value = value.next
                count += 1
            if count == index and value is not None:
                print("Элемент по индексу {}: {}".format(index, value.data))
        return None
    def insert(self, n, value):
        node = Node(value)
        if n == 0:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            for _ in range(n - 1):
                if current is None:
                    raise Exception("Индекс вне диапазона")
                current = current.next
            node.next = current.next
            current.next = node

ll = LinkedList()
ll.push(11)
ll.push(22)
ll.push(3)
ll.push(4)
ll.push(2)
ll.push(1)
ll.insert(2,3123)
ll.get(2)

for element in ll:
    print(element, end=" ")