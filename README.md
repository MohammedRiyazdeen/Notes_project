# 📝 CloudNotes (Django)

[![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0+-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Deployment](https://img.shields.io/badge/Render-Deployed-orange?logo=render&logoColor=white)](https://render.com/)

A professional, secure, and responsive **Notes Management Application** built with Django. This project demonstrates core backend engineering principles including user authentication, CRUD operations, PostgreSQL integration, and production-ready deployment workflows.

---

## 🔗 Project Links

- **Live Demo**: [https://notes-project-tj95.onrender.com](https://notes-project-tj95.onrender.com)
- **GitHub Repository**: [https://github.com/MohammedRiyazdeen/Notes_project](https://github.com/MohammedRiyazdeen/Notes_project)

---

## 🚀 Key Features

*   **Secure Authentication**: Full login/signup system with password hashing and session management.
*   **Persistent Storage**: Integrated with **PostgreSQL** for reliable data management in production.
*   **User Isolation**: Middleware and query filtering ensure users only see and manage their own notes.
*   **Search & Discovery**: Real-time filtering for efficient note searching.
*   **Responsive UI**: Mobile-first design using **Bootstrap 5** with clean "Empty States."
*   **Production Optimized**: Configured with WhiteNoise for static assets and Gunicorn as the WSGI server.

---

## 🛠️ Internal Tech Stack

*   **Backend**: Python, Django
*   **Database**: PostgreSQL (Production), SQLite (Development)
*   **Frontend**: HTML5, Vanilla CSS, Bootstrap 5
*   **Middleware**: WhiteNoise (Static file serving)
*   **WSGI Server**: Gunicorn
*   **Environment Management**: `python-dotenv` for secret management

---

## 🧠 Core Concepts Demonstrated

- **CRUD Architecture**: Implementing Create, Read, Update, and Delete operations.
- **Data Security**: Protecting user-specific data from being accessed by other logged-in users.
- **Environment Parity**: Managing different settings for Local vs. Production environments.
- **Cloud Deployment**: Automating deployment via GitHub integration on Render.

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

Built by **Mohammed Riyazdeen** as a professional portfolio project. Focus on Django backend architecture and scalable cloud deployment.
