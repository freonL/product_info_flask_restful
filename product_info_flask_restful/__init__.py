from flask import Flask
from .extensions import mongo,JSONEncoder

def create_app(config_object='product_info_flask_restful.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    app.json_encoder = JSONEncoder

    return app