from configs.default import *  # noqa

TESTING = True

DB_NAME = "{{cookiecutter.project_name}}_test"
PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{db_name}".format(
    host=DB_HOST, db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD  # noqa
)

CELERY_TASK_ALWAYS_EAGER = True
