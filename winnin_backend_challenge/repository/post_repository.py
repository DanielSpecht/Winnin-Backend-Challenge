from .base_repo import BaseRepo
from .table_mapping import DbPost

from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))

from domain import Post

class PostRepo(BaseRepo):

    def add_post(self, post):
        """
        Persists a post to the database
        
        Args:
            post (Post): The post to be persisted
        """


        try:        
            return DbPost.create(title = post.title , ups = post.ups, comments = post.comments, created = post.created, author = post.author)
        except Exception as e:
            raise Exception('error storing post')
    
    def list_posts(self, order, start, end):
        """
        Lists posts in a period of time, ordering the results according to the constraints defined by the parameters of the function
        
        Args:
            order (datetime): How the posts must be ordered. Options are 'ups' (number of upvotes) or 'comments' number of comments
            start (datetime): The start of the period 
            end (datetime): The end of the period 
                
        Returns:
            [List(Post)]: List of Posts ordered accordingly
        """

        try:
            order_clause = DbPost.comments.desc() if order == 'comments' else DbPost.ups.desc()
            db_posts = DbPost.select().where(DbPost.created.between(start, end)).order_by(order_clause)            
            return [Post(title = p.title, ups = p.ups, comments = p.comments, created = p.created, author = p.author.name) for p in db_posts]
        except Exception as e:
            raise Exception('error listing post')