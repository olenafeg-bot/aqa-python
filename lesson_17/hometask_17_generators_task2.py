def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    new_number = fibonacci_generator()
    for _ in range(17):

        print(next(new_number))
