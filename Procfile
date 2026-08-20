release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn birthday_site.wsgi --bind 0.0.0.0:$PORT --log-file -