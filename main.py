from downloader import Downloader
from extractor import Extractor

# https://github.com/kennethreitz/clint cool shit \Q-Q/
from clint.textui import colored, puts

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()
    url = "https://pornhub.com"

    rsp = dl.get(url)
    viewKeys = ex.extract_viewkeys(rsp)

    for key in viewKeys:
        puts(colored.green(key))
