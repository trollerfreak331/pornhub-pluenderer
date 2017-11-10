import requests as http
from storage import Storage

class Downloader(object):
    def __init__(self):
        self._storage = Storage()

    def get(self, url):
        rsp = http.get(url)
        return rsp.text

    def save_file(self, url, filename):
        rsp = http.get(url, stream=True)

        with self._storage.new_file(filename) as file:
            for chunk in rsp.iter_content(chunk_size=4096):
                if chunk:
                    file.write(chunk)