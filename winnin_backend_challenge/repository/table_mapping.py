from peewee import *
from .repo_config import RepoConfig
import datetime

class BaseModel(Model):
    class Meta:
        database = RepoConfig.get().database_proxy

class DbUser(BaseModel):
    name = TextField()
    ups = IntegerField(default=0)
    comments = IntegerField(default=0)

    def to_dict(self):
        return {'name': self.name, 'ups': self.ups, 'comments': self.comments}

class DbPost(BaseModel):
    title = TextField()
    ups = IntegerField(default=0)
    comments = IntegerField(default=0)
    created = DateTimeField(formats=['%Y-%m-%d %H:%M:%S'])
    author = ForeignKeyField(DbUser, backref='posts')

    def to_dict(self):
        return {'title': self.title, 'ups': self.ups, 'comments': self.comments, 'created': self.created, 'author': self.author}