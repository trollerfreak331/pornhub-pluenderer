import re

viewkey_re = r"a.+?href=\".+?viewkey=(.+?)\""
title_re = r"<span class=\"inlineFree\">(.+?)</span>"


class Extractor(object):
    def __init__(self):
        self._viewkey_re = re.compile(viewkey_re, re.MULTILINE)
        self._title_re = re.compile(title_re, re.MULTILINE)

    def extract_viewkeys(self, data):
        matches = re.findall(self._viewkey_re, data)
        return set(matches) # convert the list of matched strings to a set to eliminate redundant viewkeys

    def extract_title(self, data):
        match = re.search(self._title_re, data)
        return match.group(1)

    def extract_video_url(self, data):
        pass
