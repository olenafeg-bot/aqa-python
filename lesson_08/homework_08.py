class Student(object):
    def __init__(self, first_name, last_name, age, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def change_score(self, new_score):
        self.average_score = new_score

    def information(self):
        return self.__dict__
student1 = Student('Jenifer', 'Mildred', '23', 9)
print(student1.information())

student1.change_score(10)
print(student1.information())

