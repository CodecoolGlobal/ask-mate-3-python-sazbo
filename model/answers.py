import util


DATA_PATH = 'model/data/answer.csv'
DATA_HEADERS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

answers = {}

empty_answer_object = {
    'id': -1,
    'submission_time': 0,
    'vote_number': 0,
    'question_id': -1,
    'message': '',
    'image': ''
}


def load_answers():
    global answers
    global DATA_PATH
    global DATA_HEADERS

    answers = util.load_csv_data(DATA_PATH, DATA_HEADERS)

    for answer_id in answers.keys():
        answer_timestamp = answers[answer_id]['submission_time']
        answers[answer_id]['submission_datetime'] = util.time_kekw(answer_timestamp)


def get_answers():
    global answers
    return answers


def save_answers():
    global answers
    global DATA_PATH
    global DATA_HEADERS

    util.write_csv_data(DATA_PATH, DATA_HEADERS, answers)

    load_answers()


def get_question_answers(question_id):
    global answers
    question_answers = []

    for answer_id in answers.keys():
        if int(answers[int(answer_id)]['question_id']) == int(question_id):
            question_answers.append(answers[int(answer_id)])

    return question_answers


def get_answer(answer_id):
    global answers
    return answers[int(answer_id)]


def add_answer(question_id, answer_data):
    global answers

    new_answer_data = empty_answer_object.copy()

    new_answer_id = get_id()

    new_answer_data['id'] = new_answer_id
    new_answer_data['question_id'] = question_id
    new_answer_data['message'] = answer_data['message'].replace('\n', '<br>')
    new_answer_data['submission_time'] = int(util.date_time())
    # todo: image

    answers[new_answer_id] = new_answer_data

    save_answers()


def edit_answer(answer_id, answer_data):
    global answers

    new_answer_data = get_answer(int(answer_id)).copy()

    new_answer_data['message'] = answer_data['message'].replace('\n', '<br>')
    # todo: image

    answers[answer_id] = new_answer_data

    save_answers()


def delete_answer(answer_id):
    global answers

    answers.pop(int(answer_id))

    save_answers()


def delete_question_answers(question_id):
    global answers

    new_answers = {}

    for answer_id in answers.keys():
        if answers[answer_id]['question_id'] == question_id:
            continue

        new_answers[answer_id] = answers[answer_id]

    answers = new_answers

    save_answers()


def vote_answer(answer_id, vote):
    global answers

    old = int(answers[int(answer_id)]['vote_number'])
    answers[int(answer_id)]['vote_number'] = old + int(vote)

    save_answers()


def get_id():
    global answers
    id_list = answers.keys()

    return int(max(id_list))+1


