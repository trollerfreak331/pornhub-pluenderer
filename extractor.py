import re

class Extractor(object):
    def __init__(self):
        self._url_re = re.compile(r"a.+?href=\".+?viewkey=(.+?)\"", re.MULTILINE)

    def extract_viewkeys(self, data):
        urls = re.findall(self._url_re, data)

        return urls
