# Heatwaves Alert System
This application assists in sending SMS messages to warn subscribers about potential heat waves in their location. Application deploys machine learning model that predict temperatures from weather data scraped using weather APIs. When predicted temperature crosses 37 degree Celcius, an SMS message is sent to users using Twilio.

![image](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/5ecab6cd-87ac-4704-9179-28a8d422c528)

## Techstack Used
This application was developed using Python Django and deployed using Docker. Randomforest (ensemble) classifier is deployed in the application.

## How to setup project

1. Create a project folder "heatwavealert" and add the code for ML model. Inside the project directory, create a django project using the following commands in sequence: ```pip install django```, ```django-admin startproject myproject```, ```cd myproject```, ```python manage.py startapp myapp```.
   
Your directory structure should resemble:

heatwave_alert/

&emsp;|--manage.py

&emsp;|--heatwave_alert/

&emsp;&emsp;|-- __init__.py
       
&emsp;&emsp;|--settings.py
        
&emsp;&emsp;|--urls.py
        
&emsp;&emsp;|--wsgi.py
        
&emsp;|--alert/
  
&emsp;&emsp; |--__init__.py
       
&emsp;&emsp; |--admin.py
       
&emsp;&emsp;|--apps.py
        
&emsp;&emsp;|--migrations/
        
&emsp;&emsp;|--models.py
        
&emsp;&emsp;|--tests.py
        
&emsp;&emsp;|--views.py

2. Add a urls.py file to alert/ and copy its code into it.
3. Paste other codes in their respective files as well.
4. Signup for Twilio and create an account. Get your twilio credentials (Authorization token, phone number, SID) and try sending a sample SMS to a phone number from Twilio.
5. Fill in appropriate credential details in views.py.
6. Run the server using ```python manage.py makemigrations``` and ```python manage.py migrate```.
7. Open your web browser and go to http://127.0.0.1:8000/admin
8. Create superuser account using terminal command ```python3 manage.py createsuperuser```
9. Add subscribers along with the details of their phone numbers and location (name, latitude, longitude)
11. Send trigger alerts to the subscribers for checking your functionality.
12. To deploy application in docker, initialise and setup Docker desktop. Check if the server is running. Install docker-compose through terminal. Then, login to Docker from terminal.
13. Dockerise your application by creating a Dockerfile and add a docker-compose.yml and requirements.txt file in the root directory of your project "heatwave_alert". Use the commands ```docker-compose build``` and  ```docker-compose up```. Visit http://127.0.0.1:8000/ to check your frontend.

Directory structure:

![Screenshot 2024-06-17 at 4 27 24 PM](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/9b13003a-b828-43a2-bb71-269425f185db)

Commands:

![Screenshot 2024-06-14 at 12 52 58 AM](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/e1ecd9fa-f16e-4e66-8929-a15791d833af)

Django Admin Page:

![Screenshot 2024-06-16 at 10 24 24 PM](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/1e9f001f-e489-4f40-a68e-4c20392742b0)

Django Logs:

![image](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/4c8bb5b5-0e69-48b7-9659-3208c8299e8a)


Deployment in Docker:

![Screenshot 2024-06-17 at 5 02 40 PM](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/19bace35-a545-45df-9429-e66d6dcb4fdd)
![image](https://github.com/SwethaatGH/heatwavealertsystem/assets/98175379/21e6f05c-84b3-4a9d-96b3-9f555e27340a)


