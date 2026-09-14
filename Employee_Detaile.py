class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def show_detail(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"Department : {self.department}")

    def input_detail(self):
        self.name = input("Enter Employee Name : ")
        self.salary = int(input("Enter Salary : "))
        self.department = input("Enter Department : ")


employee1 = Employee("", 0, "")
employee1.input_detail()
print("\n--- Employee Details ---")
employee1.show_detail()