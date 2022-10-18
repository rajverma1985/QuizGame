# class based UI using tkinter
from tkinter import *

THEME_COLOR = "#375362"
score = 10


# legend: 2 column and 3 rows structure. Get a theme color, padding of 20 across,
# font Arial, 20 italic for the question inside the box in middle, height 250, width 300
# green and red check and cross of correct and incorrect
# score on top right

class QuizUi:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.text = Label(font=("Arial", 20), text=f"score:{score}", fg="white", bg=THEME_COLOR)
        self.text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        # always remember the first 2 values are the position of the text, 1/2 of canvas to center it.
        self.ques_canvas = self.canvas.create_text(150, 125, text="This is a test question",
                                                   font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons and their images
        right_image = PhotoImage(file="../images/true.png")
        wrong_image = PhotoImage(file="../images/false.png")
        self.rt_button = Button(image=right_image, highlightthickness=0)
        self.wr_button = Button(image=wrong_image, highlightthickness=0)
        self.rt_button.grid(row=2, column=0)
        self.wr_button.grid(row=2, column=1)
        self.window.mainloop()


new = QuizUi()
