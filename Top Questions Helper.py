import json
import random

with open("/home/jimmy/projects/practice/Top Questions.txt", "r") as f:
    arr = f.read().splitlines()
    questions = {}
    for each in arr:
        split = each.index("-")
        questions[each[:split-1]] = each[split+2:]
    # print(questions)

    # questions_json = json.dumps(questions)
    # with open("/home/jimmy/projects/practice/Top Questions JSON.txt", "w") as j:
    #     json.dump(questions_json, j)
    

print(random.choice(list(questions.items())))