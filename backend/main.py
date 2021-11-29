import pymysql
from app import app
from database import mysql
from flask import jsonify
from flask import flash, request
from flask_cors import CORS, cross_origin
import json
# from flask import Flask

# https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask

# app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/users', methods=['GET'])
@cross_origin(supports_credentials=True)
def users():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        if request.method == 'GET':
            sort_str = range_str = filter_str = ''
            sort_list = range_list = []
            filter_dict = {}
            sort_str = request.args.get('sort')  # filter or range or sort
            if sort_str:
                sort_list = json.loads(sort_str)
            range_str = request.args.get('range')  # filter or range or sort

            if range_str:
                range_list = json.loads(range_str)

            filter_str = request.args.get('filter')  # filter or range or sort
            if filter_str:
                filter_dict = json.loads(filter_str)
            offset = 0
            if range_list:
                offset = int(range_list[1]) - int(range_list[0]) + 1

            cur.execute(f"SELECT COUNT(*) AS count FROM users;")
            row_count = cur.fetchall()[0]['count']
            # cur.execute(f"SELECT * FROM users;")
            if filter_dict and not range_list and not sort_list:
                # print(filter_dict['id'][0])
                # print(type(filter_dict))
                # print(range_list)
                # print(sort_list)
                cur.execute(
                    f"SELECT * FROM users WHERE id = {filter_dict['id'][0]} ;")
            elif range_list and sort_list and filter_dict:
                if 'q' in filter_dict.keys():
                    cur.execute(
                        f"SELECT * FROM users WHERE id like '%{filter_dict['q']}%' or name like '%{filter_dict['q']}%' or email like '%{filter_dict['q']}%'  ORDER BY {sort_list[0]} {sort_list[1]} LIMIT {range_list[0]}, {offset};")
                else:
                    cur.execute(
                        f"SELECT * FROM users WHERE id = {filter_dict['id']}  ORDER BY {sort_list[0]} {sort_list[1]} LIMIT {range_list[0]}, {offset};")
            elif range_list and sort_list:
                cur.execute(
                    f"SELECT * FROM users ORDER BY {sort_list[0]} {sort_list[1]} LIMIT {range_list[0]}, {offset};")
            else:
                cur.execute(f"SELECT * FROM users;")

            rows = cur.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            response.headers["Content-Range"] = f"users 0-{offset}/{row_count}"
            # response.headers["Access-Control-Expose-Headers"] = '*';
            response.headers["Access-Control-Expose-Headers"] = 'Content-Range'
            return response

    except Exception as e:
        print('Exception', e)
    finally:
        cur.close()
        conn.close()


# @app.route('/users/<user_id>', methods=['GET', 'DELETE'])
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        # if request.method == 'GET':
        #     cur.execute(f"SELECT * FROM users WHERE id = {user_id};")
        #     rows = cur.fetchall()
        #     response = jsonify(rows)
        #     response.status_code = 200
        #     response.headers["Content-Range"] = "posts 0-20/20"
        #     # response.headers['Access-Control-Allow-Origin'] = '*'
        #     return response

        if request.method == 'DELETE':
            cur.execute(f"DELETE FROM users WHERE id = '{user_id}';")
            conn.commit()
            rows = cur.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response

        # if request.method == 'POST':
        #     cur.execute(f"INSERT INTO users(id, email, hashed_password, is_active) values ( {user_id}, 'test{user_id}@gmail.com', 'hash',1)")
        #     conn.commit()
        #     rows=cur.fetchall()
        #     response=jsonify(rows)
        #     response.status_code=200
        #     return response

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
@app.route('/users', methods=['DELETE'])
def delete_users():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        filter_str = request.args.get('filter')  # filter or range or sort
        if filter_str:
            filter_dict = json.loads(filter_str)
        
        if request.method == 'DELETE':
            for id in filter_dict["id"]:
                cur.execute(f"DELETE FROM users WHERE id = '{id}';")
                conn.commit()
            rows = cur.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            return response

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


# @app.route('/users', methods=['GET', 'POST'])
@app.route('/users', methods=['POST'])
def create_user():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        # form = request.form
        # user_id = request.form['id']
        # user_name = request.form['name']
        # user_email = request.form['email']
        content = request.get_json()
        if request.method == 'POST':
            cur.execute(
                f"INSERT INTO users(id, name, email) values ( '{content['id']}', '{content['name']}', '{content['email']}')")
            # cur.execute(f"INSERT INTO users(id, name, email) values ( '{user_id}', '{user_name}', '{user_email}')")

            conn.commit()

            freqs = {
                'id': f'{content["id"]}',
            }
            return jsonify(freqs)

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


# @app.route('/users/<user_id>', methods=['GET', 'PUT'])
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        content = request.get_json()

        # if request.method == 'GET':
        #     cur.execute(f"SELECT * FROM users WHERE id = {user_id};")
        #     rows = cur.fetchall()
        #     response = jsonify(rows)
        #     response.status_code = 200
        #     response.headers["Content-Range"] = "posts 0-20/20"
        #     # response.headers['Access-Control-Allow-Origin'] = '*'
        #     return response
        if request.method == 'PUT':
            # cur.execute(
            #     f"UPDATE users SET name ='{content['name']}', email = '{content['email']}' WHERE id = '{content['id']}'")
            cur.execute(
                f"UPDATE users SET name ='{content['name']}', email = '{content['email']}' WHERE id = '{user_id}'")

            conn.commit()
            # return content['id']
            cur.execute(
                f"SELECT * FROM users WHERE id = {user_id};")
            rows = cur.fetchall()
            response = jsonify(rows)
            # return user_id
            return response

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # if user_id == "undefined":
    #     return ('', 204)
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)

        # content = request.get_json()

        if request.method == 'GET':
            cur.execute(f"SELECT * FROM users WHERE id = '{user_id}';")
            rows = cur.fetchall()
            response = jsonify(rows)
            response.status_code = 200
            # response.headers["Content-Range"] = "posts 0-20/20"
            # response.headers['Access-Control-Allow-Origin'] = '*'
            return response

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    app.run()
