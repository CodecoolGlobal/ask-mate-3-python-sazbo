import util


DATA_PATH = 'model/data/question.csv'
DATA_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

questions = {}

empty_question_object = {
    'id': -1,
    'submission_time': 0,
    'view_number': 0,
    'vote_number': 0,
    'title': '',
    'message': '',
    'image': ''
}


def load_questions():
    global questions
    global DATA_PATH
    global DATA_HEADERS

    questions = util.load_csv_data(DATA_PATH, DATA_HEADERS)

    for question_id in questions.keys():
        question_timestamp = questions[question_id]['submission_time']
        questions[question_id]['submission_datetime'] = util.time_kekw(question_timestamp)
        questions[question_id]['image_class'] = 'hidden' if questions[question_id]['image'] == '' else ''


def save_questions():
    global questions
    global DATA_PATH
    global DATA_HEADERS

    util.write_csv_data(DATA_PATH, DATA_HEADERS, questions)

    load_questions()


def get_questions():
    global questions
    return questions


def get_question(question_id):
    global questions
    return questions[int(question_id)]


def add_question(question_data):
    global questions

    new_question_data = empty_question_object.copy()

    new_question_id = get_id()

    new_question_data['id'] = new_question_id
    new_question_data['title'] = question_data['title']
    new_question_data['message'] = question_data['message'].replace('\n', '<br>')
    new_question_data['submission_time'] = int(util.date_time())
    new_question_data['image'] = question_data['image']

    questions[new_question_id] = new_question_data

    save_questions()


def edit_question(question_id, question_data):
    global questions

    new_question_data = questions[int(question_id)].copy()

    new_question_data['title'] = question_data['title']
    new_question_data['message'] = question_data['message'].replace('\n', '<br>')
    # todo: image

    questions[int(question_id)] = new_question_data

    save_questions()


def delete_question(question_id):
    global questions

    questions.pop(int(question_id))
    save_questions()


def vote_question(question_id, vote):
    global questions

    old = questions[int(question_id)]['vote_number']
    questions[int(question_id)]['vote_number'] = old + int(vote)
    save_questions()


def get_id():
    global questions

    if len(questions.keys()) == 0:
        return 0

    id_list = questions.keys()

    return int(max(id_list)) + 1
