# simpleAppDjango
This application is implemented in djano, it has only three functionnalities, login, logout and show user profile  with the ability to change the email address

##Folow these instructions to run the application

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

#create a superuser or use "admin, pwd: admin)
python manage.py createsuperuser 

# run the server
python manage.py runserver

#go to the browser
http://127.0.0.1:8000/admin/login/?next=/admin/

#create new users or use "user , pwd : user1234

#go to http://127.0.0.1:8000/accounts/login/
