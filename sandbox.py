import json, requests

num_questions = 10
# category_url = 'https://opentdb.com/api_category.php'
# get_category = requests.get(category_url)
# category_dict = {key: value for key, value in json.loads(get_category.text).items()}['trivia_categories']


cat = [{'id': 9, 'name': 'General Knowledge'}, {'id': 10, 'name': 'Entertainment: Books'},
       {'id': 11, 'name': 'Entertainment: Film'}, {'id': 12, 'name': 'Entertainment: Music'},
       {'id': 13, 'name': 'Entertainment: Musicals & Theatres'}, {'id': 14, 'name': 'Entertainment: Television'},
       {'id': 15, 'name': 'Entertainment: Video Games'}, {'id': 16, 'name': 'Entertainment: Board Games'},
       {'id': 17, 'name': 'Science & Nature'}, {'id': 18, 'name': 'Science: Computers'},
       {'id': 19, 'name': 'Science: Mathematics'}, {'id': 20, 'name': 'Mythology'}, {'id': 21, 'name': 'Sports'},
       {'id': 22, 'name': 'Geography'}, {'id': 23, 'name': 'History'}, {'id': 24, 'name': 'Politics'},
       {'id': 25, 'name': 'Art'}, {'id': 26, 'name': 'Celebrities'}, {'id': 27, 'name': 'Animals'},
       {'id': 28, 'name': 'Vehicles'}, {'id': 29, 'name': 'Entertainment: Comics'},
       {'id': 30, 'name': 'Science: Gadgets'}, {'id': 31, 'name': 'Entertainment: Japanese Anime & Manga'},
       {'id': 32, 'name': 'Entertainment: Cartoon & Animations'}]

# var = input("Type the name : ").lower()


def idn(name):
    for n in cat:
        n['name'].lower()
        if n['name'] == name:
            id = [n['id'] for n['name'] in n.items()]
    return id

cat_input =input("Choose a category: ")

cat_id=idn(cat_input)

question_data = requests.get(f'https://opentdb.com/api.php?amount={num_questions}&category={cat_id[0]}')
print(question_data.json())