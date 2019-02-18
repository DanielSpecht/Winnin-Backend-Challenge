from apscheduler.schedulers.background import BackgroundScheduler
from .get_endpoint_data_use_case import GetEndpointDataUseCase
from .backup_endpoint_data_use_case import BackupEndpointDataUseCase
import pytz

from os.path import join, dirname
import sys
sys.path.append(join(dirname(__file__), ".."))
from request_response import GetEndpointDataRequest, BackupEndpointDataRequest, Response

class ScheduleBackupUseCase():
    """ Use case for schedulling when the backup must occur"""
    def execute(self, request):
        response = Response()
        try:
            def backup_endpoint_posts():
                print('backing up')
                # Obtain post data from endpoint
                get_data_request = GetEndpointDataRequest(request.endpoint)
                get_data_uc = GetEndpointDataUseCase()
                endpoint_data_response = get_data_uc.execute(get_data_request)

                # Backup obtained endpoint
                backup_data_request = BackupEndpointDataRequest(endpoint_data_response.data, timezone = request.timezone)
                backup_data_uc = BackupEndpointDataUseCase()
                backup_data_uc.execute(backup_data_request)

            # Start scheduler
            scheduler = BackgroundScheduler()
            scheduler.add_job(lambda: backup_endpoint_posts(), 'cron', hour = request.hour, minute = request.minute, second = request.second, timezone =  pytz.timezone(request.timezone))
            scheduler.start()

            return response

        except Exception as e:
            response.add_exception_error(e)
            return response