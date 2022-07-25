import json

import requests


# change the url to dynamic instead of hard coding
# num_questions = 10
# category = requests.get('https://opentdb.com/api_category.php')
# category_d = {key: value for key, value in json.loads(category.text).items()}['trivia_categories']
# question_data = requests.get(f'https://opentdb.com/api.php?amount={num_questions}&category={category_id}')


class QuestionData:
    category_url = 'https://opentdb.com/api_category.php'

    def __init__(self, num_of_questions):
        self.num_of_questions = num_of_questions

    def get_category(self, cat_name):
        get_category = requests.get(self.category_url)
        category_dict = {key: value for key, value in json.loads(get_category.text).items()}['trivia_categories']
        for category in category_dict:
            category['name'].lower()
            if category['name'] == cat_name:
                return [category['id'] for category['name'] in category.items()]

    def get_data(self, name):
        cat_id = self.get_category(name)
        question_data = requests.get(f'https://opentdb.com/api.php?amount={self.num_of_questions}&category={cat_id[0]}')
        return question_data.json()


# data = QuestionData(10)
# print(data.get_data('Science: Mathematics'))
