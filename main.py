from questions_model import Question
from data import QuestionData
from quiz_brain import QuizBrain

questions = []
for data in question_data:
    question = Question(data["text"], data["answer"])
    questions.append(question)


quiz = QuizBrain(questions)
quiz.next_question()

while quiz.questions_left():
    quiz.next_question()


