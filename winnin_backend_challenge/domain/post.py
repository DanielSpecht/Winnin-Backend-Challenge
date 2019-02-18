from datetime import datetime

class Post():
    def __init__(self, title, ups, comments, created, author):
        """
        Initializes the Post object
        Args:
            title (str): The title of the post
            ups (int): The number of upvotes of the post
            comments (int): The number of comments the post had
            created (datetime): The time of creation of the post
            author (User): The user that created the post
        """

        self.title = title
        self.ups = ups
        self.comments = comments
        self.created = created
        self.author = author
    
    def to_dict(self):
        """ Represents the object in a dictionary """
        return {'title': self.title, 'ups': self.ups, 'comments': self.comments, 'created': self.created, 'author': self.author}