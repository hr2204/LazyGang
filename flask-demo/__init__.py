from flask import Flask


def create_app(object_name, env="prod"):
    app = Flask(__name__,template_folder="templates",static_folder="static")
   
    return app


