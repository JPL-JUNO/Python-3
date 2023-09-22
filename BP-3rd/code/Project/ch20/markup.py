"""
@Title: 主程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 17:01:21
@Description:
"""

import sys
import re
from handlers import HTMLRender, Handler
from util import blocks
from rules import TitleRule, ListItemRule, ParagraphRule, HeadingRule, Rule, ListRule
from typing import Callable


class Parser:
    def __init__(self, handler: Handler) -> None:
        self.handler: Handler = handler
        self.rules: list[Rule] = []
        self.filters: list[Callable] = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start("document")
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end("document")


class BasicTextParser(Parser):
    def __init__(self, handler: Handler) -> None:
        super().__init__(handler)
        # Parser.__init__(self, handler)

        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r"\*(.+?)\*", "emphasis")
        self.addFilter(r"(http://[\.a-zA-Z/]+)", "url")
        self.addFilter(r"([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)", "mail")


if __name__ == '__main__':
    handler = HTMLRender()
    parser = BasicTextParser(handler)
    parser.parse(sys.stdin)
