class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_person(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Student(Person):
    def __init__(self, name, age, rool_num, course, marks):
        super().__init__(name, age)
        self.rool_num = rool_num
        self.course = course
        self.marks = marks
        
    def show_student(self):
        super().show_person()
        print(f"Rool Number: {self.rool_num}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif 80 <= self.marks <= 89:
            return "A"
        elif 70 <= self.marks <= 79:
            return "B"
        elif 60 <= self.marks <= 69:
            return "C"
        elif 50 <= self.marks <= 59:
            return "D"
        else:
            return "F"
        
    def Student_Input(self):
        print("\n--- Enter Student Details ---")
        self.name = input("Enter Student Name : ")
        self.age = int(input("Enter Student Age : "))
        self.rool_num = input("Enter Rool Number: ")
        self.course = input("Enter Course: ")
        self.marks = int(input("Enter Marks: "))

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
        
    def show_teacher(self):
        super().show_person()
        print(f"Subject: {self.subject}")
        self.calculate_bonus()
        
    def calculate_bonus(self):
        if self.salary >= 50000:
            bonus_percentage = 10
            bonus_amount = self.salary * 0.10
        else:
            bonus_percentage = 5
            bonus_amount = self.salary * 0.05
            
        exact_salary = self.salary + bonus_amount
        print(f"Base Salary: ₹{self.salary}")
        print(f"Bonus Added: {bonus_percentage}% (₹{bonus_amount:.2f})")
        print(f"Total Exact Salary: ₹{exact_salary:.2f}")

        return exact_salary

    def Teacher_input(self):
        print("\n--- Enter Teacher Details ---")
        self.name = input("Enter Teacher Name : ")
        self.age = int(input("Enter Teacher Age : "))         
        self.subject = input("Enter Subject: ")         
        self.salary = int(input("Enter Salary: "))        


student1 = Student("", 0, "", "", 0) 
student1.Student_Input()
print()

Teacher1 = Teacher("", 0, "", 0)
Teacher1.Teacher_input()
print()

print("=============================")
print("\n=== STUDENT RESULT ===")
print("=============================")
student1.show_student()

print()

print("=============================")
print("\n=== TEACHER RESULT ===")
print("=============================")
Teacher1.show_teacher()
