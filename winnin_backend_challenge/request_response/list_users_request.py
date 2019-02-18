class ListUsersRequest():
    def __init__(self, order):
        """
        Args:
            order (datetime): How the users must be ordered. Options are 'ups' (number of upvotes) or 'comments' number of comments
        """           
        self._order = order
    
    @property
    def order(self):
        return self._order