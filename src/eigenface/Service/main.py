from flask import Flask

import sign_in
import sign_up

app = Flask(__name__)


@app.route("/signin")
def sign_in():
    return sign_in.sign_in()


@app.route("/signup")
def sign_up():
    sign_up.sign_up()
