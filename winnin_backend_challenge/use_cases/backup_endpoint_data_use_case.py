import requests
from datetime import datetime
import pytz

from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from request_response import Response
from repository import UserRepo, PostRepo
from domain import Post, User

class BackupEndpointDataUseCase():
    """ Use case for adding to the database de post data obtained from the reddit endpoint """
    def __init__(self):
        self.user_repo = UserRepo()
        self.post_repo = PostRepo()
        
    def execute(self, request):
        response = Response()
        try:
            for post in [p['data'] for p in request.endpoint_data['data']['children']]:
                user_id = self.user_repo.add_user(User(name = post['author'], ups = post['ups'], comments = post['num_comments']))
                created_time = datetime.fromtimestamp(post['created_utc'], tz = pytz.timezone(request.timezone))
                self.post_repo.add_post(Post(title = post['title'], ups = post['ups'], comments = post['num_comments'], created = created_time, author = user_id))
            return response

        except Exception as e:
            response.add_exception_error(e)
            return response