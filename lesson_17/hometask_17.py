
#task1. Generators

def even_number_generator(number):
    for i in range(0, number+1):
        if i % 2 == 0:
            yield i
for num in even_number_generator(15):
    print(num)

#task2

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

new_number = fibonacci_generator()
for _ in range(17):
    print(next(new_number))

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


for num in ReverseNumberIterator(numbers):
    print(num)

#Iterators. Task 2.
# def even_number_iterator(number):
#     for i in range(0, 16):
#         if i % 2 == 0:
#             print(next(number+1))
# try:
#     even_number_iterator(15)
#     print(next(number+1))
# except StopIteration:
# print("Stop iterator")

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

for num in EvenNumberIterator(15):
    print(num)


 #Decorator. Task 1.

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_decorator(func):
     def wrapper(*args):
         result = func(*args)
         logging.info(f"Called {func.__name__} with args {args}")
         #return func(*args, **kwargs)
         #logging.info("f{func.__name__} returned {result}")
         return result
     return wrapper

@log_decorator
def function(name, profession):
    print('Hello %s!' % name, profession)
function("Olena", "QA")

#Task2
def exceptions_decorator(func):
     def wrapper(*args, **kwargs):
         try:
             result = func(*args, **kwargs)
             return result
         except Exception as e:
             print (f"Caught exception: {e}")
             return

     return wrapper

@exceptions_decorator
def divide(a, b):
    return a / b

print(divide(1, 0))