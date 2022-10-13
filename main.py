from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


print(question_bank)

quizz = QuizBrain(question_bank)

while quizz.still_has_question():
    quizz.next_question()

print("Quizz is completed :)")
print(f"Total score is {quizz.score}/{quizz.question_number}")