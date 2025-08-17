class Person:
    def __init__(self, name, age, gender, mobileno):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobileno = mobileno

    def showinfo(self):
        print(f"Person Name: {self.name}")
        print(f"Person age: {self.age}")
        print(f"Person gender: {self.gender}")
        print(f"Person mobileno: {self.mobileno}")


class Doctor(Person):
    def __init__(self, name, age, gender, mobileno, specialization):
        super().__init__(name, age, gender, mobileno)
        self.specialization = specialization

    def showinfo(self):
        super().showinfo()
        print(f"Doctor Specialization: {self.specialization}")


class Patient(Person):
    def __init__(self, name, age, gender, mobileno, patientid):
        super().__init__(name, age, gender, mobileno)
        self.patientid = patientid
        self.medicalhistory = []

    def showinfo(self):
        super().showinfo()
        print(f"Patient ID: {self.patientid}")
        print(f"Medical Record: {self.medicalhistory}")


class MedicalRecord:
   def __init__(self, Diagnoses, Treatment, Date):
       self.Diagnoses = Diagnoses
       self.Treatment = Treatment
       self.Date = Date

   def show_record(self):
       print(f"Diagnoses: {self.Diagnoses}")
       print(f"Treatment: {self.Treatment}")
       print(f"Date: {self.Date}")


class hms:
    def __init__(self):
        self.doctor = []
        self.patient = []

    def add_doctor(self, doctor):
        self.doctor.append(doctor)

    def view_doctor(self):
        if not self.doctor:
            print("There is no record found")
        else:
            for doctor in self.doctor:
                doctor.showinfo()
                print("------")

    def update_doctor(self, name, new_age, new_gender, new_mobileno, new_specialization):
        if not self.doctor:
            print("There is no record found")
        else:
            for doctor in self.doctor:
                if doctor.name == name:
                    doctor.age = new_age
                    doctor.gender = new_gender
                    doctor.mobileno = new_mobileno
                    doctor.specialization = new_specialization
                    print(f"Doctor {name} updated successfully")
                    return
            print(f"No doctor found with name {name}")

    def delete_doctor(self, name):
        if not self.doctor:
            print("There is no record found")
        else:
            for doctor in self.doctor:
                if doctor.name == name:
                    self.doctor.remove(doctor)
                    print(f"Doctor {name} deleted successfully")
                    return
            print(f"No doctor found with name {name}")


# ---------- TESTING ----------
d1 = Doctor("Parth", 21, "Male", 9173230632, "Ortho")
d2 = Doctor("Riya", 30, "Female", 9876543210, "Cardio")

h1 = hms()
h1.add_doctor(d1)
h1.add_doctor(d2)

print("\n--- All Doctors ---")
h1.view_doctor()

print("\n--- Updating Parth ---")
h1.update_doctor("Parth", 22, "Female", 9173230632, "Neuro")
h1.view_doctor()

print("\n--- Deleting Riya ---")
h1.delete_doctor("Riya")
h1.view_doctor()
