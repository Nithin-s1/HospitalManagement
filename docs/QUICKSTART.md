# Quick Start Guide

Get started with the Hospital Management System in just a few steps!

## Installation (1 minute)

```bash
# Clone the repository
git clone https://github.com/Nithin-s1/HospitalManagement.git
cd HospitalManagement

# Install dependencies (Python 3.6+ required)
pip install -r requirements.txt

# Initialize the database
python setup.py
```

## Running the Application

```bash
python main.py
```

## First Steps

1. **Add a Doctor**
   - Select option `2` (Doctor Management)
   - Select option `1` (Add New Doctor)
   - Enter doctor details

2. **Add a Patient**
   - Select option `1` (Patient Management)
   - Select option `1` (Add New Patient)
   - Enter patient details

3. **Create an Appointment**
   - Select option `3` (Appointment Management)
   - Select option `1` (Create New Appointment)
   - Enter patient ID and doctor ID (from steps 1-2)
   - Enter date (YYYY-MM-DD) and time (HH:MM)

## Common Tasks

### View All Patients
Main Menu → Option 1 → Option 2

### View All Doctors
Main Menu → Option 2 → Option 2

### View All Appointments
Main Menu → Option 3 → Option 2

### Search for a Patient
Main Menu → Option 1 → Option 3

### Reset Database
Main Menu → Option 6 → Type "yes" to confirm

## Tips

- Use 10-digit phone numbers for contacts
- Date format must be YYYY-MM-DD
- Time format must be HH:MM (24-hour format)
- Names can include spaces and periods
- Ages must be between 1 and 150

## Need Help?

- Check the [README.md](../README.md) for detailed documentation
- See [EXAMPLES.md](EXAMPLES.md) for code examples
- Read [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines
