import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(
        #     f"Q.{self.question_number}: {current_question.text} (True/False):")
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
    # def check_answer(self, user_answer, correct_answer):
    #     if user_answer.lower() == correct_answer.lower():

    #         self.score += 1
    #         print(f"You got it right!")
    #     # elif user_answer.lower() != "true" or user_answer.lower() != "false":
    #     #     print("Please check spelling of your answer")
    #     else:

    #         print(f"Sorry wrong answer")
    #     print(f"The correct answer was: {correct_answer}")
    #     print(f"Your current score is: {self.score}/{self.question_number}")
