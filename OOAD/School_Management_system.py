class Student:
    def __init__(self, name, age, adress="", father_name=""):
        self.name = name
        self.age = age
        self.address = adress
        self.father_name = father_name
        self.grade = []

    def __str__(self):
        return f"name of student is {self.name} age is {self.age}"


class Performance:
    def __init__(self, student):
        self.student = student

    def check_grade(self):
        if len(self.student.grade) == 0:
            return "new student"
        else:
            return self.student.grade + " Total_grade till now "


class AddStudent:
    count = 0
    total_student = []

    def __init__(self, name, age):
        self.__student = Student(name, age)
        AddStudent.count += 1
        self.__add_student()

    def __add_student(self):
        AddStudent.total_student.append((self.__student.name, self.__student.age))


if __name__ == "__main__":
    Add_st = AddStudent("Ankush", 15)
    Add_st1 = AddStudent("Anish", 23)
    total_student = AddStudent.total_student

    print(total_student)
    print("total_number of student ", AddStudent.count)
