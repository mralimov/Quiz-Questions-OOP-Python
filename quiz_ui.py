from tkinter import *
from quiz_model import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text", fill=THEME_COLOR,
            font=('Arial', 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(
            image=true_img, highlightthickness=0, command=self.true_choice)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(
            image=false_img, highlightthickness=0, command=self.false_choice)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
