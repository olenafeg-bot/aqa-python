
#task1. Generators

def even_number_generator(number):
    for i in range(0, number+1):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":
    for num in even_number_generator(15):

        print(num)



print ("task2")

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    new_number = fibonacci_generator()
    for _ in range(17):

        print(next(new_number))
