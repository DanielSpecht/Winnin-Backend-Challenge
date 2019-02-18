from .base_repo import BaseRepo
from .table_mapping import DbUser

from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from domain import User

class UserRepo(BaseRepo):

    def add_user(self, user):
        """
        Persists a user to the database
        
        Args:
            user (User): The user to be persisted
        """
        try:        
            return DbUser.create(name = user.name, ups = user.ups, comments = user.comments)
        except Exception as e:
            raise Exception('error storing user')
    
    def list_users(self, order):
        """
        Lists users ordering the results according to the constraints defined by the parameters of the function
        
        Args:
            order (datetime): How the users must be ordered. Options are 'ups' (number of upvotes) or 'comments' number of comments
        
        Returns:
            [List(User)]: List of Users ordered accordingly
        """

        try:
            order_clause = DbUser.comments.desc() if order == 'comments' else DbUser.ups.desc()
            db_users = DbUser.select().order_by(order_clause)
            return [User(name = u.name, ups = u.ups, comments = u.comments) for u in db_users]
        except Exception as e:
            raise Exception('error listing user')