Step 1
create virtual enviroment 

windows Os 
>>>pip install virtualenv

>>>virtualenv env 

activate enviroment
>>>env\scripts\activate
or
>>>python -m venv env

Linux
>>>pip3 install virtualenv

>>>virtualenv env 

activate enviroment
>>>source env/bin/activate



#=========================================================
Step 2

install dependencies

>>>pip install django

#=========================================================
Step 3

windows
>>>python manage.py makemigrations

Linux 
>>>python3 manage.py makemigrations


#=========================================================
Step 4

windows
>>>python manage.py migrate

Linux 
>>>python3 manage.py migrate


#=========================================================
Step 5

create super user

windows
>>>python manage.py createsuperuser

Linux 
>>>python3 manage.py createsuperuser


#=========================================================
Step 6

run the server

windows
>>>python manage.py runserver

Linux 
>>>python3 manage.py runserver





