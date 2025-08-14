class Student:

    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def get_info(self):
        return (f"This is student {self.name} {self.surname}. "
                f"His age is {self.age}. His average score is {self.average_score}")

    def change_point_average(self, new_value):
        self.average_score = new_value


sasha_student = Student("Sasha", "Drubetskoi", 47, 100)
print(sasha_student.get_info())
sasha_student.change_point_average(105)
print(sasha_student.get_info())
