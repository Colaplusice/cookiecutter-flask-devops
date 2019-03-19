from kombu import Exchange

CELERY_BROKER_URL = "redis://redis:6379/1"
# CELERY_BROKER_URL = 'amqp://celery:celery@rabbitmq.service.sbay:5672/shanbay'

CELERY_TASK_DEFAULT_EXCHANGE = "default-exchange"
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_TASK_DEFAULT_ROUTING_KEY = "{{cookiecutter.project_name}}.default"
CELERY_TASK_DEFAULT_QUEUE = "{{cookiecutter.project_name}}.default"

CELERY_TASK_SOFT_TIME_LIMIT = 300

default_exchange = Exchange(
    CELERY_TASK_DEFAULT_EXCHANGE, type=CELERY_TASK_DEFAULT_EXCHANGE_TYPE
)

CELERY_IMPORTS = ["app.tasks"]

CELERY_BEAT_SCHEDULE = {}
