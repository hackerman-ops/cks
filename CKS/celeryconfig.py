broker_url = 'redis://:@127.0.0.1:6379/3'  # 指定 Broker
# result_backend = 'redis://127.0.0.1:6379/1'# 指定 Backend
timezone = 'Asia/Shanghai'  # 指定时区，默认是 UTC
task_serializer = 'pickle'
result_serializer = 'pickle'
accept_content = ['pickle', 'json']
task_ignore_result = True
# timezone='UTC'
imports = (
    # 指定导入的任务模块
    'kube_worker.tasks'
)

# celery 的启动工作数量设置
CELERY_WORKER_CONCURRENCY = 1
# 任务预取功能，会尽量多拿 n 个，以保证获取的通讯成本可以压缩。
worker_prefetch_multiplier = 1
# 有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True
# celery 的 worker 执行多少个任务后进行重启操作
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
# 禁用所有速度限制，如果网络资源有限，不建议开足马力。
worker_disable_rate_limits = True

# celery beat配置（周期性任务设置）
CELERY_enable_utc = False

DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
C_FORCE_ROOT = True