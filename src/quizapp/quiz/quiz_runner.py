from src.quizapp.quizbrain.questions_model import Question
from src.quizapp.data.qdata import QuestionData
from src.quizapp.quizbrain.quiz_brain import QuizBrain

question_data = []
questions_object = QuestionData()

questions = []

user_input = input(f"Please choose a category: {questions_object.get_category()}\n")
question_data.append(questions_object.get_data(user_input)['results'])

for data in question_data[0]:
    questions.append(Question(data["question"], data["correct_answer"]))


quiz = QuizBrain(questions)
quiz.next_question()

while quiz.questions_left():
    quiz.next_question()

## add logic for multiple types instead of just boolean and give options to user to choose from.



