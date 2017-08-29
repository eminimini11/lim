from flask import Flask, render_template, request
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager


class NameForm(Form):
    name = StringField('What is you name?', validators=[Required()])
    subnit = SubmitField('Submit')


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form
    return render_template('index.html', result=result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/user/hello')
def hello():
    user_name = request.args.get('user_name', '')
    user_name = user_name + ", Welcom"
    return render_template('hello.html', user_name=user_name)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


if __name__ == '__main__':
    app.run(debug=True)
