import re

viewkey_re = r"a.+?href=\".+?viewkey=(.+?)\""


class Extractor(object):
    def __init__(self):
        self._url_re = re.compile(viewkey_re, re.MULTILINE)

    def extract_viewkeys(self, data):
        urls = re.findall(self._url_re, data)

        return urls
