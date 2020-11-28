# Oriana IOT Project

This repo is the iot project. 

We are using django, vue2 and webpack for assets.


# installation 

1.  clone this repository:
        git clone https://github.com/andresmauro17/oriana-web.git

2.  Create enviroment variables, in your .env file. maybe a bash files as show:

.env_example
       
        
2.  start a python virtual enviroment
        virtualenv -p $(which python3) .venv
        
3.  active virtualenv 
        source .venv/bin/activate
        
4.  install python dependencis
        pip install -r requirements/local.txt

5. create a superuser
        python manage.py createsuperuser

6. run the project
        python manage.py runserver