import requests as http
from storage import Storage


class Downloader(object):
    def __init__(self):
        self.storage = Storage()

    @classmethod
    def get(self, url):
        rsp = http.get(url)
        return rsp.text

    def save_file(self, url, name):
        file = self.storage.new_file(name)
        if file:
            rsp = http.get(url, stream=True)
            for chunk in rsp.iter_content(chunk_size=1000 * 1024):
                if chunk:  # filter out "keep-alive" chunks
                    file.write(chunk)
