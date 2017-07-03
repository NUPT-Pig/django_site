class TestMiddleware(object):

    def process_request(self, requset):
        return None

    def process_response(self, request, response):
        return response