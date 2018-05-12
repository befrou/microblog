from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Bruno Klein'}
    posts = [
        {
            'author': {'username' : 'Charles'},
            'body': 'Traveling to Canada!'
        },
        {
            'author': {'username' : 'Tom'},
            'body': 'Tips for tech interview!'
        }
    ]

    return render_template('index.html', title='home', user=user, posts=posts)


