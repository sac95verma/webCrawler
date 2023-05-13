# webCrawler
A web crawler is a Python script that crawls a website and collects information about the pages it visits. This web crawler takes an initial URL and a depth parameter as input, and returns a list of image links, the source page link, and the depth at which the image was found.

## Installation
- Clone the repository: git clone https://github.com/sac95verma/webCrawler.git
- Install the required packages: pip install -r requirements.txt

## Usage
Run the script using the following command:
`python web_crawler.py <initial_url> <depth>`
where <initial_url> is the URL to start crawling and <depth> is the depth to which to crawl.

For example, to crawl the website at http://example.com up to a depth of 2:
`python web_crawler.py http://example.com 2`


The script will output a JSON object containing the list of image links, source page links, and depths.

## Limitations
This web crawler has some limitations:

- It only crawls links that have an href attribute.
- It does not handle JavaScript or dynamic content.
- It may run into issues with very large websites or websites with complex navigation structures.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.