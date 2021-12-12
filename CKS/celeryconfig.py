BROKER_URL = 'redis://:@127.0.0.1:6379/3'  # 指定 Broker
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'# 指定 Backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_IGNORE_RESULT = True
# CELERY_TIMEZONE='UTC'
CELERY_IMPORTS = (
    # 指定导入的任务模块
    'celery_app.tasks'
)

# celery 的启动工作数量设置
CELERY_WORKER_CONCURRENCY = 10
# 任务预取功能，会尽量多拿 n 个，以保证获取的通讯成本可以压缩。
CELERYD_PREFETCH_MULTIPLIER = 20
# 有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True
# celery 的 worker 执行多少个任务后进行重启操作
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
# 禁用所有速度限制，如果网络资源有限，不建议开足马力。
CELERY_DISABLE_RATE_LIMITS = True

# celery beat配置（周期性任务设置）
CELERY_ENABLE_UTC = False

DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'