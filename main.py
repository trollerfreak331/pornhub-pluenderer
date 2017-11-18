from downloader import Downloader
from extractor import Extractor

# https://github.com/kennethreitz/clint cool shit \Q-Q/
from clint.textui import colored, puts

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()
    url = "https://pornhub.com"

    main_page = dl.get(url)
    viewkeys = ex.get_viewkeys(main_page)

    for key in viewkeys:
        absolute_url = "https://pornhub.com/view_video.php?viewkey=" + key
        page = dl.get(absolute_url)
        info = ex.get_video_info(page)

        if info == None:
            continue

        hdQuality = info['mediaDefinitions'][0]
        puts(colored.green(hdQuality["videoUrl"]))
        dl.save_file(hdQuality["videoUrl"], info['video_title'] + ".mp4")
