class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def check_patient(self, patient):
        print(f"{self.name}, is checking {patient.name} (age {patient.age}).")

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
doctor = Doctor("Dr. Sharma", "Cardiologist")
patient = Patient("Anmol Singh", 19)
doctor.check_patient(patient)
                

