
#task1. Generators

def even_number_generator(number):
    for i in range(0, number+1):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":
    for num in even_number_generator(15):

        print(num)
