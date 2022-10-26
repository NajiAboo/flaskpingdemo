from flask import Flask
from flask_ngrok import run_with_ngrok
from requests import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def ping():
    print(request)
    print("ping triggered !!!!")
    return "success!!"

if __name__ == '__main__':
    app.run()

