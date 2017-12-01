import sys
import signal
from clint.textui import colored, puts
from downloader import downloader
from extractor import extractor

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))


if __name__ == "__main__":
    downloader = downloader()
    extractor = extractor()
    url = "https://pornhub.com"

    puts(colored.green("getting video keys."))
    MainPage = downloader.get(url)
    ViewKeys = extractor.get_viewkeys(MainPage)

    puts(colored.green("starting to download videos."))
    for key in ViewKeys:
        puts(colored.green("getting video information."))
        absolute_url = "https://pornhub.com/view_video.php?viewkey=" + key
        page = downloader.get(absolute_url)
        info = extractor.get_video_info(page)

        if info is None:
            continue

        hdQuality = info['mediaDefinitions'][0]
        puts(colored.green("downloading video %s." % info['video_title']))
        downloader.save_file(hdQuality["videoUrl"], info['video_title'] + ".mp4")
