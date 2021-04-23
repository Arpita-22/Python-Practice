from copy import deepcopy

question_template = {
"title": "default title",
"question": "default question",
"answer": "default answer",
"hints": []
}


def populateQuestions(title, question, answer, hints = None):

    #makes a shallow copy of the dict with all its objects
    # myQuestion_template = question_template.copy()
    #it would be a brand new list and changes to it won't affect changes to other questions
    myQuestion_template = deepcopy(question_template)

    myQuestion_template["title"] = title
    myQuestion_template["question"] = question
    myQuestion_template["answer"] = answer
    # myQuestion_template["hints"] = []

    if hints != None:
        # for hint in hints:
        #     myQuestion_template["hints"].append(hint)
        
        # myQuestion_template["hints"] = hints
        myQuestion_template["hints"].extend(hints) 

    return myQuestion_template


question_1 = populateQuestions("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
question_2 = populateQuestions("title2", "question2", "answer2")
question_3 = populateQuestions("title3", "question3", "answer3", ["q3 hint1"])

print(question_1, question_2, question_3)