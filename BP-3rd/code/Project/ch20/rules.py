"""
@Title: 规则 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 16:44:01
@Description: 
"""
from handlers import HTMLRender


class Rule:
    """
    所有规则的基类
    """

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(block)
        return True


class HeadingRule(Rule):
    """
    标题只包含一行，不超过 70 个字符且不以冒号结尾
    """
    type = "heading"

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ":"


class TitleRule(HeadingRule):
    """
    """
    type = "title"
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    type = "listitem"

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler: HTMLRender):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    type = "listitem"
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            # handler 是 Handler 的一个实例
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    """
    type = 'paragraph'

    def condition(self, block):
        return True
