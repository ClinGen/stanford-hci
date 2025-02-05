"""This module sets up custom middleware."""

# pylint: skip-file
# TODO(Liam): Don't skip lint in this module.

# TODO(Liam): Don't use deprecated `MiddlewareMixin`.
# https://docs.djangoproject.com/en/5.1/topics/http/middleware/#writing-your-own-middleware

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HealthCheckMiddleware(MiddlewareMixin):
    """This is the health check that we use in AWS to make sure the HCI is still alive
    and well."""

    def process_request(self, request):
        if request.META["PATH_INFO"] == "/ping/":
            return HttpResponse("pong")
