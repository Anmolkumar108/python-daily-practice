# class Person:
#     def show_name(self):
#         print("My name is Anmol")

# class student(Person):
#     def study(self):
#         print("I am studying BCA")
# student1 = student()
# student1.show_name()
# student1.study()

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class student (person) :
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course
    def show_detail(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age} ")
        print(f"course : {self.course}")
student1 = student("Anmol Singh",19,"BCA")
student1.show_detail()