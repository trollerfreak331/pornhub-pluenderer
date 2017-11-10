from downloader import Downloader
from extractor import Extractor

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()

    url = "https://pornhub.com"

    rsp = dl.get(url)
    urls = ex.extract_urls(url, rsp)
    for url in urls:
        print(url)