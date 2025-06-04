from question_model import Question
from data import question_data

object_question_bank=[]

    # Todo 1 : Creation of a question bank in a list using the class:
for i in question_data:
    new_question = Question(i["text"], i["answer"])
    object_question_bank.append(new_question)

    # Todo 2: Bring up one of those questions. 