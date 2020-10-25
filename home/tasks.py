import time

from celery import shared_task

from .models import Number


@shared_task
def adding(x, y, id):
    time.sleep(10)
    num = Number.objects.get(id=id)
    num.result = x + y
    num.save()
    return num.result
