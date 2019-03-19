import os

workers = int(os.environ.get("WORKERS_NUM", 4))

bind = "0.0.0.0:5000"

worker_class = "sync"

timeout = 20

limit_request_line = 4096

limit_request_fields = 100

limit_request_field_size = 8190

graceful_timeout = 5

loglevel = "info"

if os.getenv("FLASK_ENV", "development") == "production":
    loglevel = "warning"

proc_name = "{{cookiecutter.project_name}}"
