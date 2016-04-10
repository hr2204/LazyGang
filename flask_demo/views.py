from flask_demo import app
from flask import render_template

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    user = {'nickname': 'Lazy Gang'}  
    posts = [  
        { 
            'author': {'nickname': 'Little Horse'}, 
            'body': 'Rewriting Your Front End Every 6 Weeks' 
        },
        { 
            'author': {'nickname': 'Who'}, 
            'body': 'javascipt From Beginner to Loser' 
        },
        { 
            'author': {'nickname': 'Gig Ben'}, 
            'body': 'Writing code that Noboday Else Can Read' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)