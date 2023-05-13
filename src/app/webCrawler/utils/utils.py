import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    links = []
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        links.append(href)
    return links