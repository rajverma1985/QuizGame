import html


class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def questions_left(self):
        # index 12 doesn't exit, so we can only eval till < and not = as index 12 will give out of range
        return self.q_num < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.q_num]
        self.q_num += 1
        # human-readable format and un-escaping the special characters
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.q_num}: {q_text}"

    def check_answer(self, answer):
        correct_answer = self.current_question.answer
        if answer.lower() == correct_answer.lower():
            self.score += 5
            return True
        else:
            return False
