# Description

This project is to build and deploy a REST API with Django and Docker.  
The base docker image is ubuntu:20.04.  
Django backend DB is oracle18c.  
The web server is using apache2.  

# Dev Build Image
```
docker-compose build
```

# Migrate Basic Tables
```
docker-compose run mic_api sh -c "python /var/www/micApiApp/manage.py migrate"
```
It will create the following tables:  
DJANGO_ADMIN_LOG  
DJANGO_CONTENT_TYPE  
DJANGO_MIGRATIONS  
DJANGO_SESSION  
AUTH_GROUP  
AUTH_GROUP_PERMISSIONS  
AUTH_PERMISSION  
AUTH_USER  
AUTH_USER_GROUPS  
AUTH_USER_USER_PERMISSIONS  

# Create Admin User
```
docker-compose run mic_api sh -c "python /var/www/micApiApp/manage.py createsuperuser"
```

# Dev Run Image
```
docker-compose up mic_api
```
This command will run the service mic_api as a container  
It maps localhost port 8080 to container port 80  
The folder ./src will be mount to container /var/www/micApiApp  
When the container is running, any subsequent changes in ./src will trigger reloading  
The service mic_api is hosted on the build-in developer server  

```
docker-compose up apache2
```
This command will run the service mic_api as a container    
It maps localhost port 8090 to container port 80    
The folder ./src will be mount to container /var/www/micApiApp  
The service mic_api is hosted on the apache2 server  