from question_model import Question
from data import question_data
from quiz_model import QuizBrain
from quiz_ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
