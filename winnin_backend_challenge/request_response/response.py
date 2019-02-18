class Response():
    def __init__(self, response_data = None):
        """
            response_data (list, optional): Defaults to None. The contents of the output of the executed use case
        """

        self.data = response_data
        self.errors = []

    def add_error(self, error, message):
        self.errors.append({'error': error, 'message': message})

    def add_exception_error(self, exception):
        self.add_error(format(exception.__class__.__name__ ), format(exception))

    @property
    def has_errors(self):
        return len(self.errors) > 0