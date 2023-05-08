
At first, you have to create virtual environment for this project
by entering the following command

python -m venv venv


if it requires permission
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then, you have to activate your venv
venv/Scripts/activate

then select the interpreter from\
 view->command palette -> python: select interpreter -> recommended one

then install the reequirements
pip install -r requirements.txt


Now you have to create a database named petparadise
if you already have a same named databse, then drop that

Now, Go to settings.py and change the database informations according to your device.


Now run the following commands 

python manage.py makemigrations 
python manage.py migrate

now run
python manage.py runserver

you are good to go.