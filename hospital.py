class Person:
    def __init__(self, name, age, gender, mobile):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Mobile: {self.mobile}"


class Doctor(Person):
    def __init__(self, name, age, gender, mobile, specialization):
        super().__init__(name, age, gender, mobile)
        self.specialization = specialization

    def __str__(self):
        return super().__str__() + f", Specialization: {self.specialization}"


class MedicalRecord:
    def __init__(self, diagnosis, treatment, date):
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.date = date

    def __str__(self):
        return f"Diagnosis: {self.diagnosis}, Treatment: {self.treatment}, Date: {self.date}"


class Patient(Person):
    def __init__(self, name, age, gender, mobile, patient_id):
        super().__init__(name, age, gender, mobile)
        self.patient_id = patient_id
        self.medical_history = []  # list of MedicalRecord

    def add_medical_record(self, diagnosis, treatment, date):
        record = MedicalRecord(diagnosis, treatment, date)
        self.medical_history.append(record)

    def __str__(self):
        return super().__str__() + f", Patient ID: {self.patient_id}"


class HospitalManagementSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []

    # ---------------- Doctor ----------------
    def add_doctor(self):
        name = input("Enter Doctor Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        mobile = input("Enter Mobile: ")
        specialization = input("Enter Specialization: ")
        doctor = Doctor(name, age, gender, mobile, specialization)
        self.doctors.append(doctor)
        print(" Doctor Added Successfully!\n")

    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.\n")
        else:
            for doc in self.doctors:
                print(doc)

    def update_doctor(self, mobile):
        for doc in self.doctors:
            if doc.mobile == mobile:
                name = input("Enter new Name (press enter to skip): ")
                age = input("Enter new Age (press enter to skip): ")
                gender = input("Enter new Gender (press enter to skip): ")
                specialization = input("Enter new Specialization (press enter to skip): ")

                if name: doc.name = name
                if age: doc.age = age
                if gender: doc.gender = gender
                if specialization: doc.specialization = specialization

                print("Doctor Updated!\n")
                return
        print("Doctor not found.\n")

    def delete_doctor(self, mobile):
        for doc in self.doctors:
            if doc.mobile == mobile:
                self.doctors.remove(doc)
                print(" Doctor Deleted!\n")
                return
        print("Doctor not found.\n")

    # ---------------- Patient ----------------
    def add_patient(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        mobile = input("Enter Mobile: ")
        patient_id = input("Enter Patient ID: ")
        patient = Patient(name, age, gender, mobile, patient_id)
        self.patients.append(patient)
        print(" Patient Added Successfully!\n")

    def view_patients(self):
        if not self.patients:
            print("No patients found.\n")
        else:
            for pat in self.patients:
                print(pat)

    def update_patient(self, mobile):
        for pat in self.patients:
            if pat.mobile == mobile:
                name = input("Enter new Name (press enter to skip): ")
                age = input("Enter new Age (press enter to skip): ")
                gender = input("Enter new Gender (press enter to skip): ")
                patient_id = input("Enter new Patient ID (press enter to skip): ")

                if name: pat.name = name
                if age: pat.age = age
                if gender: pat.gender = gender
                if patient_id: pat.patient_id = patient_id

                print(" Patient Updated!\n")
                return
        print("Patient not found.\n")

    def delete_patient(self, mobile):
        for pat in self.patients:
            if pat.mobile == mobile:
                self.patients.remove(pat)
                print("Patient Deleted!\n")
                return
        print("Patient not found.\n")

    # ---------------- Medical Records ----------------
    def add_medical_history(self, mobile):
        for pat in self.patients:
            if pat.mobile == mobile:
                diagnosis = input("Enter Diagnosis: ")
                treatment = input("Enter Treatment: ")
                date = input("Enter Date: ")
                pat.add_medical_record(diagnosis, treatment, date)
                print("Medical Record Added!\n")
                return
        print("Patient not found.\n")

    def search_patient_history(self, mobile):
        for pat in self.patients:
            if pat.mobile == mobile:
                print(f"Patient Found: {pat}")
                print("Medical History:")
                if pat.medical_history:
                    for rec in pat.medical_history:
                        print(rec)
                else:
                    print("No medical history available.")
                return
        print("Patient not found.\n")


# ---------------- Example Run ----------------
hms = HospitalManagementSystem()

# Add 2 doctors
hms.doctors.append(Doctor("Dr. Smith", 45, "Male", "1111", "Cardiology"))
hms.doctors.append(Doctor("Dr. Jane", 38, "Female", "2222", "Neurology"))

# Add 2 patients
p1 = Patient("Alice", 30, "Female", "3333", "P001")
p2 = Patient("Bob", 25, "Male", "4444", "P002")
hms.patients.append(p1)
hms.patients.append(p2)

# Add medical history for Alice
p1.add_medical_record("Fever", "Paracetamol", "2025-07-20")

# Display
print("---- Doctors ----")
hms.view_doctors()
print("\n---- Patients ----")
hms.view_patients()
print("\n---- Search Patient ----")
hms.search_patient_history("3333")
