from flask_restful import Resource, reqparse, fields, marshal
from product_info_flask_restful.extensions import mongo
from bson.objectid import ObjectId

product_fields = {
    'title': fields.String,
    'category': fields.String,
    'price': fields.Float,
    'pic_url': fields.String
}

class ProductList(Resource):
    def get(self):
        collection = mongo.db.products
        resp = []
        for doc in collection.find():
            resp.append(doc)
        return  [marshal(task, product_fields) for task in resp]
    def post(self):
        pass
