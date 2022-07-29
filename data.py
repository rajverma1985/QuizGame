import json
import requests


class QuestionData:
    category_url = 'https://opentdb.com/api_category.php'
    cat_name = []

    def __init__(self, num_of_questions=10, cat_type='boolean'):
        self.num_of_questions = num_of_questions
        self.cat_type = cat_type

    def get_category(self):
        get_category = requests.get(self.category_url)
        category_dict = {key: value for key, value in json.loads(get_category.text).items()}['trivia_categories']
        return category_dict

    def get_data(self):
        input_cat = input(f"Please choose a category: {self.get_category()}\n")
        for cat in self.get_category():
            if cat['name'].lower() == input_cat.lower():
                cat_id = cat['id']
        question_data = requests.get(f'https://opentdb.com/api.php?amount={self.num_of_questions}'
                                     f'&category={cat_id}&type={self.cat_type}')
        return question_data.json()['results']
