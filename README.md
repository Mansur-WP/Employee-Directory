# Employee Directory

A modern Django web application for managing and viewing employee information. This project features a clean Bootstrap interface, employee detail pages, and image support.

## Features

- List all employees with names, designations, and phone numbers
- Click on an employee to view detailed information in a stylish card format
- Upload and display employee profile images
- Responsive design using Bootstrap 5
- Media and static file support
- Admin interface for managing employees

## Screenshots

![Home Page](mysite/static/images/logo.png)

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- (Recommended) Virtual environment tool such as `venv`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mansur-WP/Employee-Directory.git
   cd Employee-Directory
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django pillow
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   - Home page: [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure

```
├── employees/           # Employee app (models, views, urls)
├── mysite/              # Project settings and main urls
├── templates/           # HTML templates
├── media/               # Uploaded images
├── static/              # Static files (CSS, images)
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── .gitignore           # Git ignore file
```

## License

This project is licensed under the MIT License.

---

Made with ❤️ using Django and Bootstrap.
