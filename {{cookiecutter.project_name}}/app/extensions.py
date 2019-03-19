from raven.contrib.flask import Sentry

from coast.celery import Celery
from peeweext.flask import Peeweext


pwx = Peeweext()
sentry = Sentry()
celeryapp = Celery()
