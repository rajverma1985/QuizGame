import json
import requests

# example URL1 : https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean
# example URL2: https://opentdb.com/api.php?amount=10&category=11&difficulty=hard&type=multiple


params = {"amount": 10,
          "category": 9,
          "difficulty": 'medium',
          "type": 'boolean'
          }


class QuestionData:
    category_url = 'https://opentdb.com/api_category.php'
    data_url = 'https://opentdb.com/api.php'
    cat_name = []

    def __init__(self, num_of_questions=10, cat_type='boolean'):
        self.num_of_questions = num_of_questions
        self.cat_type = cat_type

    def get_category(self):
        get_category = requests.get(self.category_url, params=params)
        get_category.raise_for_status()
        category_dict = {key: value for key, value in json.loads(get_category.text).items()}['trivia_categories']
        return category_dict

    def get_data(self, input_cat):
        for cat in self.get_category():
            if cat['name'].lower() == input_cat.lower():
                question_data = requests.get(self.data_url, params=params)

                # requests.get(f"{self.data_url}?amount={self.num_of_questions}"
                #                              f"&category={cat['id']}&type={self.cat_type}")
        return question_data.json()
