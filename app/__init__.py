from flask import Flask
from flask_restful import Api
from .extensions import mongo,JSONEncoder

def create_app(config_object='product_info_flask_restful.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    app.json_encoder = JSONEncoder
    api = Api(app)
    from .api.Products import ProductList

    api.add_resource(ProductList, '/products')
    return app