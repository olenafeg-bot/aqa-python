# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(5)



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_num(num1, num2):
    return num1 + num2
if __name__ == "__main__":
    print (sum_num(4, 5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers = [1 ,5, 6, 7, 8]
def average(numbers):
    return sum(numbers) / len(numbers)
print(average(numbers))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
my_string = "From fairest creatures we desire increase"
def reverse_string(my_string):
    return my_string[::-1]
if __name__ == "__main__":
    print(reverse_string(my_string))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
word_list = ['animals', 'flowers', 'hobby','book']
def longest_word(word_list):
    longest = ""
    for word in word_list:
        if len(word) > len(longest):
            return word
if __name__ == "__main__":
    print(longest_word(word_list))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
if __name__ == "__main__":
    print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
if __name__ == "__main__":
    print(find_substring(str1, str2)) # поверне -1

# task 7

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
"""add the record to the list of the people records"""

def people_records_inserted(people_records):
    people_records.insert(0, ('Emilia', 'Clark', 39, 'Actress', 'Los Angeles'))
    return people_records
if __name__ == "__main__":
     print(people_records_inserted(people_records))

"""Change the replace the records in the list"""

def people_records_new(people_records):
    people_records[1], people_records[5] = people_records[5], people_records[1]
    return people_records
if __name__ == "__main__":
    print(people_records_new(people_records))

"""Check the age of the people"""
def check_age(people_records):
    return all(people_records[i][2] >= 30 for i in [6, 10, 13])
if __name__ == "__main__":
    print(check_age(people_records))
# task 8
"""Return the even numbers from the list"""

def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


if __name__ == "__main__":
    print(even_numbers([1, 76, 5, 777, 89, 44, 6, 30, 64]))


# task 9
"""Add the string items to the list"""
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def new_list():
    lst2 = []
    for item in lst1:
        if type(item) == str:
            lst2.append(item)
    return lst2
if __name__ == "__main__":
    print(new_list())
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

"""Count worrds from capital letters"""

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
def count_title_words(text):

    adwentures_of_tom_sawer_words = text.split()
    count = sum(1 for word in adwentures_of_tom_sawer_words if word.istitle())
    return count
if __name__ == "__main__":
    print(count_title_words(adwentures_of_tom_sawer))

