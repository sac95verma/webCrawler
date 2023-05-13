import argparse
import requests
from bs4 import BeautifulSoup
from utils import utils
from validations import validate_input 

def doCrawling(initial_url, max_depth):
    visited = set()
    images = []
    queue = [(initial_url, 0)]
    while queue:
        url, depth = queue.pop(0)
        if depth > max_depth:
            break
        if url in visited:
            continue
        visited.add(url)
        try:
            response = requests.get(url)
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL: {url}")
            continue
        soup = BeautifulSoup(response.content, 'html.parser')
        for img in soup.find_all('img'):
            images.append({
                'imageUrl': img['src'],
                'sourceUrl': url,
                'depth': depth
            })
        for link in utils.get_all_links(url):
            queue.append((link, depth+1))
    return images

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('initial_url', help='the string URL to start crawling')
    parser.add_argument('depth', type=int, help='the depth to which to crawl (integer)')
    args = parser.parse_args()
    validate_input(args.initial_url, args.depth)
    results = doCrawling(args.initial_url, args.depth)
    print({'results': results})
