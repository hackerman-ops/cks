from CKS import celery_app
from celery_app.kubernetes_job_api import create_job


@celery_app.task
def create_cron_job(*args, **kwargs):
    create_job(*args, **kwargs)
