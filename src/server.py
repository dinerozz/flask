import os
import secrets
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

flag = os.getenv("FLAG") or 'f13{fake_flag}'
users = {
    'userid': 1,
    'username': 'admin',
    'password': secrets.token_hex(16)
}


@app.route('/api/users/', defaults={'userid': None, 'username': None}, methods=['POST'])
@app.route('/api/users/<userid>/<username>', methods=['POST'])
def auth_user(userid, username):
    if userid is None:
        answer_from_server = ('ok', jsonify(users))
    else:
        if str(users['userid']) == userid:
            print(users.get('password'))
            password = request.args.get('password')

            if users['username'] == username and users['password'] == password:
                answer_from_server = ('ok', flag)
            else:
                answer_from_server = ('error', 'Login or password incorrect')
        else:
            answer_from_server = ('error', 'User not found')

    if str(request.args.get('show_response')) == '1':
        return answer_from_server[1]
    else:
        return answer_from_server[0]


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001, debug=False)
