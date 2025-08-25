Little Lemon Web Application (Django REST Framework + MySQL)

Requirements
-----------
- Python 3.10+
- MySQL Server (create a DB first, e.g., `CREATE DATABASE littlelemon CHARACTER SET utf8mb4;`)
- `pip install -r requirements.txt`

Environment Variables (MySQL)
-----------------------------
Set these before running:
- DB_NAME (e.g., littlelemon)
- DB_USER (e.g., root)
- DB_PASSWORD
- DB_HOST (default 127.0.0.1)
- DB_PORT (default 3306)

Quick Start
-----------
1) Install dependencies:
   pip install -r requirements.txt

2) Export env vars (example on macOS/Linux):
   export DB_NAME=littlelemon
   export DB_USER=root
   export DB_PASSWORD=yourpassword
   export DB_HOST=127.0.0.1
   export DB_PORT=3306

   (On Windows PowerShell):
   setx DB_NAME littlelemon
   setx DB_USER root
   setx DB_PASSWORD yourpassword
   setx DB_HOST 127.0.0.1
   setx DB_PORT 3306

3) Run migrations and create token tables:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

4) Run the dev server:
   python manage.py runserver

Static HTML Check
-----------------
Visit http://127.0.0.1:8000/ to see a static page served by Django.

API Paths for Peer Testing
--------------------------
/api/menu/
/api/bookings/        (Token required for POST/PUT/PATCH/DELETE)
/api/registration/
/api/api-token-auth/

Auth Flow
---------
1) POST /api/registration/ with { "username": "...", "password": "..." }
2) POST /api/api-token-auth/ with form-data or JSON:
   { "username": "...", "password": "..." }
3) Use the returned token for protected endpoints:
   Authorization: Token <your-token>

Run Unit Tests
--------------
python manage.py test

Notes
-----
- DB settings are placeholders via environment variables (safer for peer review).
- If mysqlclient fails to install on your OS, ensure you have MySQL dev headers.
  On macOS: `brew install mysql-client` (then set necessary flags).
  On Windows: Consider using precompiled wheels or WSL.