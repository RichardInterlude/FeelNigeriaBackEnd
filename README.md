# 🇳🇬 Feel Nigeria Initiative

A web application built with **Django** and **Python** for the *Feel Nigeria Initiative* project.  
This backend provides a foundation for managing content, users, and communications related to the initiative.

---

## 🚀 Tech Stack
- **Backend:** Django (Python)
- **Environment:** Virtualenv
- **Environment Management:** python-dotenv

---

## ⚙️ Setup & Installation

Follow these steps to set up and run the project locally.

### 1 Clone the Repository
``` bash
git clone https://github.com/yourusername/feel-nigeria-initiative.git
cd feel-nigeria-initiative
```

### 2 Create your virtual environment
``` bash
python -m venv venv
venv\Scripts\activate --> This is to activate your virtual environment
```

### 3 Install Dependecies
``` bash
pip install -r requirements.txt
```

### 4 Create your .env file
Create a .env file in your project folder and out this into it

DJANGO_SECRET_KEY=your_secret_key_here
EMAIL_HOST_USER=your_email_here
EMAIL_HOST_PASSWORD=your_email_password_here

### 5 Running the Application
``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

