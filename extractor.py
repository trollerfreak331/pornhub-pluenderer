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

        # convert to a set to eliminate redundant viewkeys
        return set(matches)

    def get_video_info(self, data):
        info_json = re.search(self._videoinfo_re, data)
        if info_json is None:
            return None
        return json.loads(info_json.group(1))
