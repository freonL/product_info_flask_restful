from flask import Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal
from app.extensions import mongo
from bson.objectid import ObjectId

product_fields = {
    '_id': fields.String,
    'title': fields.String,
    'category': fields.String,
    'price': fields.Float,
    'pic_url': fields.String
}

bp  = Blueprint('products', __name__)
api = Api(bp)

class ProductList(Resource):
    def get(self):
        collection = mongo.db.products
        resp = []
        for doc in collection.find():
            resp.append(doc)
        return  [marshal(task, product_fields) for task in resp]
    def post(self):
        pass


class Product(Resource):
    def get(self,id):
        collection = mongo.db.products
        resp = collection.find_one({ "_id": ObjectId(oid=str(id)) })
        return marshal(resp, product_fields)
    def patch(self,id):
        pass
    def delete(self,id):
        pass


api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<id>')