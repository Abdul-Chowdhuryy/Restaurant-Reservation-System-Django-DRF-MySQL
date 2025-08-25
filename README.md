🍋 Little Lemon Restaurant Reservation System

A full-stack backend project built with Django, Django REST Framework (DRF), and MySQL.
This system allows customers to browse the menu, book tables, and register accounts, while enabling staff to manage bookings and menu items.

Developed as part of the Meta Back-End Developer Capstone, this project highlights practical skills in API design, authentication, database integration, and testing.

✨ Features

🖼️ Static Content – Landing page served with Django templates

📋 Menu API – Endpoints to create, list, update, and delete dishes

🍽️ Table Booking API – Endpoints for customers to reserve tables

🔐 User Authentication – Registration & login via token-based authentication

🗄️ Database Integration – MySQL-powered persistent data storage

🧪 Unit Testing – Automated tests for core API functionality

🌐 API Testing – Fully compatible with Insomnia and Postman

🛠️ Tech Stack

Framework: Django, Django REST Framework

Database: MySQL

Authentication: DRF Token Authentication

Testing: Django Unit Tests & DRF APIClient

Frontend: Django Templates (for static content)

🚀 Installation & Setup

Clone the repository

git clone https://github.com/your-username/littlelemon-drf-mysql.git
cd littlelemon-drf-mysql


Install dependencies

pip install -r requirements.txt


Configure MySQL in .env or settings.py:

DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306


Apply migrations

python manage.py migrate


Run the server

python manage.py runserver

📡 API Endpoints

📋 Menu API

GET /api/menu/ – List all menu items

POST /api/menu/ – Add a new dish

🍽️ Booking API

GET /api/bookings/ – View all bookings

POST /api/bookings/ – Create a booking (requires token)

👤 User Auth

POST /api/registration/ – Register a new account

POST /api/api-token-auth/ – Get an authentication token

✅ Testing

Run automated tests with:

python manage.py test

🌟 Project Value

This project demonstrates the ability to:

Build secure, production-ready APIs

Integrate Django with a relational database (MySQL)

Implement authentication and permissions

Write unit tests for reliability

Deploy professional documentation for peers and recruiters

📌 Author

👨‍💻 Developed by Abdul Chowdhury as part of the Meta Back-End Developer Capstone Project.

⚡ This repo is ready for both academic submission and as a portfolio piece to showcase backend engineering skills.
