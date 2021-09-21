from flask import Flask, render_template, request
import cv2 as cv
import numpy as np
import base64

import src.eigenface.Service.sign_up as signup
import src.eigenface.Service.sign_in as signin

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/shot", methods=['GET', 'POST'])
def shot():
    if request.method == 'POST':
        code = request.form['image']
        code = bytes(code[22:], 'ascii')
        image = base64.b64decode(code)  # decode base64 string representation of image from POST request
        writer = open('src/eigenface/Service/input.png', 'wb')
        writer.write(image)

        # cut face only and throw away background outside of the red frame
        image = np.array(cv.imread('src/eigenface/Service/input.png'))
        image = image[50:250, 120:280, :]  # the frame as shown in web.js and home.html
        cv.imwrite('src/eigenface/Service/input.png', image)
    return "done"


@app.route("/signin")
def sign_in():
    return "Sign in succeed" if signin.sign_in() else "Sign in failed"


@app.route("/signup")
def sign_up():
    try:
        signup.sign_up()
        return "Sign up success! Next time I'll remember you:)"
    except Exception as err:
        print(err)
        return "Error occurred when you signed up"


if __name__ == "__main__":
    app.run(debug=True)
