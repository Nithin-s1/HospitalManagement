"""
Hospital Management System - Controller Module
Handles business logic and coordinates between models and views
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from utils.validators import Validator


class HospitalController:
    """Main controller for hospital management operations"""
    
    def __init__(self):
        self.patient_model = Patient()
        self.doctor_model = Doctor()
        self.appointment_model = Appointment()
        self.validator = Validator()
    
    # Patient Operations
    def add_patient(self, name, age, gender, contact, address=""):
        """Add a new patient with validation"""
        if not self.validator.validate_name(name):
            return None, "Invalid name"
        if not self.validator.validate_age(age):
            return None, "Invalid age"
        if not self.validator.validate_gender(gender):
            return None, "Invalid gender"
        if not self.validator.validate_contact(contact):
            return None, "Invalid contact number"
        
        patient_id = self.patient_model.add_patient(name, age, gender, contact, address)
        return patient_id, "Patient added successfully"
    
    def get_all_patients(self):
        """Get all patients"""
        return self.patient_model.get_all_patients()
    
    def search_patients(self, search_term):
        """Search for patients"""
        return self.patient_model.search_patients(search_term)
    
    # Doctor Operations
    def add_doctor(self, name, specialization, contact, email=""):
        """Add a new doctor with validation"""
        if not self.validator.validate_name(name):
            return None, "Invalid name"
        if not self.validator.validate_contact(contact):
            return None, "Invalid contact number"
        if email and not self.validator.validate_email(email):
            return None, "Invalid email address"
        
        doctor_id = self.doctor_model.add_doctor(name, specialization, contact, email)
        return doctor_id, "Doctor added successfully"
    
    def get_all_doctors(self):
        """Get all doctors"""
        return self.doctor_model.get_all_doctors()
    
    def search_doctors(self, search_term):
        """Search for doctors"""
        return self.doctor_model.search_doctors(search_term)
    
    # Appointment Operations
    def create_appointment(self, patient_id, doctor_id, appointment_date, appointment_time, notes=""):
        """Create a new appointment with validation"""
        if not self.validator.validate_date(appointment_date):
            return None, "Invalid date format (use YYYY-MM-DD)"
        if not self.validator.validate_time(appointment_time):
            return None, "Invalid time format (use HH:MM)"
        
        appointment_id = self.appointment_model.create_appointment(
            patient_id, doctor_id, appointment_date, appointment_time, notes
        )
        return appointment_id, "Appointment created successfully"
    
    def get_all_appointments(self):
        """Get all appointments"""
        return self.appointment_model.get_all_appointments()
    
    def get_patient_appointments(self, patient_id):
        """Get appointments for a patient"""
        return self.appointment_model.get_patient_appointments(patient_id)
    
    def get_doctor_appointments(self, doctor_id):
        """Get appointments for a doctor"""
        return self.appointment_model.get_doctor_appointments(doctor_id)
    
    def cancel_appointment(self, appointment_id):
        """Cancel an appointment"""
        return self.appointment_model.cancel_appointment(appointment_id)
    
    def complete_appointment(self, appointment_id):
        """Mark appointment as completed"""
        return self.appointment_model.complete_appointment(appointment_id)
