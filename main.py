from downloader import Downloader
from extractor import Extractor
import sys
import signal
from clint.textui import colored, puts

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))


if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()
    url = "https://pornhub.com"

    puts(colored.green("getting video keys."))
    main_page = dl.get(url)
    viewkeys = ex.get_viewkeys(main_page)

    puts(colored.green("starting to download videos."))
    for key in viewkeys:
        puts(colored.green("getting video information."))
        absolute_url = "https://pornhub.com/view_video.php?viewkey=" + key
        page = dl.get(absolute_url)
        info = ex.get_video_info(page)

        if info is None:
            continue

        hdQuality = info['mediaDefinitions'][0]
        puts(colored.green("downloading video %s." % info['video_title']))
        dl.save_file(hdQuality["videoUrl"], info['video_title'] + ".mp4")
