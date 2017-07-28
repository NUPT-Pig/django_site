from django.utils import deprecation


class TestMiddleware(deprecation.MiddlewareMixin):  # must inherited from deprecation.MiddlewareMixin since django 1.10

    def process_request(self, requset):
        return None

    def process_response(self, request, response):
        return response