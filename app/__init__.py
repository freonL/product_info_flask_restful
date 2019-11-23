from flask import Flask
from flask_restful import Api
from .extensions import mongo,JSONEncoder

def create_app(config_object='app.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    app.json_encoder = JSONEncoder


    from .api.Products import bp as product_bp
    app.register_blueprint(product_bp)
    return app