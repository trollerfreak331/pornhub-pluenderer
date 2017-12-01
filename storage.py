from os import path, makedirs

Download_Folder = "download/"


class AlreadyDownloadedError(Exception):
    def __init__(self, filename):
        message = "The file %s is skipped as it already exists."
        Exception.__init__(self, message % filename)


class Storage(object):
    def __init__(self):
        self._skipped_files = []

    def new_file(self, filename):
        if path.exists(filename):
            self._skipped_files.append(filename)
            raise AlreadyDownloadedError(filename)

        if path.exists(Download_Folder) is not True:
            makedirs(Download_Folder)

        return open(Download_Folder + filename, "wb")

    @property
    def skipped_files(self):
        return self._skipped_files
