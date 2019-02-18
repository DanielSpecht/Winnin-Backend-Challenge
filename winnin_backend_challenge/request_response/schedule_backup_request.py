class ScheduleBackupRequest():
    def __init__(self, hour, minute, second, timezone, endpoint):
        """
        Args:
            hour (str): The hour of day when the backup must occur
            minute (str): The minute of day when the backup must occur
            second (str): The second of day when the backup must occur
            timezone (str): The timezone to be used for processing the posts
            endpoint (str): The subreddit endpoint for hot posts
        """

        self._hour = hour
        self._minute = minute
        self._second = second
        self._timezone = timezone
        self._endpoint = endpoint
    
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
    def timezone(self):
        return self._timezone
    
    @property
    def endpoint(self):
        return self._endpoint