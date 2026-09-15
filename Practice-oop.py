class student:
    collage = "SIT"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_detail(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Collage : {self.collage}")
    def input_detail(self):
        self.name = input("Enter Student Name : ")
        self.age = int(input("Enter Age : "))
    def change_college(self):
        self.collage = "MIT"

student1 = student("", 0)
student1.input_detail()
print("---------------------------")
print("Second Student Detaile's")
print("---------------------------")
student2 = student("", 0)
student2.input_detail()
student2.change_college()
print("\n--- Employee Details ---")
student1.show_detail()
print()
student2.show_detail()
