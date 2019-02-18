from .repository.repo_config import RepoConfig
from .settings import AppSettings
from .repository.table_mapping import DbPost, DbUser
from flask import Flask
from flask_restful_swagger_2 import Api
from .rest import PostResource, UserResource
from .use_cases import ScheduleBackupUseCase, BackupEndpointDataUseCase
from .request_response import ScheduleBackupRequest, BackupEndpointDataRequest
from os.path import isfile
import json

def run_app():
    
    # Setup database
    if not isfile(AppSettings.get().database_path):
        if AppSettings.get().create_db_if_not_exists:
            RepoConfig.get().database.create_tables([DbPost,DbUser])
        else:
            raise Exception('Database %s does not exist'%(AppSettings.get().database_path))

    if AppSettings.get().load_from_json:
        for file in AppSettings.get().json_file_endpoint_data:
            with open(file,'r') as f:
                endpoint_data = json.loads(f.read())
                backup_request = BackupEndpointDataRequest(endpoint_data, AppSettings.get().timezone)
                uc = BackupEndpointDataUseCase()
                uc.execute(backup_request)
                
    # Schedule backups
    if AppSettings.get().initialize_scheduler:
        schedule_request = ScheduleBackupRequest(AppSettings.get().hour, AppSettings.get().minute, AppSettings.get().second, AppSettings.get().timezone, AppSettings.get().posts_api)
        scheduler = ScheduleBackupUseCase()
        scheduler.execute(schedule_request)

    # Start rest endpoints
    if AppSettings.get().initialize_endpoints:
        app = Flask(__name__)
        api = Api(app, api_version='1.0', api_spec_url='/api/swagger', title = 'Winnin Backend Challenge', description = 'Implementation of the winnin backend challenge')
        api.add_resource(PostResource, '/api/posts')
        api.add_resource(UserResource, '/api/users')
        app.run(host = AppSettings.get().host, port = AppSettings.get().port)