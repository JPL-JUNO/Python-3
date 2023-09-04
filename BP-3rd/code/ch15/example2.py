"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 13:55:11
@Description: 
"""

from urllib.request import urlopen
from html.parser import HTMLParser


def is_job(url):
    try:
        a, b, c, d = url.split("/")
    except ValueError:
        return False
    return a == d == "" and b == "jobs" and c.isdigit()


class Scraper(HTMLParser):
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get("href", "")
        if tag == 'a' and is_job(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.in_link:
            print("{} ({})".format("".join(self.chunks), self.url))
            self.in_link = False


text = urlopen("http://python.org/jobs").read().decode()
parser = Scraper()
parser.feed(text)
parser.close()
