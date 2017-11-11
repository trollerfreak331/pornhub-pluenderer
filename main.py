from downloader import Downloader
from extractor import Extractor

# https://github.com/kennethreitz/clint cool shit \Q-Q/
from clint.textui import colored, puts

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()
    url = "https://pornhub.com"

    main_page = dl.get(url)
    viewkeys = ex.extract_viewkeys(main_page)

    for i, key in enumerate(viewkeys):
        absolute_url = "https://pornhub.com/view_video.php?viewkey=" + key
        page = dl.get(absolute_url)

        title = ex.extract_title(page)
        puts(colored.green("%d -> %s : %s" % (i, key, title)))
