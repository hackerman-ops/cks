from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings
from django.utils import timezone

# set the default Django settings module for the 'celery' program.
# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CKS.settings')

# 创建celery app
app = Celery('CKS')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# 从单独的配置模块中加载配置
app.config_from_object('CKS.celeryconfig')
# 设置app自动加载任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# 解决时区问题,定时任务启动就循环输出
app.now = timezone.now
