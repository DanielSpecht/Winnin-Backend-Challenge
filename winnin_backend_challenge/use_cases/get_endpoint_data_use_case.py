import requests
from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from request_response import Response

class GetEndpointDataUseCase():
    """ Use case for obtaining the hot post data from the reddit endpoint """
    def execute(self, request):
        response = Response()
        try:
            data_json = requests.get(request.endpoint, headers = {'User-agent': 'winnin backend'}).json()
            response.data = data_json
            return response
        except Exception as e:
            response.add_exception_error(e)
            return response
            