
import logging
import json

logging.getLogger().setLevel(logging.INFO)

class LoggingMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request):
        print('invoked')
        logging.info(f"Incoming request: {request.method} {request.path} {json.dumps(request.body.decode('utf-8'), indent=4)}")
        logging.info(json.dumps(request.body.decode('utf-8'), indent=4))
        response = self.get_response(request)
        logging.info(f"Outgoing response: {response.status_code}")
        return response