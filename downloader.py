import requests as http

class Downloader(object):
    def get(self, url):
        rsp = http.get(url)
        return rsp.text