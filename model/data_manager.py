from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor
import model.database_common as database_common

# @database_common.connection_handler
# def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:
#     query = f"SELECT first_name, last_name, city " \
#             f"FROM mentor " \
#             f"WHERE last_name LIKE '%{last_name}%' " \
#             f"ORDER BY first_name;"
#     cursor.execute(query)
#     return cursor.fetchall()


# QUESTION FUNCTIONS

@database_common.connection_handler
def list_question_with_tag(cursor: RealDictCursor) -> list:
    query = f"SELECT question_id, tag_id, title, tag.name, view_number, vote_number, message, image, submission_time " \
            f"FROM question_tag " \
            f"LEFT JOIN question q on q.id = question_tag.question_id " \
            f"LEFT JOIN tag on question_tag.tag_id = tag.id;"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def list_question_with_tag_xd(cursor: RealDictCursor, tag_name) -> list:
    query = f"SELECT question_id, tag_id, title, tag.name, view_number, vote_number, message, image, submission_time " \
            f"FROM question_tag " \
            f"LEFT JOIN question q on q.id = question_tag.question_id " \
            f"LEFT JOIN tag on question_tag.tag_id = tag.id " \
            f"WHERE tag.name = '{tag_name}';"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def add_question(cursor: RealDictCursor, title, message, image, user) -> list:
    query = f"INSERT INTO question(submission_time, view_number, vote_number, title, message, image, users) " \
            f"VALUES (CURRENT_TIMESTAMP, 0, 0, '{title}', '{message}', '{image}', '{user}') RETURNING id;"
    cursor.execute(query)

    x = cursor.fetchone()
    y = x['id']
    return y


@database_common.connection_handler
def add_tag(cursor: RealDictCursor, current_id, tag_id) -> list:

    tag_query = f"INSERT INTO question_tag(question_id, tag_id) " \
                f"VALUES ({current_id}, {tag_id});"
    cursor.execute(tag_query)


@database_common.connection_handler
def edit_question(cursor: RealDictCursor, new_message, new_image, current_id: int) -> list:
    query = f"UPDATE question SET submission_time = CURRENT_TIMESTAMP message = '{new_message}', image = '{new_image}' WHERE id = {current_id};"
    cursor.execute(query)


@database_common.connection_handler
def delete_question(cursor: RealDictCursor, current_id: int) -> list:
    query = f"DELETE FROM answer WHERE question_id = {current_id};" \
            f"DELETE FROM question_tag WHERE question_id = {current_id};"\
            f"DELETE FROM question WHERE id = {current_id};"
    cursor.execute(query)


@database_common.connection_handler
def list_table(cursor: RealDictCursor, table_name: str) -> list:
    query = f"SELECT * " \
            f"FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchall()


# ANSWER FUNCTIONS


@database_common.connection_handler
def add_answer(cursor: RealDictCursor, question_id: int, message, image, user) -> list:
    query = f"INSERT INTO answer (submission_time, vote_number, question_id, message, image, users)" \
            f"VALUES (CURRENT_TIMESTAMP, 0, {question_id}, '{message}', '{image}', '{user}');"
    cursor.execute(query)


@database_common.connection_handler
def edit_answer(cursor: RealDictCursor, new_message, new_image, current_id: int) -> list:
    query = f"UPDATE answer SET submission_time = CURRENT_TIMESTAMP message = '{new_message}', image = '{new_image}' WHERE id = {current_id};"
    cursor.execute(query)


@database_common.connection_handler
def delete_answer(cursor: RealDictCursor, current_id: int) -> list:
    query = '''DELETE FROM answer WHERE id = %(current_id)s;
    '''
    cursor.execute(query, {'current_id': current_id})


@database_common.connection_handler
def list_answer(cursor: RealDictCursor) -> list:
    query = "SELECT submission_time, vote_number, message, image, users FROM answer"
    cursor.execute(query)
    return cursor.fetchall()


# VOTE


@database_common.connection_handler
def votes(cursor: RealDictCursor, table, current_id: int, vote: int) -> list:

    query = f'UPDATE {table} SET vote_number = (vote_number + {vote}) WHERE id = {current_id};'
    cursor.execute(query)

# GET DATA


@database_common.connection_handler
def get_data_by_id(cursor: RealDictCursor, question_id: int, table_name: str) -> list:
    if table_name == 'question':
        query_id = 'id'
    else:
        query_id = 'question_id'
    query = f"SELECT * FROM {table_name} WHERE {query_id} = {question_id};"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_question_id_by_answer_id(cursor: RealDictCursor, answer_id: int) -> list:
    query = f"SELECT question_id FROM answer WHERE id = {answer_id};"
    cursor.execute(query)
    result = cursor.fetchall()

    return result[0]['question_id']


# @database_common.connection_handler
# def get_answers_data(cursor: RealDictCursor, question_id: int) -> list:
#     query = f"SELECT * FROM answer WHERE question_id = {question_id};"
#     cursor.execute(query)
#     return cursor.fetchall()


# sort query

@database_common.connection_handler
def sort(cursor: RealDictCursor, sort_type: str, sort_row: str) -> list:
    query = f"SELECT question_id, tag_id, title, tag.name, view_number, vote_number, message, image, submission_time " \
            f"FROM question_tag " \
            f"LEFT JOIN question q on q.id = question_tag.question_id " \
            f"LEFT JOIN tag on question_tag.tag_id = tag.id " \
            f"ORDER BY {sort_row} {sort_type};"
    cursor.execute(query)
    return cursor.fetchall()


# USER DATAS


@database_common.connection_handler
def add_user(cursor: RealDictCursor, name, password: str):
    query = f"INSERT INTO user_data (user_name, user_password) " \
            f"VALUES ('{name}', '{password}');"
    cursor.execute(query)


@database_common.connection_handler
def list_user(cursor: RealDictCursor) -> list:
    query = f"SELECT user_name FROM user_data;"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def list_passwords(cursor: RealDictCursor) -> list:
    query = f"SELECT user_password FROM user_data;"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_user_pw(cursor: RealDictCursor, name: str) -> list:
    query = f"SELECT user_password FROM user_data WHERE user_name LIKE '{name}';"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def list_question_with_user(cursor: RealDictCursor, user) -> list:
    query = f"SELECT * " \
            f"FROM question " \
            f"WHERE users like '{user}';"
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def list_answer_with_user(cursor: RealDictCursor, user) -> list:
    query = f"SELECT * " \
            f"FROM answer " \
            f"WHERE users like '{user}';"
    cursor.execute(query)
    return cursor.fetchall()
