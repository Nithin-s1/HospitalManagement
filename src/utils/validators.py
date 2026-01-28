"""
Validators Module
Contains validation functions for various inputs
"""
import re
from datetime import datetime


class Validator:
    """Input validation class"""
    
    @staticmethod
    def validate_name(name):
        """Validate name - should contain only letters, spaces, and periods"""
        if not name or len(name.strip()) < 2:
            return False
        return bool(re.match(r'^[a-zA-Z\s.]+$', name))
    
    @staticmethod
    def validate_age(age):
        """Validate age - should be between 0 and 150"""
        try:
            age_int = int(age)
            return 0 < age_int <= 150
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def validate_gender(gender):
        """Validate gender - should be Male, Female, or Other"""
        valid_genders = ['male', 'female', 'other', 'm', 'f', 'o']
        return gender.lower() in valid_genders
    
    @staticmethod
    def validate_contact(contact):
        """Validate contact number - should be 10 digits"""
        contact_str = str(contact).strip()
        return bool(re.match(r'^\d{10}$', contact_str))
    
    @staticmethod
    def validate_email(email):
        """Validate email address"""
        if not email:
            return True  # Email is optional
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_date(date_str):
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def validate_time(time_str):
        """Validate time format (HH:MM)"""
        try:
            datetime.strptime(time_str, '%H:%M')
            return True
        except (ValueError, TypeError):
            return False
