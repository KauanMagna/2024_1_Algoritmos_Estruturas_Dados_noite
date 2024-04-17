class Student:
    def __init__(self, code, name, registration):
        self.code = code
        self.name = name
        self.registration = registration

    def print_student(self):
        print(f"Code: {self.code} \nName: {self.name} \nResgistration: {self.registration}")

class Middle_School(Student):
    def __init__(self, code, name, registration, year):
        Student.__init__(self, code, name, registration)
        self.year = year

    def print_MD_student(self):
        print(f"Code: {self.code} \nName: {self.name} \nResgistration: {self.registration} \nYear: {self.year}")

class Undergraduate_degree(Student):
    def __init__(self, code, name, registration, semester):
        Student.__init__(self, code, name, registration)
        self.semester = semester

    def print_undergraduate_student(self):
        print(f"Code: {self.code} \nName: {self.name} \nResgistration: {self.registration} \nSemester: {self.semester}")

student01 = Student(10, "Mary", 12345)
student01.print_student()
print("--" * 5)
littlest = Middle_School(11, "Marcus", 67890, "2018")
littlest.print_MD_student()
print("--" * 5)
biggerst = Undergraduate_degree(12, "Luc", 76543, "second")
biggerst.print_undergraduate_student()

