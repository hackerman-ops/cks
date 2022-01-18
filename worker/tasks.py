from CKS import celery_app
from worker.kubernetes_job_api import create_job


@celery_app.task
def create_job_task(*args, **kwargs):
    create_job(*args, **kwargs)

@celery_app.task
def collect_interval_task():
    # Todo
    # 从redis中收集定时任务 写入数据库
    pass
