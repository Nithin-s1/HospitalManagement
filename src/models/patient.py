"""
Patient Model
Handles all patient-related operations
"""
from models.database import Database


class Patient:
    """Patient management class"""
    
    def __init__(self):
        self.db = Database()
    
    def add_patient(self, name, age, gender, contact, address=""):
        """Add a new patient to the database"""
        query = """
            INSERT INTO patients (name, age, gender, contact, address)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (name, age, gender, contact, address)
        patient_id = self.db.execute_insert(query, params)
        return patient_id
    
    def get_all_patients(self):
        """Retrieve all patients"""
        query = "SELECT * FROM patients ORDER BY created_at DESC"
        return self.db.execute_query(query)
    
    def get_patient_by_id(self, patient_id):
        """Retrieve a specific patient by ID"""
        query = "SELECT * FROM patients WHERE id = ?"
        results = self.db.execute_query(query, (patient_id,))
        return results[0] if results else None
    
    def update_patient(self, patient_id, name, age, gender, contact, address):
        """Update patient information"""
        query = """
            UPDATE patients 
            SET name = ?, age = ?, gender = ?, contact = ?, address = ?
            WHERE id = ?
        """
        params = (name, age, gender, contact, address, patient_id)
        self.db.execute_query(query, params)
        return True
    
    def delete_patient(self, patient_id):
        """Delete a patient from the database"""
        query = "DELETE FROM patients WHERE id = ?"
        self.db.execute_query(query, (patient_id,))
        return True
    
    def search_patients(self, search_term):
        """Search patients by name or contact"""
        query = """
            SELECT * FROM patients 
            WHERE name LIKE ? OR contact LIKE ?
            ORDER BY name
        """
        search_pattern = f"%{search_term}%"
        return self.db.execute_query(query, (search_pattern, search_pattern))
