#Iterators. Task1

class ReverseNumberIterator:
    def __init__(self, number):
        self.number = number
        self.index = len(number)-1

    def __iter__(self):
            return self

    def __next__(self):
        if self.index >= 0:
            value = self.number[self.index]
            self.index = self.index - 1
            return value

        else:
            raise StopIteration

        return value

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    for num in ReverseNumberIterator(numbers):
        print(num)

print("task 2")

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


