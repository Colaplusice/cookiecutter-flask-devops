from configs.default import *  # noqa

CACHE_HOST = "cache-redis.rds"

CELERY_BROKER_URL = "amqp://celery:celery@rabbitmq.service.sbay:5672/shanbay"

DB_HOST = "db-mysql.rds"
PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{db_name}".format(
    host=DB_HOST, db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD  # noqa
)
