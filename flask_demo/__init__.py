from flask import Flask

# app = Flask(__name__,template_folder="templates",static_folder="static")
app = Flask(__name__)

from flask_demo import views