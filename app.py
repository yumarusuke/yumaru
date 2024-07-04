from flask import Flask
haru = Flask(__name__)
@haru.route("/")
def hello():
    return "rei"
haru.run(host="0.0.0.0")