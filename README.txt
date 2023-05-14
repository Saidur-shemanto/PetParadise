
At first, you have to create virtual environment for this project
by entering the following command,

python -m venv venv

Then, you have to activate your venv by entering the following command,

venv/Scripts/activate

If it requires permission, enter the following command,
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then select the interpreter from

 view->command palette -> python: select interpreter -> recommended one

Then install the reequirements by entering the following command,

pip install -r requirements.txt


Now you have to create a database named 'petparadise'. 
If you already have a same named databse, then drop that by entering the following command,

drop database petparadise;

Now, Go to settings.py and change the database informations according to your device.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'petparadise',
        'HOST': 'localhost',
        'USER': 'Your user name',
        'PASSWORD': 'Your Password', 
    }
}


Now run the following commands, 

python manage.py makemigrations 
python manage.py migrate

Now run the following command,

python manage.py runserver

you are good to go.