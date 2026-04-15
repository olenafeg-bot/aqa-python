value = ["1,2,3,4", "1,2,3,4,50","qwerty1,2,3"]
def calculate_sum(value):
    try:
        numbers = value.split(',')
        numbers = map(int, numbers)
        return sum(numbers)
    except ValueError:
        return f"Can't print the sum"


for item in value:
    print(calculate_sum(item))