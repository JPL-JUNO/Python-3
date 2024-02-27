"""
@File         : 8_multiplication_quiz.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-14 18:47:04
@Email        : cuixuanstephen@gmail.com
@Description  : 编写自己的乘法测验
"""

# TODO 用户的输入应该启用新的线程，主线程等待，超时放弃
import pyinputplus as pyip

import random, time

question_numbers = 10
score = 0

for i in range(question_numbers):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    print(f"#{i} {num1} x {num2}")
    begin_time = time.time()
    while time.time() - begin_time < 8:
        answer = input("Enter Question Number:")
        if answer == str(num1 * num2):
            score += 1
            break
    else:
        break
