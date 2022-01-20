import json
import os
import sys

import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oak.settings')
dd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dd)
import django

django.setup()


from app.tasks import task_test

task_test.delay("assdfa")

