from flask import Flask, render_template
from flask.ext.script import Manager
from flask import Flask
app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello Everyone!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/index/')
def index():
    return render_template('/index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('/user.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)