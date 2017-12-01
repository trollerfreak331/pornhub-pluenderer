import sys
import signal
from clint.textui import colored, puts
from downloader import Downloader
from extractor import Extractor

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))


def main():
    downloader = Downloader()
    extractor = Extractor()
    url = "https://pornhub.com"

    puts(colored.green("getting video keys."))
    main_page = downloader.get(url)
    view_keys = extractor.get_viewkeys(main_page)

    puts(colored.green("starting to download videos."))
    for key in view_keys:
        puts(colored.green("getting video information."))
        absolute_url = "https://pornhub.com/view_video.php?viewkey=" + key
        page = downloader.get(absolute_url)
        info = extractor.get_video_info(page)

        if info is None:
            continue

        hd_quality = info['mediaDefinitions'][0]
        puts(colored.green("downloading video %s." % info['video_title']))
        downloader.save_file(hd_quality["videoUrl"], info['video_title'] + ".mp4")


if __name__ == "__main__":
    main()
