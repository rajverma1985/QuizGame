from quizapp.gui.ui import QuizUi
from quizapp.quizbrain.questions_model import Question
from quizapp.data.qdata import QuestionData
from quizapp.quizbrain.quiz_brain import QuizBrain


question_data = []
get_data = QuestionData().get_data("General Knowledge")["results"]

for question in get_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_data.append(new_question)

quiz = QuizBrain(question_data)
new = QuizUi(quiz)