from flask import Flask
from snakeeyes.blueprints.page import page

def create_app():
    """
    Create a Flask application using the app factory pattern.
    
    :return: Flask app
    """

    # Since version 0.8 Flask provides one more configuration option – instance folders. 
    # The instance folder is designed not to be under source control and 
    # could store sensitive information. This instance folder should be directly 
    # deployed on the production server. for example: 
    # app = Flask(__name__, instance_relative_config=True) 
    # app.config.from_pyfile('flask.cfg')
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)
    return app





