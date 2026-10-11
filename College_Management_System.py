class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach_student(self, student):
        print(f"Teacher {self.name} is teaching {student.name}.")


class Department:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"Students in {self.name}:")
        for student in self.students:
            print(student.name)


class College:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.departments = []

    def add_student(self, student):
        self.students.append(student)

    def add_department(self, department_name):
        department = Department(department_name)
        self.departments.append(department)
        return department

    def display_students(self):
        print("Students in College:")
        for student in self.students:
            print(student.name)


student1 = Student("Anmol Singh", "25BCA008")
student2 = Student("Rahul Kumar", "25BCA009")

teacher = Teacher("Mahadev")

college = College("SIT")
college.add_student(student1)
college.add_student(student2)

computer_science = college.add_department("Computer Science")
computer_science.add_student(student1)
computer_science.add_student(student2)

print("========== COLLEGE MANAGEMENT SYSTEM ==========")
print()
print(f"College: {college.name}")
print()
print(f"Department: {computer_science.name}")
print()
college.display_students()
print()
computer_science.display_students()
print()
teacher.teach_student(student1)