"""
Hospital Management System - Main Application
A comprehensive system for managing hospital operations
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from models.database import Database
from controllers.hospital_controller import HospitalController
from utils.display import Display


class HospitalManagementSystem:
    """Main application class"""
    
    def __init__(self):
        self.controller = HospitalController()
        self.display = Display()
        self.running = True
    
    def initialize_database(self):
        """Initialize the database with tables"""
        db = Database()
        db.create_tables()
    
    def main_menu(self):
        """Display main menu"""
        self.display.print_header("Hospital Management System")
        options = [
            "Patient Management",
            "Doctor Management",
            "Appointment Management",
            "View All Records",
            "Search",
            "Initialize/Reset Database"
        ]
        self.display.print_menu(options)
    
    def patient_menu(self):
        """Patient management menu"""
        self.display.print_header("Patient Management")
        options = [
            "Add New Patient",
            "View All Patients",
            "Search Patient",
            "Update Patient",
            "Delete Patient"
        ]
        self.display.print_menu(options)
    
    def doctor_menu(self):
        """Doctor management menu"""
        self.display.print_header("Doctor Management")
        options = [
            "Add New Doctor",
            "View All Doctors",
            "Search Doctor",
            "Update Doctor",
            "Delete Doctor"
        ]
        self.display.print_menu(options)
    
    def appointment_menu(self):
        """Appointment management menu"""
        self.display.print_header("Appointment Management")
        options = [
            "Create New Appointment",
            "View All Appointments",
            "View Patient Appointments",
            "View Doctor Appointments",
            "Cancel Appointment",
            "Complete Appointment"
        ]
        self.display.print_menu(options)
    
    def add_patient_flow(self):
        """Flow for adding a new patient"""
        self.display.print_header("Add New Patient")
        
        try:
            name = input("Enter patient name: ").strip()
            age = input("Enter age: ").strip()
            gender = input("Enter gender (M/F/Other): ").strip()
            contact = input("Enter contact number (10 digits): ").strip()
            address = input("Enter address (optional): ").strip()
            
            patient_id, message = self.controller.add_patient(name, age, gender, contact, address)
            
            if patient_id:
                self.display.print_success(f"{message} (ID: {patient_id})")
            else:
                self.display.print_error(message)
        except Exception as e:
            self.display.print_error(f"Failed to add patient: {str(e)}")
    
    def view_all_patients(self):
        """Display all patients"""
        self.display.print_header("All Patients")
        patients = self.controller.get_all_patients()
        
        if not patients:
            print("No patients found.")
            return
        
        for patient in patients:
            self.display.print_patient(patient)
    
    def add_doctor_flow(self):
        """Flow for adding a new doctor"""
        self.display.print_header("Add New Doctor")
        
        try:
            name = input("Enter doctor name: ").strip()
            specialization = input("Enter specialization: ").strip()
            contact = input("Enter contact number (10 digits): ").strip()
            email = input("Enter email (optional): ").strip()
            
            doctor_id, message = self.controller.add_doctor(name, specialization, contact, email)
            
            if doctor_id:
                self.display.print_success(f"{message} (ID: {doctor_id})")
            else:
                self.display.print_error(message)
        except Exception as e:
            self.display.print_error(f"Failed to add doctor: {str(e)}")
    
    def view_all_doctors(self):
        """Display all doctors"""
        self.display.print_header("All Doctors")
        doctors = self.controller.get_all_doctors()
        
        if not doctors:
            print("No doctors found.")
            return
        
        for doctor in doctors:
            self.display.print_doctor(doctor)
    
    def create_appointment_flow(self):
        """Flow for creating a new appointment"""
        self.display.print_header("Create New Appointment")
        
        try:
            patient_id = input("Enter patient ID: ").strip()
            doctor_id = input("Enter doctor ID: ").strip()
            date = input("Enter appointment date (YYYY-MM-DD): ").strip()
            time = input("Enter appointment time (HH:MM): ").strip()
            notes = input("Enter notes (optional): ").strip()
            
            appointment_id, message = self.controller.create_appointment(
                patient_id, doctor_id, date, time, notes
            )
            
            if appointment_id:
                self.display.print_success(f"{message} (ID: {appointment_id})")
            else:
                self.display.print_error(message)
        except Exception as e:
            self.display.print_error(f"Failed to create appointment: {str(e)}")
    
    def view_all_appointments(self):
        """Display all appointments"""
        self.display.print_header("All Appointments")
        appointments = self.controller.get_all_appointments()
        
        if not appointments:
            print("No appointments found.")
            return
        
        for appointment in appointments:
            self.display.print_appointment(appointment)
    
    def run(self):
        """Main application loop"""
        print("\n" + "=" * 60)
        print("  Welcome to Hospital Management System")
        print("=" * 60)
        
        while self.running:
            try:
                self.main_menu()
                choice = input("\nEnter your choice: ").strip()
                
                if choice == "0":
                    print("\nThank you for using Hospital Management System!")
                    self.running = False
                elif choice == "1":
                    self.patient_menu()
                    sub_choice = input("\nEnter your choice: ").strip()
                    if sub_choice == "1":
                        self.add_patient_flow()
                    elif sub_choice == "2":
                        self.view_all_patients()
                elif choice == "2":
                    self.doctor_menu()
                    sub_choice = input("\nEnter your choice: ").strip()
                    if sub_choice == "1":
                        self.add_doctor_flow()
                    elif sub_choice == "2":
                        self.view_all_doctors()
                elif choice == "3":
                    self.appointment_menu()
                    sub_choice = input("\nEnter your choice: ").strip()
                    if sub_choice == "1":
                        self.create_appointment_flow()
                    elif sub_choice == "2":
                        self.view_all_appointments()
                elif choice == "6":
                    confirm = input("This will reset the database. Continue? (yes/no): ")
                    if confirm.lower() == "yes":
                        self.initialize_database()
                        self.display.print_success("Database initialized successfully!")
                else:
                    print("Invalid choice. Please try again.")
                
                if self.running:
                    input("\nPress Enter to continue...")
            
            except KeyboardInterrupt:
                print("\n\nExiting...")
                self.running = False
            except Exception as e:
                self.display.print_error(f"An error occurred: {str(e)}")
                input("\nPress Enter to continue...")


def main():
    """Entry point of the application"""
    app = HospitalManagementSystem()
    
    # Check if database exists, if not initialize it
    if not os.path.exists("hospital.db"):
        print("Initializing database for the first time...")
        app.initialize_database()
    
    app.run()


if __name__ == "__main__":
    main()
