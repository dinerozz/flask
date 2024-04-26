import requests
import secrets
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		
		response = requests.post(f"http://localhost:3001/api/users/1/{username}?password={password}&show_response=1")
		return response.text
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug = False)