from flask import Flask, render_template
from flask_script import Manager
# from flask import Flask


app = Flask(__name__)
manager = Manager(app)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hells, %s!<h1/>' % name


@app.route('/index/')
def index():
    return render_template('/index.html')


@app.route('/user/hello')
def hello():
    user_name = user + ", Welcom"
    return render_template('hello.html', user_name=user_name)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


if __name__ == '__main__':
    app.run(debug=True)
