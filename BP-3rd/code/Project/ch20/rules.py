# """
# @Title: 规则
# @Author(s): Stephen CUI
# @LastEditor(s): Stephen CUI
# @CreatedTime: 2023-09-05 16:44:01
# @Description:
# """
# from handlers import HTMLRender


# class Rule:
#     """
#     所有规则的基类
#     规则是供主程序（解析器）使用的。主程序必须根据给定的文本块选择合适的规则来对其进行必要的转换。换而言之，规则必须具备如下功能：
#     1. 知道自己适用于那种文本块（条件）
#     2. 对文本块进行转换（操作）
#     """

#     def action(self, block, handler):
#         handler.start(self.type)
#         handler.feed(block)
#         handler.end(self.type)
#         return True


# class HeadingRule(Rule):
#     """
#     标题只包含一行，不超过 70 个字符且不以冒号结尾
#     """
#     type = "heading"

#     def condition(self, block):
#         return not '\n' in block and len(block) <= 70 and not block[-1] == ":"


# class TitleRule(HeadingRule):
#     """
#     题目是文档中的第一个文本块，前提条件是它属于标题
#     """
#     type = "title"
#     first = True

#     def condition(self, block):
#         if not self.first:
#             return False
#         self.first = False
#         return HeadingRule.condition(self, block)


# class ListItemRule(Rule):
#     """
#     列表项是以连字符打头的段落。在设置格式的过程中，将把连字符删除
#     """
#     type = "listitem"

#     def condition(self, block):
#         return block[0] == '-'

#     def action(self, block, handler: HTMLRender):
#         """
#         它重新实现了方法action。相比于Rule的方法action，这个方法唯一的不同之处在于，它删
#         除了文本块中的第一个字符（连字符），并删除了余下文本中多余的空白。标记会生成列表项目
#         符号，因此不再需要连字符。
#         """
#         handler.start(self.type)
#         handler.feed(block[1:].strip())
#         handler.end(self.type)
#         return True


# class ListRule(ListItemRule):
#     """
#     列表以紧跟在非列表项文本块后面的
#     列表项开头，以相连的最后一个列表
#     项结束
#     """
#     type = "list"
#     inside = False

#     def condition(self, block):
#         return True

#     def action(self, block, handler):
#         if not self.inside and ListItemRule.condition(self, block):
#             # handler 是 Handler 的一个实例
#             handler.start(self.type)
#             self.inside = True
#         elif self.inside and not ListItemRule.condition(self, block):
#             handler.end(self.type)
#             self.inside = False
#         return False


# class ParagraphRule(Rule):
#     """
#     段落是不符合其他规则的文本块
#     """
#     type = 'paragraph'

#     def condition(self, block):
#         return True
class Rule:
    """
    Base class for all rules.
    """

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    A heading is a single line that is at most 70 characters and
    that doesn't end with a colon.
    """
    type = 'heading'

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(HeadingRule):
    """
    The title is the first block in the document, provided that
    it is a heading.
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    A list item is a paragraph that begins with a hyphen. As part of the
    formatting, the hyphen is removed.
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    A list begins between a block that is not a list item and a
    subsequent list item. It ends after the last consecutive list item.
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    A paragraph is simply a block that isn't covered by any of the other rules.
    """
    type = 'paragraph'

    def condition(self, block):
        return True
