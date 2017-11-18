import re
import json

viewkey_re = r"a.+?href=\".+?viewkey=(.+?)\""
info_re = r"var flashvars_.+? = ({.+})"


class Extractor(object):
    def __init__(self):
        self._viewkey_re = re.compile(viewkey_re, re.MULTILINE)
        self._videoinfo_re = re.compile(info_re, re.MULTILINE)

    def get_viewkeys(self, data):
        matches = re.findall(self._viewkey_re, data)
        return set(matches) # convert the list of matched strings to a set to eliminate redundant viewkeys

    def get_video_info(self, data):
        infoJson = re.search(self._videoinfo_re, data)
        if infoJson == None:
            return None
        return json.loads(infoJson.group(1))
