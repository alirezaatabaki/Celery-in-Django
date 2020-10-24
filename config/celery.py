import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

celery_app = Celery('config')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()
# find all tasks.py in whole project. you can change the name of file with "related_name"
