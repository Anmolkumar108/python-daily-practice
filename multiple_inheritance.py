class father:
    def __init__(self , father_name , father_occupation,**kwargs):
        self.father_name = father_name
        self.father_occupation = father_occupation
        super().__init__(**kwargs)
    def show_father(self):
        print(f"Father Name : {self.father_name}")
        print(f"Father Occupation : {self.father_occupation}")
class mother:
    def __init__(self , mother_name , mother_occupation,**kwargs):
        self.mother_name = mother_name
        self.mother_occupation = mother_occupation
        super().__init__(**kwargs)
    def show_mother(self):
        print(f"Mother Name : {self.mother_name}")
        print(f"Mother Occupation : {self.mother_occupation}")

class child (father , mother):
   def __init__ (self , father_name , father_occupation , mother_name , mother_occupation):
       super().__init__(father_name=father_name,
                        father_occupation=father_occupation,
                        mother_name=mother_name,
                        mother_occupation = mother_occupation)

child1 = child("Manish Singh",
               "Farmer",
               "Rupi Devi",
               "HouseWife")
child1.show_father()
print()
child1.show_mother()

        