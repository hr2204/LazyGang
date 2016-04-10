from flask import Flask, render_template

app = Flask(__name__, template_folder="flask_demo/templates",static_folder="flask_demo/static")

@app.route("/")
@app.route("/index")
def hello():
    return "Hello World!!!!"

@app.route("/rendhtml", methods=["GET"])
def rendhtml():
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


if __name__ == "__main__":
    app.run(debug=True, port=9527)