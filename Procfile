release: python manage.py makemigtations --no-input
release: python manage.py migrate --no-input

web: gunicorn posts.wsgi --log-file -