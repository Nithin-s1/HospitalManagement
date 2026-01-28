"""
Appointment Model
Handles all appointment-related operations
"""
from models.database import Database


class Appointment:
    """Appointment management class"""
    
    def __init__(self):
        self.db = Database()
    
    def create_appointment(self, patient_id, doctor_id, appointment_date, appointment_time, notes=""):
        """Create a new appointment"""
        query = """
            INSERT INTO appointments 
            (patient_id, doctor_id, appointment_date, appointment_time, notes)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (patient_id, doctor_id, appointment_date, appointment_time, notes)
        appointment_id = self.db.execute_insert(query, params)
        return appointment_id
    
    def get_all_appointments(self):
        """Retrieve all appointments with patient and doctor details"""
        query = """
            SELECT a.id, p.name as patient_name, d.name as doctor_name,
                   a.appointment_date, a.appointment_time, a.status, a.notes
            FROM appointments a
            JOIN patients p ON a.patient_id = p.id
            JOIN doctors d ON a.doctor_id = d.id
            ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """
        return self.db.execute_query(query)
    
    def get_appointment_by_id(self, appointment_id):
        """Retrieve a specific appointment by ID"""
        query = """
            SELECT a.*, p.name as patient_name, d.name as doctor_name
            FROM appointments a
            JOIN patients p ON a.patient_id = p.id
            JOIN doctors d ON a.doctor_id = d.id
            WHERE a.id = ?
        """
        results = self.db.execute_query(query, (appointment_id,))
        return results[0] if results else None
    
    def get_patient_appointments(self, patient_id):
        """Get all appointments for a specific patient"""
        query = """
            SELECT a.*, d.name as doctor_name, d.specialization
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.id
            WHERE a.patient_id = ?
            ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """
        return self.db.execute_query(query, (patient_id,))
    
    def get_doctor_appointments(self, doctor_id):
        """Get all appointments for a specific doctor"""
        query = """
            SELECT a.*, p.name as patient_name, p.contact
            FROM appointments a
            JOIN patients p ON a.patient_id = p.id
            WHERE a.doctor_id = ?
            ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """
        return self.db.execute_query(query, (doctor_id,))
    
    def update_appointment_status(self, appointment_id, status):
        """Update appointment status"""
        query = "UPDATE appointments SET status = ? WHERE id = ?"
        self.db.execute_query(query, (status, appointment_id))
        return True
    
    def cancel_appointment(self, appointment_id):
        """Cancel an appointment"""
        return self.update_appointment_status(appointment_id, "cancelled")
    
    def complete_appointment(self, appointment_id):
        """Mark an appointment as completed"""
        return self.update_appointment_status(appointment_id, "completed")
    
    def delete_appointment(self, appointment_id):
        """Delete an appointment"""
        query = "DELETE FROM appointments WHERE id = ?"
        self.db.execute_query(query, (appointment_id,))
        return True
