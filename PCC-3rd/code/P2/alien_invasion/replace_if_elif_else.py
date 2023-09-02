"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-02 22:56:32
@Description: 
"""


class ReplaceIfElse:

    def __init__(self):
        self._formatter = {
            'csv': self.formatter_csv,
            'html': self.formatter_html,
            'pdf': self.formatter_pdf,
        }

    def formatter_csv(self):
        print("CSV format")

    def formatter_html(self):
        print("HTML format")

    def formatter_pdf(self):
        print("PDF format")

    def replace_if_elif_else(self, extension):
        if extension in self._formatter:
            self._formatter[extension]()
        else:
            raise RuntimeError("Unknown format")


if __name__ == "__main__":
    ins = ReplaceIfElse()
    ins.replace_if_elif_else("csv")
    ins.replace_if_elif_else("pdf")
    ins.replace_if_elif_else("html")
