"""
@Title: 处理程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 16:20:17
@Description:
"""


class Handler:
    """

    """

    def callback(self, prefix, name, *args):
        """
        根据指定的前缀（如'start_'）和名称（如'paragraph'）查找相应的方
        法。这是通过使用getattr并将默认值设置为None实现的。如果getattr返回的对象是可调
        用的，就使用额外提供的参数调用它
        """
        # 获取某个属性，名称由 prefix + name 组成
        method = getattr(self, prefix + name, None)
        if callable(method):
            # 判断是不是方法（函数）
            return method(*args)

    def start(self, name):
        """方法start和end都是辅助方法，它们分别使用前缀start_和end_调用callback"""
        self.callback("start_", name)

    def end(self, name):
        """方法start和end都是辅助方法，它们分别使用前缀start_和end_调用callback"""
        self.callback("end_", name)

    def sub(self, name):
        """返回一个函数，这个函数将作为替换函数传递给re.sub（这就是它只接受一个匹配对象作为参数的原因所在）
        >>> import re
        >>> re.sub(r"\*(.+?)\*", handler.sub("emphasis"), "This *is* a test")
        "This <em>is<em> a test
        """
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution


class HTMLRender(Handler):
    """
    用于渲染 HTML 的具体处理程序
    HTMLRenderer 的方法可通过超类 Handler 的方法
    start()、end()和 sub() 来访问。这些方法实现了
    HTML 文档使用的基本标记
    """

    def start_document(self):
        print("<html><head><title>...</title></head><body>")

    def end_document(self):
        print("</body></html>")

    def start_paragraph(self):
        print("<p>")

    def end_paragraph(self):
        print("</p>")

    def start_heading(self):
        print("<h2>")

    def end_heading(self):
        print("</h2>")

    def start_list(self):
        print("<ul>")

    def end_list(self):
        print("</ul>")

    def start_listitem(self):
        print("<li>")

    def end_listitem(self):
        print("</li>")

    def start_title(self):
        print("<h1>")

    def end_title(self):
        print("</h1>")

    def sub_emphasis(self, match):
        return "<em>{}</em>".format(match.group(1))

    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data, end="")
