"""
Database Setup Script
Run this script to initialize the hospital database
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from models.database import Database


def setup_database():
    """Initialize the database with all required tables"""
    print("Setting up Hospital Management System database...")
    
    db = Database()
    db.create_tables()
    
    print("\nDatabase setup completed successfully!")
    print("You can now run the main application using: python main.py")


if __name__ == "__main__":
    setup_database()
