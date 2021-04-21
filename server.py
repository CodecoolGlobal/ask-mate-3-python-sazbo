import os
from flask import Flask, render_template, redirect, request, url_for, session, escape
from werkzeug.utils import secure_filename
import model.data_manager as data_manager
import util
import model.password_check as password_check

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def main_page():
    sort = request.args.get('input_sort')
    sort_type = request.args.get('input_sort_type')
    if sort is None or sort_type is None:
        questions = data_manager.list_question_with_tag()
    else:
        questions = data_manager.sort(sort, sort_type)
    answers = data_manager.list_table('answer')

    return render_template("/main.html", questions=questions, answers=answers)


# TAG SITE

@app.route("/tag/<tag_name>")
def tag_site(tag_name):
    questions = data_manager.list_question_with_tag_xd(tag_name)
    answers = data_manager.list_table('answer')

    return render_template("/tag.html", questions=questions, answers=answers)


# QUESTIONS


@app.route("/question/<question_id>")
def view_question(question_id):
    question_data = data_manager.get_data_by_id(question_id, 'question')
    question_answers = data_manager.get_data_by_id(question_id, 'answer')

    return render_template("question.html", questions=question_data, answers=question_answers)


@app.route("/add-question", methods=["POST"])
def add_question():
    if request.method == "POST":
        title = request.form.get('question-title')
        message = request.form.get('question-message')
        tag_id = request.form.get('question-tag')
        image = ''

        if 'question-image' in request.files:
            file = request.files['question-image']
            if file.filename != '' and file and util.allowed_file(file.filename, ALLOWED_EXTENSIONS):
                image = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], image))

        current_id = data_manager.add_question(title, message, image)

        data_manager.add_tag(current_id, tag_id)

    return redirect("/")


# //EDIT QUESTION
# @app.route("/question/<question_id>/edit", methods=["POST"])
# def edit_question(question_id, request_values):
#     question_data = {}
#     title = request_values["question-title"]
#     message = request_values["question-message"]
#     question_data["title"] = title
#     question_data["message"] = message
#
#     questions.edit_question(question_id, question_data)
#
#     return util.question_url(question_id)


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    data_manager.delete_question(question_id)

    return redirect("/")


@app.route("/vote-question/<question_id>", methods=["GET"])
def question_vote(question_id):
    if request.method == "GET":
        vote = request.args["vote"]
        data_manager.votes('question', question_id, vote)

    return redirect("/question/" + question_id)


# ANSWERS


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def answer_question(question_id):
    if request.method == "POST":
        message = request.form.get('answer-message')
        image = ''

        if 'answer-image' in request.files:
            file = request.files['answer-image']
            if file.filename != '' and file and util.allowed_file(file.filename, ALLOWED_EXTENSIONS):
                image = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], image))

        data_manager.add_answer(question_id, message, image)
        return redirect("/question/" + question_id)


# EDIT ANSWER
# @app.route('/answer/<answer_id>/edit-answer', methods=['POST'])
# def edit_answer(answer_id, request_values):
#     # answer_data = {}
#     #
#     # message = request_values["answer-message"]
#     # answer_data['message'] = message
#     #
#     # answers.edit_answer(answer_id, answer_data)
#     #
#     # answer_data = answers.get_answer(answer_id)
#     # question_id = answer_data['question_id']
#
#     return util.question_url(question_id)


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    question_id = data_manager.get_question_id_by_answer_id(answer_id)
    data_manager.delete_answer(answer_id)

    return redirect("/question/" + str(question_id))


@app.route("/vote-answer/<answer_id>", methods=["GET"])
def answer_vote(answer_id):
    if request.method == "GET":
        q_id = data_manager.get_question_id_by_answer_id(answer_id)
        vote = request.args["vote"]
        data_manager.votes('answer', answer_id, vote)

        return redirect("/question/" + str(q_id))


# USER LOG/CREATE


# @app.route('/')
# def index():
#     if 'username' in session:
#         text = 'Logged in as %s' % escape(session['username'])
#         return render_template("index.html", text=text)
#     text = 'You are not logged in, please Login!'
#     return render_template('login.html', text=text)


@app.route('/log', methods=['GET', 'POST'])
def log():
    return render_template("login.html")


@app.route('/create-us', methods=['GET', 'POST'])
def create_us():
    return render_template("create-user.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        current_password = request.form['password']
        print(current_password)
        user_data = data_manager.list_user()
        users = []
        n = 0
        for i in user_data:
            user_dat = user_data[n]
            users.append(user_dat['user_name'])
            n += 1
        user_password = data_manager.get_user_pw(session['username'])
        user_pw = user_password[0]
        check = password_check.verify_password(current_password, user_pw['user_password'])
        if session['username'] in users:
            if check:
                return main_page()

            else:
                return render_template('login.html')


@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        session['username'] = request.form['username']
        user_name = request.form['username']
        user_password = request.form['password']
        hashed_password = password_check.hash_password(user_password)
        user_data = data_manager.list_user()
        users = []
        n = 0
        for i in user_data:
            user_dat = user_data[n]
            users.append(user_dat['user_name'])
            n += 1
        if user_name not in users:
            data_manager.add_user(user_name, hashed_password)
            return render_template('login.html', text="Successful user creation!")
        else:
            return render_template('login.html', text="This user created before pls try again!")


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
