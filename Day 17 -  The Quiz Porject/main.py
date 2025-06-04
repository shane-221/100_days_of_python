from question_model import Question
from data import question_data

object_question_bank=[]

    # Todo 1 : Creation of a qquestion bank using the class:
for i in question_data:
    question = Question(i["text"], i["answer"])
    object_question_bank.append(question)

print(object_question_bank)