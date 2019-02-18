class BackupEndpointDataRequest():
    def __init__(self, endpoint_data, timezone):
        """
        Args:
            endpoint_data (dict): dictionary conaining the result of the request to the reddit api
            timezone (str): The timezone to be used for processing the posts
        """

        self._endpoint_data = endpoint_data
        self._timezone = timezone
    
    @property
    def endpoint_data(self):
        return self._endpoint_data

    @property
    def timezone(self):
        return self._timezone