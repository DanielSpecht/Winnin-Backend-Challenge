class ListPostsRequest():
    def __init__(self, order, start, end):
        """
        Args:
            order (datetime): How the posts must be ordered. Options are 'ups' (number of upvotes) or 'comments' number of comments
            start (datetime): The start of the period 
            end (datetime): The end of the period 
        """

        self._order = order
        self._start = start
        self._end = end
    
    @property
    def order(self):
        return self._order
    
    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end