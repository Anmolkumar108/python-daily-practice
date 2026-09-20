class student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
        
    def get_age(self):
        return self.__age
        
    def set_Name(self, name):
        self.__name = name
        
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid Age")

student1 = student("Anmol Singh", 19)
print(student1.get_name()) 
print(student1.get_age())  
print()
student1.set_Name("Vicky Singh")
student1.set_age(23)

print(student1.get_name()) 
print(student1.get_age())   
