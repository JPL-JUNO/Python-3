"""
@File         : random_quiz_generator.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-15 20:06:03
@Email        : cuixuanstephen@gmail.com
@Description  : 项目：生成随机的测验试卷文件
"""

import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

for quiz_num in range(35):
    quiz_file = open(f"capitals_quiz{quiz_num+1}.txt", "w")
    answer_key_file = open(f"capitals_answer{quiz_num+1}.txt", "w")
    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write((" " * 20) + f"State Capitals Quiz (Form{quiz_num+1})")
    quiz_file.write("\n\n")

    states = list(capitals.keys())
    random.shuffle(states)
    # 打乱答案
    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        wrong_answer = list(capitals.values())
        # 删除正确的答案
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_options = wrong_answer + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write(
            f"{question_num+1}. What is the capital of {states[question_num]}?\n"
        )
        for i in range(4):
            quiz_file.write(f"  {'ABCD'[i]}. { answer_options[i]}\n")
            quiz_file.write("\n")
        answer_key_file.write(
            f"{question_num+1}. {'ABCD'[answer_options.index(correct_answer)]}\n"
        )
    quiz_file.close()
    answer_key_file.close()
