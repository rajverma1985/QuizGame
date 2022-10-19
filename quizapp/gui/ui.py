# class based UI using tkinter
from tkinter import *
from quizapp.data.qdata import QuestionData
from quizapp.quizbrain.quiz_brain import QuizBrain

THEME_COLOR = "#375362"
score = 0
category = [cat['name'] for cat in QuestionData().get_category()]


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(font=("Arial", 20), text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # always remember the first 2 values are the position of the text, 1/2 of canvas to center it.
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="This is a test question",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons and their images
        right_image = PhotoImage(file="../images/true.png")
        self.rt_button = Button(image=right_image, highlightthickness=0, command=self.right_pressed)
        self.rt_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="../images/false.png")
        self.wr_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_pressed)
        self.wr_button.grid(row=2, column=1)
        self.get_ques()
        self.window.mainloop()

    def get_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.questions_left():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.rt_button.config(state="disabled")
            self.wr_button.config(state="disabled")

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_ques)

# dropdown = StringVar(self.window)
# dropdown.set("Select Category")
# options = OptionMenu(self.window, dropdown, *category)
# options.grid(row=0, column=0)