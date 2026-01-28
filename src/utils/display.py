"""
Display Utilities
Functions for formatting and displaying data
"""


class Display:
    """Display utilities for console output"""
    
    @staticmethod
    def print_header(title):
        """Print a formatted header"""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)
    
    @staticmethod
    def print_patient(patient):
        """Display patient information"""
        print(f"ID: {patient[0]}")
        print(f"Name: {patient[1]}")
        print(f"Age: {patient[2]}")
        print(f"Gender: {patient[3]}")
        print(f"Contact: {patient[4]}")
        print(f"Address: {patient[5]}")
        print("-" * 40)
    
    @staticmethod
    def print_doctor(doctor):
        """Display doctor information"""
        print(f"ID: {doctor[0]}")
        print(f"Name: {doctor[1]}")
        print(f"Specialization: {doctor[2]}")
        print(f"Contact: {doctor[3]}")
        print(f"Email: {doctor[4]}")
        print("-" * 40)
    
    @staticmethod
    def print_appointment(appointment):
        """Display appointment information"""
        print(f"Appointment ID: {appointment[0]}")
        print(f"Patient: {appointment[1]}")
        print(f"Doctor: {appointment[2]}")
        print(f"Date: {appointment[3]}")
        print(f"Time: {appointment[4]}")
        print(f"Status: {appointment[5]}")
        if len(appointment) > 6 and appointment[6]:
            print(f"Notes: {appointment[6]}")
        print("-" * 40)
    
    @staticmethod
    def print_menu(options):
        """Print menu options"""
        print("\nPlease select an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("0. Exit")
    
    @staticmethod
    def print_success(message):
        """Print success message"""
        print(f"\n✓ {message}")
    
    @staticmethod
    def print_error(message):
        """Print error message"""
        print(f"\n✗ Error: {message}")
