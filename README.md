# Capstone Project: Student Management System

## Project Overview
This project is a Student Management System built using Python. It allows users to manage student data, including adding new students, updating existing student information, deleting students (soft delete), and viewing student insights. The system also features a login feature to differentiate between ADMIN and GUEST roles, restricting access to certain features based on the user's role.

The system uses a dictionary-based data structure (siswaDict) to store student information, such as NIS, name, class, and grades.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete student data.
  - **Create**: Add new students with unique NIS.
  - **Read**: View student details and grades.
  - **Update**: Modify student information like name, class, and grades.
  - **Delete**: Soft delete students and move them to the Recycle Bin.
- **Insights**: View statistical insights such as the most difficult/least difficult subjects and the overall graduation rate.
- **Role-Based Access**: Admin has full access to all features, while Guests are restricted from editing and deleting data.

### Technologies Used
- **Python**: For the backend logic.
- **Tabulate**: For rendering tabular data.

## Installation
### Clone the Repository:
```bash
git clone https://github.com/bonifasiusx/capstone-python-crud.git\
```
### Navigate to the Project Directory:
```cd capstone-python-crud```
### Run the Program:
Simply execute the main.py script to start the program:
```python main.py```

### Dependencies:
- Python 3.x
- tabulate library for formatting tables:
pip install tabulate

### Usage
1. When prompted, enter ADMIN credentials for full access.
2. The system will guide you through the menu where you can:
    - **View Student Data**: Display student details in a table format.
    - **Add New Student**: Input the details of a new student (name, class, grades).
    - **Edit Student Data**: Modify an existing student's information.
    - **Delete Student**: Soft delete a student's data (move to Recycle Bin).
    - **View Insights**: Check subject performance (most difficult/easiest) and graduation rate.
    - **Recycle Bin**: Restore or permanently delete soft-deleted student data.

### Folder Structure
```bash
Capstone Project/
│
├── create.py            # Contains logic to create new student records
├── read.py              # Contains logic to read and display student data
├── update.py            # Contains logic to update existing student records
├── delete.py            # Contains logic to delete (soft delete) student records
├── insight.py           # Contains logic to generate insights (subject difficulty, graduation rate)
├── menuConsole.py       # Main menu logic, including login and access control
├── Utilities.py         # Helper functions for input validation, checking OS, etc.
├── Database.py          # Contains the student data structure (siswaDict)
└── README.md            # Documentation of the project
```

### How to Contribute
Feel free to fork the project and submit pull requests. Contributions are welcome!