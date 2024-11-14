"""This module provides the Celery config. (It comes from django-docker-
example.)

Celery is a distributed task queue. It is a great tool for running long tasks
in the background or at scheduled times.
"""

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("hci")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
