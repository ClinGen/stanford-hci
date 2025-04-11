"""Set up custom middleware."""

# pylint: skip-file
# TODO(Liam): Don't skip lint in this module.

# TODO(Liam): Don't use deprecated `MiddlewareMixin`.
# https://docs.djangoproject.com/en/5.1/topics/http/middleware/#writing-your-own-middleware

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HealthCheckMiddleware(MiddlewareMixin):
    """Establish a health check endpoint.

    We can use this to monitor the status of the application.
    """

    def process_request(self, request):
        """Process the HTTP request."""
        if request.META["PATH_INFO"] == "/ping/":
            return HttpResponse("pong")
