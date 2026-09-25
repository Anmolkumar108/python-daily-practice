class Person:
    def show_name(self):
        print("My name is Anmol")

class student(Person):
    def study(self):
        print("I am studying BCA")
student1 = student()
student1.show_name()
student1.study()