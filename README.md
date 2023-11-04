# Oriana IOT Project

This repo is the iot project. 

We are using django, vue2 and webpack for assets.


# installation 

1.  clone this repository:
        git clone https://github.com/andresmauro17/oriana-web.git

2.  Create enviroment variables, in your .env file. maybe a bash files as show:

.env_example
       

## With Docker
2.  install docker
        docker-compose build

3.  run docker
        docker-compose up


## Without Docker

2.  start a python virtual enviroment
        python -m venv .venv

3.  active virtualenv 
        source .venv/bin/activate

4.  install python dependencis
        pip install -r requirements/local.txt

5. create a superuser
        python manage.py createsuperuser

6. run the project
        python manage.py runserver

# some commands 

## production
1. Create a super user
        docker-compose run --rm django python manage.py createsuperuser

2. Building assets to production
        docker-compose run --rm node npm run build

3. Collect statics 
        docker-compose run --rm django python manage.py collectstatic

4. run logs in production
        - docker-compose exec django /bin/sh
        - tail -f /var/log/django.log

## Emqx stuffs
1. create rules in emqx using api from django
        docker-compose run --rm django python manage.py createemqxrules

{
  "agent": {
    "sensorid":"fffff00011",
    "typeofmessage":"storedata",
    "data":{
      "value":32,
      "energy":1,
      "date":"23-03-29",
      "time":"03:24"
    }
  }
}

2. run emqx 
        sudo docker-compose -f docker-compose.yml up