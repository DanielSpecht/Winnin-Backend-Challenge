from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from repository import PostRepo
from request_response import Response

class ListPostsUseCase(object):
    """ Use case for listing the posts """
    def __init__(self):
        self.post_repo = PostRepo()

    def execute(self, request_object):
        response = Response()
        try:
            posts = self.post_repo.list_posts(request_object.order, request_object.start, request_object.end)
            response.data = posts
            return response
            
        except Exception as e:
            response.add_exception_error(e)
            return response