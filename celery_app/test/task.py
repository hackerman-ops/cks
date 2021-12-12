import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CKS.settings')
import django

django.setup()
from django_celery_beat.models import PeriodicTask, IntervalSchedule

import json


def my_task(string):
    schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)

    PeriodicTask.objects.create(
        interval=schedule,
        name='add device %s' % string,
        task='celery_app.task.test_func',
        args=json.dumps([string])
    )


if __name__ == "__main__":
    my_task("asdasdsad")
