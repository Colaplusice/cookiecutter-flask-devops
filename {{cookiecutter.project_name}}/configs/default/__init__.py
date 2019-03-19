import os
{%- if cookiecutter._is_test_env == "n" %}
import raven
{%- endif %}
from .peewee import *  # noqa


DEBUG = True

PROJECT_NAME = "{{cookiecutter.project_name}}"
TZ = "Asia/Shanghai"

SENTRY_TAGS = {"project": PROJECT_NAME}
SENTRY_ENVIRONMENT = os.environ.get("FLASK_ENV", "development")

{%- if cookiecutter._is_test_env == "n" %}
SENTRY_RELEASE = raven.fetch_git_sha(
    os.path.abspath(os.path.join(__file__, "../../../"))
)
{%- else %}
SENTRY_RELEASE = None
{%- endif %}
