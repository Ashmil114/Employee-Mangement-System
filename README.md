# Employee Management System API

## Introduction
The Employee Management System (EMS) is a web-based application designed to streamline the management of employee records, departments, and roles within an organization. This system provides functionalities such as user authentication, employee CRUD operations, department assignments, and more.

## Features
- User authentication (JWT)
- Employee CRUD operations
- Department management
- Role-based access control


## Technologies Used
- **Backend:** Django, Django Rest Framework
- **Database:** PostgreSQL
- **Authentication:** JWT

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Ashmil114/Employee-Mangement-System.git
    cd Employee-Mangement-System
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    

4. Set up the PostgreSQL database and update the `DATABASES` setting in `settings.py`.

5. Run migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
- Access the backend API at `http://localhost:8000/api/`.

## Contributing
We welcome contributions to this project. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

