"""
@File         : multiplication_quiz.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-14 15:18:56
@Email        : cuixuanstephen@gmail.com
@Description  : 项目：乘法测验
"""

import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    prompt = f"#{question_number}: {num1} x {num2} = "
    try:
        pyip.inputStr(
            prompt,
            allowRegexes=[f"^{num1*num2}$"],
            # 元组中的第一个字符串是
            # 与每个可能的字符串匹配的正则表达式。
            # 因此，如果用户的回答与正确答案不符，
            # 该程序将拒绝他们提供的答案。
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
            blank=True,
        )
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        print("Correct!")
        correct_answers += 1
    time.sleep(1)
print(f"Score: {correct_answers/number_of_questions}")
