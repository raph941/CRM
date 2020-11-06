# CRM
this is a crime and criminal record management system, it is a personal project, built for law enforcement agencies especially here in Nigeria in ordwe to automate the existing manual process of storing crime and criminal records.

![CriminalApp Image](https://res.cloudinary.com/raph941/image/upload/v1604642174/Github%20/CRM/slide1_vcpauy.png)
![CriminalApp Image](https://res.cloudinary.com/raph941/image/upload/v1604642174/Github%20/CRM/slide3_a16i7p.png)


# Live: 
    the app is hosted on "http://criminalrecord.herokuapp.com"
    you can login as admin: username: admin1234, password:adminaccountpass,
    as regularuser: username:user12345, password:nigerians


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
python 3.6.0 
django 2.1

## installing
    you can simply download a copy of the project at https://github.com/raph941/CRM

## Create virtual environment
    pip install virtualenv 

## activate virtual environment
    venv\Scripts\activate.bat

### install requirement files: 
    pip install -r requirements.txt

### make migrations
    python manage.py makemigrations

## migrate
    python manage.py migrate

## create super user
    python manage.py createsuperuser

## Run
    to run, 
    on your command line in the project directory,
    python manage.py runserver
    on your web browser goto

    http://127.0.0.1:8000/home 



