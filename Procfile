web: gunicorn config.wsgi:application
worker: celery worker --app=deven.taskapp --loglevel=info
