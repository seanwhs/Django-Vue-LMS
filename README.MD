# 🎓 Django + Vue Learning Management System (LMS)

A full-stack Learning Management System built with **Django (DRF)** and **Vue.js**, following a YouTube tutorial series and enhanced with additional custom modifications.

This project demonstrates a modern **decoupled architecture**:

* 🔙 Backend API powered by Django REST Framework
* 🔜 Frontend SPA built with Vue
* 🔐 Token-based authentication
* 📚 Course management system

---

## 🙏 Acknowledgement & Credit

This project was built by following the YouTube playlist:

🎥 **Django + Vue LMS Tutorial Series**
[https://www.youtube.com/playlist?list=PLpyspNLjzwBk3oofmtqs0KMD3DY9BjNwp](https://www.youtube.com/playlist?list=PLpyspNLjzwBk3oofmtqs0KMD3DY9BjNwp)

Full credit goes to the original creator of the tutorial for the structured walkthrough and foundational implementation.

While following the series, I made several refinements and adjustments to better understand the architecture and improve parts of the implementation.

---

## 🏗 Architecture Overview

```
Django (API)  <----JSON---->  Vue Frontend
```

### Backend

* Python
* Django
* Django REST Framework
* SQLite (default, configurable)

### Frontend

* Vue.js
* Vue Router
* Vuex (State Management)
* Axios (API communication)
* Bulma (Styling)

---

## 🚀 Features

### 🔐 Authentication

* User registration
* Login / Logout
* Token-based authentication
* Persistent login using local storage

### 📚 Course Management

* List all courses
* View course details
* Categories
* Course content rendering

### 🧠 LMS Capabilities

* Modular Django apps (`core`, `course`)
* RESTful API endpoints
* Decoupled frontend & backend
* State-managed frontend authentication

---

## 📂 Project Structure

```
Django-Vue-LMS/
│
├── core/              # Core Django app (auth, base config)
├── course/            # Course-related models and APIs
├── frontend/          # Vue.js application
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/seanwhs/Django-Vue-LMS.git
cd Django-Vue-LMS
```

---

## 🐍 Backend Setup (Django)

### Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Run Backend Server

```bash
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000/
```

---

## 🌐 Frontend Setup (Vue)

Navigate into frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run serve
```

Frontend runs at:

```
http://localhost:8080/
```

---

## 🔄 API Endpoints (Sample)

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| GET    | /api/v1/courses/      | List all courses  |
| GET    | /api/v1/courses/<id>/ | Course detail     |
| POST   | /api/v1/token/login/  | User login        |
| POST   | /api/v1/users/        | User registration |

---

## 🧩 Custom Modifications

While following the tutorial series, I implemented additional improvements:

* Refactored some API logic
* Adjusted authentication handling in Vuex
* Improved Axios error handling
* Minor UI refinements
* Cleaned up project structure

---

## 🛠 Development Notes

* Backend and frontend are completely decoupled.
* Authentication uses token-based strategy.
* Axios interceptors handle authentication headers.
* Vuex maintains global authentication state.

---

## 📌 Learning Objectives

This project helped me deepen my understanding of:

* Django REST Framework
* Vue.js state management
* API integration patterns
* Token authentication flows
* Full-stack application architecture

---

## 🔮 Future Improvements

* Role-based permissions (Instructor / Student)
* Course enrollment system
* Progress tracking
* Payment integration
* Deployment to cloud (GCP / Render / Railway)
* Dockerization

---

## 👨‍💻 Author

Sean Wong

Built as part of hands-on learning and full-stack experimentation.

