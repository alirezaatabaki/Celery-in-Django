import time

from celery import shared_task
from django.core.mail import EmailMessage

from .models import Number


@shared_task
def adding(x, y, id):
    time.sleep(10)
    num = Number.objects.get(id=id)
    num.result = x + y
    num.save()
    return num.result


@shared_task
def sending_email():
    message = 'this emai send by celery'
    mail_subject = 'فراموشی رمز عبور'
    to_email = 'alirezaatabaki@icloud.com'
    email = EmailMessage(
        subject=mail_subject, body=message, to=[to_email]
    )
    email.send()
    # use command below to start your task in one terminal and start your worker on other terminal
    # celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
