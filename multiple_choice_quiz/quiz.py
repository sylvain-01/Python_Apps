# Building a Multiple Choice Quiz


from question import Question


question_prompts = [
    "How many states are there in America?\n(a) 48\n(b) 52\n(c) 50\n\n",
    "What city is the capital of France?\n(a) Paris\n(b) London\n(c) Milan\n\n",
    "What bird is famous for being pink?\n(a) Raven\n(b) Flamingo\n(c) Cardinal\n\n",
    "Babe Ruth is synonymous with which sport?\n(a) Baseball\n(b) Cricket\n(c) Football\n\n",
    "What is the largest land animal to roam the planet?\n(a) Mouse\n(b) Polar Bear\n(c) Elephant\n\n"

]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

        print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)


