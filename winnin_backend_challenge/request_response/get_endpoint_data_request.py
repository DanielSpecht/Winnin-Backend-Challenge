import requests
from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from request_response import Response

class GetEndpointDataRequest():
    def __init__(self, endpoint):
        """
        Args:
            endpoint (str): The subreddit endpoint for hot posts
        """
        self._endpoint = endpoint
    
    @property
    def endpoint(self):
        return self._endpoint