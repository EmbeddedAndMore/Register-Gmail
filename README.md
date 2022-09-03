source env/bin/activate
pip install -r requirements.txt
cd First
./manage.py createsuperuser
./manage.py runserver
