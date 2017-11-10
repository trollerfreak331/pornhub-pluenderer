from os import path

class AlreadyDownloadedError(Exception):
    def __init__(self, filename):
        Exception.__init__(self, "The file %s is skipped as it already exists." % filename)

class Storage(object):
    def __init__(self):
        self._skipped_files = []

    def new_file(self, filename):
        if path.exists(filename):
            self._skipped_files.append(filename)
            raise AlreadyDownloadedError(filename)

        return open(filename, "wb")

    @property
    def skipped_files(self):
        return self._skipped_files