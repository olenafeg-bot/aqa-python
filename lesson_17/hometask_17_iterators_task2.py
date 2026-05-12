class EvenNumberIterator:
    def __init__(self, number):
        self.initial = 0
        self.number = number
    def __iter__(self):
        return self
    def __next__(self):
        if self.initial >self.number:
            raise StopIteration

        value2 = self.initial
        self.initial = self.initial + 2
        return value2

if __name__ == "__main__":
    for num in EvenNumberIterator(15):
        print(num)


