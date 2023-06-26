"""
@Description: Lists of Lists
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-26 12:36:33
"""

# A list with three lists of length 3 can represent a tic-tac-toe board
# 2-14
board = [['_'] * 3 for _ in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# A list with three references to the same list is useless
# 2-15
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board)

# what code list 2-15 do
row = ['_'] * 3
weird_board = []
for _ in range(3):
    weird_board.append(row)
print(weird_board)

# what code list 2-14 do
board = []
for i in range(3):
    # 每次都会创建一个新的row来引用
    row = ['_'] * 3
    board.append(row)
print(board)