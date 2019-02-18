from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from repository import UserRepo, PostRepo
from request_response import Response

class ListUsersUseCase(object):
    """ Use case for listing the users """
    def __init__(self):
        self.user_repo = UserRepo()

    def execute(self, request_object):
        response = Response()
        try:            
            users = self.user_repo.list_users(request_object.order)
            response.data = users
            return response
            
        except Exception as e:
            response.add_exception_error(e)
            return response
            
