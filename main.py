from downloader import Downloader
from extractor import Extractor

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()

    url = "https://pornhub.com"

    rsp = dl.get(url)
    viewKeys = ex.extract_viewkeys(rsp)

    for key in viewKeys:
        print(key)
