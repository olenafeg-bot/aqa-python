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

