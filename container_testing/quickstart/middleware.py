
import logging
import json

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class LoggingMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request):
        print('invoked')
        logging.info(f"Incoming request: {request.method} {request.path} \n{json.dumps(json.loads(request.body), indent=4)}")
        response = self.get_response(request)
        logging.info(f"Outgoing response: {response.status_code}")
        return response