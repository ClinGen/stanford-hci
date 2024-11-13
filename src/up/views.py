"""This module defines the views for the up app.

The up app is used to check the status of the application and its databases.
"""

from django.conf import settings
from django.db import connection
from django.http import HttpResponse
from redis import Redis

redis = Redis.from_url(settings.REDIS_URL)


def index(request):
    return HttpResponse("")


def databases(request):
    redis.ping()
    connection.ensure_connection()

    return HttpResponse("")
