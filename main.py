import sys
import signal
from clint.textui import colored, puts
from downloader import Downloader
from extractor import Extractor

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))


if __name__ == "__main__":
    Downloader = Downloader()
    Extractor = Extractor()
    Url = "https://pornhub.com"

    puts(colored.green("getting video keys."))
    MainPage = Downloader.get(Url)
    ViewKeys = Extractor.get_viewkeys(MainPage)

    puts(colored.green("starting to download videos."))
    for key in ViewKeys:
        puts(colored.green("getting video information."))
        absolute_url = "https://pornhub.com/view_video.php?viewkey=" + key
        page = Downloader.get(absolute_url)
        info = Extractor.get_video_info(page)

        if info is None:
            continue

        hdQuality = info['mediaDefinitions'][0]
        puts(colored.green("downloading video %s." % info['video_title']))
        Downloader.save_file(hdQuality["videoUrl"], info['video_title'] + ".mp4")
