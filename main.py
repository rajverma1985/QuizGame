from questions_model import Question
from data import QuestionData
from quiz_brain import QuizBrain

question_data = []
questions_object = QuestionData()
question_data.append(questions_object.get_data())
questions = []
print(question_data)

for data in question_data[0]:
    question = Question(data["question"], data["correct_answer"])
    questions.append(question)


quiz = QuizBrain(questions)
quiz.next_question()

while quiz.questions_left():
    quiz.next_question()



