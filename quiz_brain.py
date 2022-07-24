
class QuizBrain:
    def __init__(self, question_list, q_num=0, score=0):
        self.question_list = question_list
        self.q_num = q_num
        self.score = score

    def questions_left(self):
        # index 12 doesn't exit, so we can only eval till < and not = as index 12 will give out of range
        return self.q_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.q_num]
        self.q_num += 1
        input(f"Q.{self.q_num} {current_question.text} (True/False?)")