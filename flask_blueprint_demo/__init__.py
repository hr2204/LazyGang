from flask import Flask

# app = Flask(__name__,template_folder="templates",static_folder="static")
app = Flask(__name__)

from controllers.main import main
app.register_blueprint(main)

from controllers.user import user
app.register_blueprint(user)