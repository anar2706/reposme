release: python manage.py migrate
web: gunicorn blood_bank_project.wsgi
worker: celery -A blood_bank_project worker -D