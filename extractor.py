import re

class Extractor(object):
    def __init__(self):
        self.url_re = re.compile(r"a.+? href=\"(.+?)\"", re.MULTILINE)

    def extract_urls(self, base_url, data):
        urls = re.findall(self.url_re, data)

        for i, url in enumerate(urls):
            if not url.startswith(base_url):
                urls[i] = base_url + url

        return urls