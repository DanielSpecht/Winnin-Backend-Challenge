from .repo_config import RepoConfig

class BaseRepo():
    """ Base class for the implementation of the repository pattern """
    
    def __init__(self):
        RepoConfig.get().database.connect(reuse_if_open=True)

    def __exit__(self, type_, value, traceback):
        self.close()

    def close(self):
        RepoConfig.get().database.close()