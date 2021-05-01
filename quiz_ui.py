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

        self.window.mainloop()
