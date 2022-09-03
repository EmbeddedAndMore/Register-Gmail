source env/bin/activate
pip install -r requirements.txt
cd LoginGmail
./manage.py createsuperuser
./manage.py runserver

