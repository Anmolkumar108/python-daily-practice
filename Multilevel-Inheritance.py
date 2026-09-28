class person:
    def __init__(self ,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
class student(person):
    def __init__(self,roll_no, course, name, age):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
    def show(self):
        super().show()
        print(f"Roll No. : {self.roll_no}")
        print(f"Course : {self.course}")
class CollegeStudent(student):
    def __init__(self, college, semester , marks, roll_no, course, name, age):
        super().__init__(roll_no, course, name, age)
        self.college = college
        self.semester = semester
        self.marks = marks
    
    def show(self):
        super().show()
        print(f"College Name : {self.college}")
        print(f"Semester : {self.semester}")
        print(f"Marks : {self.marks}")
        print(f"Grade : {self.get_grade()}")

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
            return "Fail"
        
student1 = CollegeStudent("SIT", "3rd", 85, 
                          "25BCA008", "BCA", 
                          "Anmol Singh", 19)
student1.show()