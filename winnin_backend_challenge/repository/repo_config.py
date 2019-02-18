from peewee import Proxy, SqliteDatabase

from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from settings import AppSettings

class RepoConfig(object):

    def __init__(self):
        self._database_path = None
        self._database = None
        self._database_proxy = None
            
    def set_database_path(self, path):
        self._database_path = path
        self._database = SqliteDatabase(self._database_path)
        self._database_proxy = Proxy()
        self._database_proxy.initialize(self._database)

    @property
    def database_path(self):
        return self._database_path

    @property
    def database(self):
        return self._database

    @property
    def database_proxy(self):
        return self._database_proxy
        
    # singleton
    instance = None
    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

RepoConfig().get().set_database_path(AppSettings.get().database_path)

#DATABASE_PROXY.initialize(DATABASE)
# DATABASE_PATH = './my_database_2.db'
# DATABASE = SqliteDatabase(DATABASE_PATH)
# DATABASE_PROXY = Proxy()
# DATABASE_PROXY.initialize(DATABASE)

# def set_database_path(path):
#     DATABASE_PATH = path
#     DATABASE_PROXY.initialize(SqliteDatabase(DATABASE_PATH))