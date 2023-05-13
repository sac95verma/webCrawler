import argparse
from crawler import doCrawling

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('initial_url', help='the URL to start crawling (string)')
    parser.add_argument('depth', type=int, help='the depth to which to crawl (integer)')
    args = parser.parse_args()
    results = doCrawling(args.initial_url, args.depth)
    print({'results': results})