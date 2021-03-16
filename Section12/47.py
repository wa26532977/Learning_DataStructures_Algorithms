import _ctypes


class DynamicArray:

    def __init__(self, n, capacity):

        self.n = n
        self.capacity = capacity

    def __len__(self):
        return self.n

    def print_self(self):
        print(f"The N = {self.n} and the capacity = {self.capacity}")

