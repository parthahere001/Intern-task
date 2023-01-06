# Intern-task
A repo for internship assignment submission

## Getting Started

Just clone the repo onto your local machine and the follow the following steps (For Linux)

Open the Settings.py file (present in assignmentapp/assignmentapp/)
find the following section :-
```
DATABASES = {
        'default': {
        'ENGINE': 'djongo',
        'NAME': '<DB-Name>',
        'HOST': 'mongodb+srv://<DB Username>:<Db password>@....mongodb.net/test?retryWrites=true',
        'USER': '<db username>',
        'PASSWORD': '<db-username>',
    }
}
```
Here replace *DB-name* with your desired Database name, *DB username* with the username for your MongoDB database and *DB password* with the password for your MongoDb database

Start up Mongod

Navigate to the project directory, open the terminal in this directory and run the following command :
```
source bin/activate
cd assignmentapp/
python3 manage.py createsuperuser
```
Enter the details to create an Admin account
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
open the server link, before signing-in or registering visit http://127.0.0.1:8000/admin/ to log-in into the admin dashboard and add some data into the Products Section.

Finally open http://127.0.0.1:8000/ and use (Remember that when registering choose a password that is atlease 8 letters long and has some combination of letters - small and captal, numbers and special characters).

### Prerequisites

Make sure to have Python (version 3.0.0 or onwards) and Virtual env set up on your local device.
To view the data being saved to the MongoDB database use MongoDB Compass
