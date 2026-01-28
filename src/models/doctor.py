"""
Doctor Model
Handles all doctor-related operations
"""
from models.database import Database


class Doctor:
    """Doctor management class"""
    
    def __init__(self):
        self.db = Database()
    
    def add_doctor(self, name, specialization, contact, email=""):
        """Add a new doctor to the database"""
        query = """
            INSERT INTO doctors (name, specialization, contact, email)
            VALUES (?, ?, ?, ?)
        """
        params = (name, specialization, contact, email)
        doctor_id = self.db.execute_insert(query, params)
        return doctor_id
    
    def get_all_doctors(self):
        """Retrieve all doctors"""
        query = "SELECT * FROM doctors ORDER BY name"
        return self.db.execute_query(query)
    
    def get_doctor_by_id(self, doctor_id):
        """Retrieve a specific doctor by ID"""
        query = "SELECT * FROM doctors WHERE id = ?"
        results = self.db.execute_query(query, (doctor_id,))
        return results[0] if results else None
    
    def update_doctor(self, doctor_id, name, specialization, contact, email):
        """Update doctor information"""
        query = """
            UPDATE doctors 
            SET name = ?, specialization = ?, contact = ?, email = ?
            WHERE id = ?
        """
        params = (name, specialization, contact, email, doctor_id)
        self.db.execute_query(query, params)
        return True
    
    def delete_doctor(self, doctor_id):
        """Delete a doctor from the database"""
        query = "DELETE FROM doctors WHERE id = ?"
        self.db.execute_query(query, (doctor_id,))
        return True
    
    def search_doctors(self, search_term):
        """Search doctors by name or specialization"""
        query = """
            SELECT * FROM doctors 
            WHERE name LIKE ? OR specialization LIKE ?
            ORDER BY name
        """
        search_pattern = f"%{search_term}%"
        return self.db.execute_query(query, (search_pattern, search_pattern))
    
    def get_doctors_by_specialization(self, specialization):
        """Get all doctors with a specific specialization"""
        query = "SELECT * FROM doctors WHERE specialization = ? ORDER BY name"
        return self.db.execute_query(query, (specialization,))
