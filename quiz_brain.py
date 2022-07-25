class QuizBrain:
    def __init__(self, question_list, q_num=0, score=0):
        self.question_list = question_list
        self.q_num = q_num
        self.score = score
        self.correct = 0

    def questions_left(self):
        # index 12 doesn't exit, so we can only eval till < and not = as index 12 will give out of range
        return self.q_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.q_num]
        self.q_num += 1
        answer = input(f"Q.{self.q_num} {current_question.text} (True/False?)\n")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer.lower():
            self.score += 5
            print(f"Correct the answer is {correct_answer}")
            self.correct += 1
        else:
            print(f"Incorrect the correct answer is {correct_answer}")
        print(f"Your total is {self.score} points, you have {self.correct}/{self.q_num} questions right.")
