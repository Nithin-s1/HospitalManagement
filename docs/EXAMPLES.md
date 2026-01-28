# Example Usage Guide

This guide demonstrates common operations in the Hospital Management System.

## Adding a Patient

```python
from models.patient import Patient

patient = Patient()
patient_id = patient.add_patient(
    name="John Doe",
    age=35,
    gender="Male",
    contact="9876543210",
    address="123 Main Street"
)
print(f"Patient added with ID: {patient_id}")
```

## Adding a Doctor

```python
from models.doctor import Doctor

doctor = Doctor()
doctor_id = doctor.add_doctor(
    name="Dr. Sarah Smith",
    specialization="Cardiology",
    contact="9876543211",
    email="sarah.smith@hospital.com"
)
print(f"Doctor added with ID: {doctor_id}")
```

## Creating an Appointment

```python
from models.appointment import Appointment

appointment = Appointment()
appointment_id = appointment.create_appointment(
    patient_id=1,
    doctor_id=1,
    appointment_date="2026-02-01",
    appointment_time="10:30",
    notes="Regular checkup"
)
print(f"Appointment created with ID: {appointment_id}")
```

## Searching for Patients

```python
from models.patient import Patient

patient = Patient()
results = patient.search_patients("John")
for patient_record in results:
    print(f"ID: {patient_record[0]}, Name: {patient_record[1]}")
```

## Getting Doctor's Appointments

```python
from models.appointment import Appointment

appointment = Appointment()
appointments = appointment.get_doctor_appointments(doctor_id=1)
for appt in appointments:
    print(f"Patient: {appt[7]}, Date: {appt[3]}, Time: {appt[4]}")
```

## Using the Controller

The controller provides validation and a unified interface:

```python
from controllers.hospital_controller import HospitalController

controller = HospitalController()

# Add patient with validation
patient_id, message = controller.add_patient(
    name="Jane Doe",
    age=28,
    gender="Female",
    contact="9876543212",
    address="456 Oak Avenue"
)

if patient_id:
    print(f"Success: {message}")
else:
    print(f"Error: {message}")
```

## Running the Interactive Application

Simply run:
```bash
python main.py
```

Follow the on-screen menu to perform operations interactively.
