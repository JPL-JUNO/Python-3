"""
@Description: Piping output
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-16 20:06:26
"""
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print("Word count: ", wordcount)
