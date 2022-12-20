import os

class AvailableFiles(object):

    def __new__(self, args:str='app/static/public'):
        files = [f for f in os.listdir(args)]
        return files
    