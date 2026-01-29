import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():

    username = os.getenv("USERNAME")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    print(username, email, password)

    return f'<h1>Hello, World!{username}<br>{email}<br>{password}</h1>', 200


@app.route('/healthz')
def healthz():
    return 'OK', 200

def status_404(error):
    return '<h1>404</h1>', 404

if __name__ == "__main__":
    app.run(debug=True)