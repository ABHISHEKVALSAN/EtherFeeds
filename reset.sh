rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
cd etherfeeds
python3 deployContract
cd ..
