class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return f"Your question is: {self.text} and answer is: {self.answer}"
