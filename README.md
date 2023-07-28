Event management System

Project name: Event management system 
Framework: Django
Backend: Python 
Frontend: HTML, CSS, JAVA SCRIPT 
Database: sqlite3

Project Structure:
-event_management/
|-- manage.py
|-- eventmanagement/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- ecommerce/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   |-- templates/
|   |   |   |-- index.html
|   |   |   |-- aboutus.html
|   |   |   |-- login.html
|   |   |   |-- contact.html
|   |-- static/
|   |   |-- css/
|    |   |--icon/
|    |   |--front/
|   |   |-- js/
|   |   |-- images/

Here's an explanation of the main directories and files:
•	manage.py: Django's command-line utility for administrative tasks.
•	eventmanagement: The project's main settings and configuration folder.
•	settings.py: Main project settings.
•	ecommerce: An app that handles user authentication and profiles.
•	models.py: Define the database models for user profiles.
•	views.py: Contains the views/logic for user authentication and profiles.
•	urls.py: URL configuration for the accounts app.
•	forms.py: Define custom forms for user authentication and profile views.
•	templates/: Directory to store HTML templates related to accounts.
•	static/: Directory to store static files (CSS, JS, images) for accounts.
•	templates/: Directory to store base templates (like the base HTML template), and templates for generic pages like home, about, contact, etc.
•	static/: Directory to store the project's static files like CSS, JS, and images.
•	media/: Directory to store user-uploaded files like event images.
•	requirements.txt: A list of project dependencies.

How to run the application locally
1.	Install Django and Other Dependencies:
•	Make sure you have Python installed on your system. You can download Python from the official website (https://www.python.org/downloads/).
•	After installing Python, open a terminal or command prompt and install virtual environment and Django using pip (Python package manager):
	py -m venv (flodername)
eg: py -m venv evn
(once complete installing VE, activate the VE)
	pip install Django
Note: virtual environment and Django install incase if it not works in your system but don’t forget to delete virtual environment already exit in the application.
2.	Navigate to the Project Directory:
•	Change your working directory to the root directory of your Django project.
3.	Start the Development Server:
•	To run the Django application locally, start the development server using the following command:
	python manage.py runserver
•	You should see output indicating that the development server is running. By default, it will be available at http://127.0.0.1:8000/ (or http://localhost:8000/).
4.	Access the Application:
•	Open your web browser and navigate to http://127.0.0.1:8000/ (or http://localhost:8000/) to access your Django application locally.


Functionality:
1.	Registration for events 
2.	View latest event 
3.	View previous event 
4.	Contact (customer can also contact through contact form)
5.	Admin login 

Admin login credential:
Username: sangay
Password: sangay

•	In the admin dashboard, admin can fully control the customers and comments details by deleting, updating and adding new customer.  



 



