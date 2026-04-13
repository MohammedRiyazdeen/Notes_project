# 📝 CloudNotes (Django)

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0+-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Deployment](https://img.shields.io/badge/Render-Deployed-orange?logo=render&logoColor=white)](https://render.com/)

A professional, secure, and responsive **Notes Management Application** built with Django. This project demonstrates core backend engineering principles including user authentication, CRUD operations, PostgreSQL integration, and production-ready deployment workflows.

---

## 🔗 Project Links

- **Live Demo**: [Click here to view the app](https://your-app-name.onrender.com) *(Update this after deployment!)*
- **GitHub Repository**: [MohammedRiyazdeen/Notes_project](https://github.com/MohammedRiyazdeen/Notes_project)

---

## 🚀 Key Features

*   **Secure Authentication**: Full login/signup system with password hashing and session management.
*   **Persistent Storage**: Integrated with **PostgreSQL** for reliable data management in production.
*   **User Isolation**: Middleware and query filtering ensure users only see and manage their own notes.
*   **Search & Discovery**: Real-time filtering using Django's `Q` objects for efficient note searching.
*   **Responsive UI**: Mobile-first design using **Bootstrap** with clean "Empty States" for better UX.
*   **Pagination**: Hand-optimized pagination for handling large volumes of notes smoothly.

---

## 🛠️ Internal Tech Stack

*   **Backend**: Python, Django
*   **Database**: PostgreSQL (Production), SQLite (Development)
*   **Frontend**: HTML5, Vanilla CSS, Bootstrap 5
*   **Middleware**: WhiteNoise (Static file serving)
*   **WSGI Server**: Gunicorn
*   **Environment Management**: `python-dotenv` for secret management

---

## ⚙️ How to Run Locally

1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/MohammedRiyazdeen/Notes_project.git
    cd Notes_project
    ```
2.  **Environment Setup**:
    Create a `.env` file based on `.env.example`:
    ```bash
    cp .env.example .env
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Database Initialisation**:
    ```bash
    python manage.py migrate
    ```
5.  **Run Development Server**:
    ```bash
    python manage.py runserver
    ```

---

## 📎 Author

Built by **A. Riyaz** as a portfolio project. Focus on Django backend architecture, database relationships, and production deployment.
