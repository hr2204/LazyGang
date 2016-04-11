from flask import Flask

def create_app(object_name, env="prod"):
    
    app = Flask(__name__,template_folder="templates",static_folder="static", static_url_path="/")
    
    # app.config.from_object(object_name)
    # app.config['ENV'] = env

    # register our blueprints
    from controllers.main import main
    app.register_blueprint(main)

    from controllers.user import user
    app.register_blueprint(user)

    return app