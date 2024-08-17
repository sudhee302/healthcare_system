from datetime import datetime, timedelta

class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis_history = []
        self.appointments = []

    def add_diagnosis(self, diagnosis, prescription):
        record = {
            'Date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'Diagnosis': diagnosis,
            'Prescription': prescription
        }
        self.diagnosis_history.append(record)

    def view_diagnosis_history(self):
        if not self.diagnosis_history:
            print(f"\nNo diagnosis history for {self.name} (ID: {self.patient_id}).")
        else:
            print(f"\nDiagnosis history for {self.name} (ID: {self.patient_id}):")
            for record in self.diagnosis_history:
                print(f"Date: {record['Date']}, Diagnosis: {record['Diagnosis']}, Prescription: {record['Prescription']}")

    def schedule_appointment(self, doctor, date_time):
        appointment = {
            'Doctor': doctor,
            'DateTime': date_time
        }
        self.appointments.append(appointment)

    def view_appointments(self):
        if not self.appointments:
            print(f"\nNo upcoming appointments for {self.name} (ID: {self.patient_id}).")
        else:
            print(f"\nUpcoming appointments for {self.name} (ID: {self.patient_id}):")
            for appointment in self.appointments:
                print(f"Doctor: {appointment['Doctor']}, Date & Time: {appointment['DateTime']}")

    def cancel_appointment(self, doctor, date_time):
        for appointment in self.appointments:
            if appointment['Doctor'] == doctor and appointment['DateTime'] == date_time:
                self.appointments.remove(appointment)
                print(f"\nAppointment with {doctor} on {date_time} has been cancelled.")
                return
        print(f"\nNo appointment found with {doctor} on {date_time}.")

class HealthMonitoringSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, gender):
        if patient_id in self.patients:
            print(f"\nPatient ID {patient_id} already exists. Cannot add duplicate patient.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, age, gender)
            print(f"\nPatient {name} (ID: {patient_id}) added successfully!")

    def view_patient(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            print(f"\nPatient ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}")
            patient.view_diagnosis_history()
            patient.view_appointments()
        else:
            print(f"\nNo record found for patient ID {patient_id}.")

    def add_diagnosis(self, patient_id, diagnosis, prescription):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.add_diagnosis(diagnosis, prescription)
            print(f"\nDiagnosis and prescription added for {patient.name} (ID: {patient_id}).")
        else:
            print(f"\nNo record found for patient ID {patient_id}. Cannot add diagnosis.")

    def schedule_appointment(self, patient_id, doctor, date_time):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.schedule_appointment(doctor, date_time)
            print(f"\nAppointment scheduled for {patient.name} (ID: {patient_id}) with Dr. {doctor} on {date_time}.")
        else:
            print(f"\nNo record found for patient ID {patient_id}. Cannot schedule appointment.")

    def cancel_appointment(self, patient_id, doctor, date_time):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.cancel_appointment(doctor, date_time)
        else:
            print(f"\nNo record found for patient ID {patient_id}. Cannot cancel appointment.")

    def reminder_system(self):
        print("\n--- Appointment Reminders ---")
        current_time = datetime.now()
        for patient in self.patients.values():
            for appointment in patient.appointments:
                appointment_time = datetime.strptime(appointment['DateTime'], '%Y-%m-%d %H:%M')
                if appointment_time - current_time < timedelta(hours=24):
                    print(f"Reminder: {patient.name} (ID: {patient.patient_id}) has an appointment with Dr. {appointment['Doctor']} on {appointment['DateTime']}.")

def main_menu():
    system = HealthMonitoringSystem()
    
    while True:
        print("\n--- Automatic Health Monitoring System ---")
        print("1. Add Patient Record")
        print("2. View Patient Record")
        print("3. Add Diagnosis")
        print("4. Schedule Appointment")
        print("5. Cancel Appointment")
        print("6. View Appointment Reminders")
        print("7. Exit")
        
        choice = input("Enter your choice (1/7): ")
        
        if choice == '1':
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender: ")
            system.add_patient(patient_id, name, age, gender)
        
        elif choice == '2':
            patient_id = input("Enter Patient ID: ")
            system.view_patient(patient_id)
        
        elif choice == '3':
            patient_id = input("Enter Patient ID: ")
            diagnosis = input("Enter Diagnosis: ")
            prescription = input("Enter Prescription: ")
            system.add_diagnosis(patient_id, diagnosis, prescription)
        
        elif choice == '4':
            patient_id = input("Enter Patient ID: ")
            doctor = input("Enter Doctor's Name: ")
            date_time = input("Enter Appointment Date & Time (YYYY-MM-DD HH:MM): ")
            system.schedule_appointment(patient_id, doctor, date_time)
        
        elif choice == '5':
            patient_id = input("Enter Patient ID: ")
            doctor = input("Enter Doctor's Name: ")
            date_time = input("Enter Appointment Date & Time (YYYY-MM-DD HH:MM): ")
            system.cancel_appointment(patient_id, doctor, date_time)
        
        elif choice == '6':
            system.reminder_system()
        
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Start the application
if __name__ == "__main__":
    main_menu()
