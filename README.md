# Hospital Management System

A comprehensive Python-based Hospital Management System for managing patients, doctors, and appointments.

## Features

- **Patient Management**: Add, view, update, and search patient records
- **Doctor Management**: Manage doctor information including specializations
- **Appointment Scheduling**: Create and manage appointments between patients and doctors
- **Database Management**: SQLite-based database for persistent storage
- **Input Validation**: Comprehensive validation for all user inputs
- **User-Friendly Interface**: Console-based interactive menu system

## Project Structure

```
HospitalManagement/
├── main.py                 # Main application entry point
├── setup.py               # Database setup script
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── src/
    ├── models/           # Data models
    │   ├── database.py   # Database management
    │   ├── patient.py    # Patient model
    │   ├── doctor.py     # Doctor model
    │   └── appointment.py # Appointment model
    ├── controllers/      # Business logic
    │   └── hospital_controller.py
    └── utils/           # Utility functions
        ├── validators.py # Input validation
        └── display.py    # Display utilities
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Nithin-s1/HospitalManagement.git
cd HospitalManagement
```

2. Install dependencies (Python 3.6+ required):
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python setup.py
```

## Usage

Run the main application:
```bash
python main.py
```

The system will present you with an interactive menu where you can:

1. **Patient Management**
   - Add new patients
   - View all patients
   - Search for patients
   - Update patient information
   - Delete patient records

2. **Doctor Management**
   - Add new doctors
   - View all doctors
   - Search for doctors
   - Update doctor information
   - Delete doctor records

3. **Appointment Management**
   - Create new appointments
   - View all appointments
   - View appointments by patient
   - View appointments by doctor
   - Cancel appointments
   - Mark appointments as completed

## Database Schema

### Patients Table
- id (Primary Key)
- name
- age
- gender
- contact
- address
- created_at

### Doctors Table
- id (Primary Key)
- name
- specialization
- contact
- email
- created_at

### Appointments Table
- id (Primary Key)
- patient_id (Foreign Key)
- doctor_id (Foreign Key)
- appointment_date
- appointment_time
- status
- notes
- created_at

## Requirements

- Python 3.6 or higher
- SQLite3 (included with Python)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for educational purposes.