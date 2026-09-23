class student: 
    def __init__(self, name="", age=0, course="", marks=0, RollNumber="", college="SIT"): 
        self.name = name 
        self.age = age 
        self.course = course 
        self.marks = marks 
        self.RollNumber = RollNumber 
        self.college = college 
        
    def input_detail(self): 
        print("\n--- Enter Student Details ---")
        self.name = input("Enter Student Name   : ") 
        self.age = int(input("Enter Age            : ")) 
        self.course = input("Enter Course         : ") 
        self.RollNumber = input("Enter Roll Number    : ") 
        self.marks = int(input("Enter Marks          : ")) 
        print("✔ Student Added Successfully!")
        
    def show_detail(self): 
        print("-" * 40)
        print(f"| Roll Number   : {self.RollNumber:<23} |") 
        print(f"| Student Name  : {self.name:<23} |") 
        print(f"| Student Age   : {self.age:<23} |") 
        print(f"| College Name  : {self.college:<23} |") 
        print(f"| Course        : {self.course:<23} |") 
        print(f"| Marks         : {self.marks:<23} |") 
        print("-" * 40)
        
    def change_college(self): 
        
        new_college = input(f"Enter new college name for {self.name}: ")
        self.college = new_college 
        print(f"✔ College changed to {self.college} for {self.name}!")

    def update_marks(self):
        new_marks = int(input(f"Enter new marks for {self.name}: "))
        self.marks = new_marks
        print(f"✔ Marks updated successfully to {self.marks}!")
        
    @staticmethod 
    def welcome(): 
        print("\n=============================================")
        print("======== STUDENT MANAGEMENT SYSTEM =========") 
        print("=============================================")


student_list = [] 

while True:
    print("\n1. Add Student")
    print("2. Show Student Details")
    print("3. Change College")
    print("4. Update Marks")
    print("5. Show Welcome Message")
    print("6. Exit")
    
    choice = input("\nSelect an option (1-6): ")
    
    if choice == "1":
        s = student()
        s.input_detail()
        student_list.append(s)
        
    elif choice == "2":
        if not student_list:
            print("⚠ No students found! Please add a student first.")
        else:
            print("\n================ ALL STUDENTS ================")
            for s in student_list:
                s.show_detail()
                
    elif choice == "3":
        if not student_list:
            print("⚠ No students found!")
        else:
           
            roll = input("Enter the Roll Number of the student: ")
            found = False
            for s in student_list:
                if s.RollNumber == roll:
                    s.change_college() 
                    found = True
                    break
            if not found:
                print("⚠ Student with this Roll Number not found.")
                
    elif choice == "4":
        if not student_list:
            print("⚠ No students found!")
        else:
            
            roll = input("Enter the Roll Number of the student: ")
            found = False
            for s in student_list:
                if s.RollNumber == roll:
                    s.update_marks()
                    found = True
                    break
            if not found:
                print("⚠ Student with this Roll Number not found.")
                
    elif choice == "5":
        student.welcome()
        
    elif choice == "6":
        print("\nThank you for using Student Management System! Goodbye. 👋")
        break
        
    else:
        print("⚠ Invalid Choice! Please enter a number between 1 and 6.")