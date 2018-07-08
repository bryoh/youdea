''' App for youdea '''
from flask import Flask, render_template 


youdea_app = Flask(__name__)


@youdea_app.route('/')
def index():
    """ methods and functions to manipulate the home page html"""
    return render_template('index.html')


if __name__ == "__main__":
    youdea_app.run(debug=True)
