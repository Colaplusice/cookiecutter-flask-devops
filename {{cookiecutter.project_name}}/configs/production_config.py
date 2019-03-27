from configs.base_config import Config


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = "mysql://root:newpass@mysql/{{cookiecutter.project_name}}"
    CELERY_RESULT_BACKEND = "redis://redis:6379/1"
    BROKER_URL = "redis://redis:6379/1"
    DB_HOST = "mysql"
    REDIS_HOST = "redis"
    CACHE_HOST = "redis"
