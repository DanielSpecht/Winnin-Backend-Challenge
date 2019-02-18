from os.path import *

class AppSettings(object):

    def __init__(self):
        # Database settings
        self._database_path = './my_database.db'
        self._create_db_if_not_exists = True
        self._load_from_json = True
        self._json_file_endpoint_data = [join(dirname(__file__), '..' ,'resources', 'hot_posts.json')]

        # Backup Scheduler settings
        self._initialize_scheduler = True
        self._timezone = 'America/Sao_Paulo'
        self._hour = "13"
        self._minute = "0"
        self._second = "0" 

        # Endpoint settings 
        self._initialize_endpoints = True
        self._posts_api = 'https://api.reddit.com/r/artificial/hot'
        self._host = '127.0.0.1'
        self._port = 5000

    @property
    def database_path(self):
        return self._database_path
    
    @property
    def create_db_if_not_exists(self):
        return self._create_db_if_not_exists

    @property
    def load_from_json(self):
        return self._load_from_json

    @property
    def json_file_endpoint_data(self):
        return self._json_file_endpoint_data

    @property
    def initialize_scheduler(self):
        return self._initialize_scheduler

    @property
    def timezone(self):
        return self._timezone

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @property
    def initialize_endpoints(self):
        return self._initialize_endpoints

    @property
    def posts_api(self):
        return self._posts_api

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port
    
    # singleton
    instance = None
    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance