# Step 1 — Doctor Class
class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.appointments = [] 

    def display_appointments(self):
        print(f"\n--- {self.name}'s Appointments ({self.specialization}) ---")
        if not self.appointments:
            print("No appointments scheduled.")
            return
        
        # Step 7 — Doctor ke appointments display loop
        for appt in self.appointments:
            print(f"Patient: {appt.patient.name}") 
            print(f"Date: {appt.date}")
            print(f"Time: {appt.time}")
            print(f"Reason: {appt.reason}")
            print(f"Status: {appt.status}")
            print("-" * 30)


# Step 2 — Patient Class
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.appointments = [] 

    def display_appointments(self):
        print(f"\n--- {self.name}'s Appointments ---")
        if not self.appointments:
            print("No appointments scheduled.")
            return

        # Step 8 — Patient ke appointments display loop
        for appt in self.appointments:
            print(f"Doctor: {appt.doctor.name}") 
            print(f"Date: {appt.date}")
            print(f"Time: {appt.time}")
            print(f"Reason: {appt.reason}")
            print(f"Status: {appt.status}")
            print("-" * 30)


# Step 3 — Appointment Class
class Appointment:
    def __init__(self, doctor, patient, date, time, reason):
        self.doctor = doctor       
        self.patient = patient     
        self.date = date
        self.time = time
        self.reason = reason
        self.status = "Scheduled"   # Default status
        
        # Step 5 & 6 — Dono ki lists me SAME appointment object add karna
        self.doctor.appointments.append(self)
        self.patient.appointments.append(self)

    # Step 9 — Appointment Cancel Method
    def cancel(self):
        self.status = "Cancelled"
        print(f"\n[Notification] Appointment for {self.patient.name} with {self.doctor.name} has been CANCELLED.")


# ==========================================
# VERSION 2 — MULTIPLE DOCTORS AND PATIENTS
# ==========================================

doctors = []
patients = []
appointments = []


def get_required_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_patient_age():
    while True:
        try:
            age = int(input("Patient age: ").strip())
            if age > 0:
                return age
            print("Age must be greater than 0.")
        except ValueError:
            print("Please enter age as a whole number.")


def print_section(title):
    print(f"\n{'=' * 56}\n  {title}\n{'=' * 56}")


def find_doctor(doctor_id):
    doctor_id = doctor_id.strip().upper()
    for doctor in doctors:
        if doctor.doctor_id.upper() == doctor_id:
            return doctor
    return None


def find_patient(patient_id):
    patient_id = patient_id.strip().upper()
    for patient in patients:
        if patient.patient_id.upper() == patient_id:
            return patient
    return None


def add_doctor():
    print_section("ADD DOCTOR")
    doctor_id = get_required_input("Doctor ID: ").upper()
    if find_doctor(doctor_id):
        print(f"Doctor ID {doctor_id} is already registered.")
        return

    name = get_required_input("Doctor name: ")
    specialization = get_required_input("Specialization: ")
    doctors.append(Doctor(doctor_id, name, specialization))
    print(f"Doctor {name} ({doctor_id}) added successfully.")


def add_patient():
    print_section("ADD PATIENT")
    patient_id = get_required_input("Patient ID: ").upper()
    if find_patient(patient_id):
        print(f"Patient ID {patient_id} is already registered.")
        return

    name = get_required_input("Patient name: ")
    age = get_patient_age()
    patients.append(Patient(patient_id, name, age))
    print(f"Patient {name} ({patient_id}) added successfully.")


def book_appointment():
    print_section("BOOK APPOINTMENT")
    doctor_id = get_required_input("Doctor ID: ").upper()
    doctor = find_doctor(doctor_id)
    if doctor is None:
        print(f"No doctor found with ID {doctor_id}. Add the doctor first.")
        return

    patient_id = get_required_input("Patient ID: ").upper()
    patient = find_patient(patient_id)
    if patient is None:
        print(f"No patient found with ID {patient_id}. Add the patient first.")
        return

    appointment_date = get_required_input("Date (for example, 10-10-2026): ")
    appointment_time = get_required_input("Time (for example, 10:00 AM): ")
    reason = get_required_input("Reason for visit: ")
    appointment = Appointment(doctor, patient, appointment_date, appointment_time, reason)
    appointments.append(appointment)

    print_section("APPOINTMENT CONFIRMED")
    print(f"Status       : {appointment.status}")
    print(f"Doctor       : {doctor.name} ({doctor.doctor_id}) - {doctor.specialization}")
    print(f"Patient      : {patient.name} ({patient.patient_id}), age {patient.age}")
    print(f"Date & time  : {appointment.date} at {appointment.time}")
    print(f"Reason       : {appointment.reason}")


def view_doctor_appointments():
    print_section("VIEW DOCTOR APPOINTMENTS")
    doctor_id = get_required_input("Doctor ID: ").upper()
    doctor = find_doctor(doctor_id)
    if doctor is None:
        print(f"No doctor found with ID {doctor_id}.")
        return
    doctor.display_appointments()


def view_patient_appointments():
    print_section("VIEW PATIENT APPOINTMENTS")
    patient_id = get_required_input("Patient ID: ").upper()
    patient = find_patient(patient_id)
    if patient is None:
        print(f"No patient found with ID {patient_id}.")
        return
    patient.display_appointments()


def cancel_appointment():
    print_section("CANCEL APPOINTMENT")
    if not appointments:
        print("There are no appointments to cancel.")
        return

    for index, appointment in enumerate(appointments, start=1):
        print(
            f"{index}. {appointment.patient.name} with {appointment.doctor.name} | "
            f"{appointment.date} at {appointment.time} | {appointment.status}"
        )

    while True:
        try:
            selection = int(input("Choose appointment number to cancel: ").strip())
            if 1 <= selection <= len(appointments):
                break
            print(f"Enter a number from 1 to {len(appointments)}.")
        except ValueError:
            print("Please enter a valid appointment number.")

    appointment = appointments[selection - 1]
    if appointment.status == "Cancelled":
        print("This appointment is already cancelled.")
        return
    appointment.cancel()


def show_menu():
    print_section("HOSPITAL APPOINTMENT SYSTEM")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Book Appointment")
    print("4. View Doctor Appointments")
    print("5. View Patient Appointments")
    print("6. Cancel Appointment")
    print("7. Exit")


def main():
    actions = {
        "1": add_doctor,
        "2": add_patient,
        "3": book_appointment,
        "4": view_doctor_appointments,
        "5": view_patient_appointments,
        "6": cancel_appointment,
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "7":
            print_section("THANK YOU")
            print("Hospital Appointment System closed.")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid option. Please choose a number from 1 to 7.")
            continue
        action()


if __name__ == "__main__":
    main()
