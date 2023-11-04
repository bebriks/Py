class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.cur_val = None
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.lst):
            if len(self.lst) % 2 != 0:
                self.lst += (None,)
            self.cur_val = (self.lst[self.counter], self.lst[self.counter + 1])
            self.counter += 2
            return self.cur_val
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
