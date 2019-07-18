from QuestionClass import Question

question_prompts = [
    "1. What is the colour of Banana: ?\n a. yellow\n b. Orange\n c. Blue\n d.Red\n\n",
    "2. What is the colour of Apple: ?\n a. yellow\n b. Orange\n c. Blue\n d.Red\n\n",
    "3. What is the colour of orange: ?\n a. yellow\n b. Orange\n c. Blue\n d.Red\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "b"),
]

def runtest(questions):
    score = 0

    for test in questions:
        print(test.prompts)
        answer = input("Enter you option: ")
        if (answer == test.options):
            score = score + 1

    return score

print("Exam begins now !")
result = runtest(questions)
print("Your score is " +str(result))


