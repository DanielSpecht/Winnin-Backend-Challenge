
import unittest
import json
from os.path import join, dirname
import datetime
import sys
sys.path.insert(0,join(dirname(__file__), ".."))

from winnin_backend_challenge.domain import Post, User

class DomainTests(unittest.TestCase):
    def test_user_model_init(self):
        name = 'user'
        ups = 1
        comments = 2

        user = User(name, ups, comments)

        assert user.name == name
        assert user.ups == ups
        assert user.comments == comments

    def test_post_model_init(self):
        user = User('user', 1, 2)

        title = 'title'
        ups = 1
        comments = 2
        created = datetime.datetime.now()
        author = user
        
        post = Post(title, ups, comments, created, author)

        assert post.title == title
        assert post.ups == ups
        assert post.comments == comments
        assert post.created == created
        assert post.author == author

if __name__ == '__main__':
    unittest.main()
