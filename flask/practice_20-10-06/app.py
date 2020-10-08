from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/href_1')
def href_1():
    return render_template("href_1.html")


if __name__ == '__main__':
    app.run(debug=True)