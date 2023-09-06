"""
@Title: 一个简单的页面创建脚本
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-06 11:41:16
@Description:
"""

from xml.sax.handler import ContentHandler
from xml.sax import parse


class PageMaker(ContentHandler):
    passthrough = False

    def startElement(self, name, attrs):
        if name == "page":
            self.passthrough = True
            self.out = open(attrs["name"] + ".html", "w")
            self.out.write("<html><head>\n")
            self.out.write("<title>{}</title>\n".format(attrs["title"]))
            self.out.write("</head><body>\n")
        elif self.passthrough:
            self.out.write("<" + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write(">")

    def endElement(self, name):
        if name == "page":
            self.passthrough = False
            self.out.write("\n</body></html>\n")
            self.out.close()
        elif self.passthrough:
            self.out.write("</{}>".format(name))

    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)


parse('./website.xml', PageMaker())
