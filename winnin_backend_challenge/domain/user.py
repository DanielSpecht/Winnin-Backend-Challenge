from datetime import datetime

class User():
    def __init__(self, name, ups, comments):
        """
        Initializes the User object
        
        Args:
            name (str): The name of the user
            ups (int): The number of upvotes of the posts of the user
            comments (int): The number of comments the posts of the user had
        """
        self.name = name
        self.ups = ups
        self.comments = comments

    def to_dict(self):
        """ Represents the object in a dictionary """
        return {'name': self.name, 'ups': self.ups, 'comments': self.comments}