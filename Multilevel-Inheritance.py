class person:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Name : {self.name}")
class student(person):
    def __init__(self,name, course):
        super().__init__(name)
        self.course = course
    def show(self):
        super().show()
        print(f"Student Course : {self.course}")
class collagestudent(student):
    def __init__(self, name,course,collage):
        super().__init__(name,course)
        self.collage = collage
    def show(self):
        super().show()
        print(f"Student Collage {self.collage}")

student1 = collagestudent("Anmol Singh",
                          "BCA",
                          "SIT") 
student1.show()