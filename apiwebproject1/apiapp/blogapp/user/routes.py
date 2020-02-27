from flask_restful import Resource
from blogapp.app import db
from .models import User
from flask import jsonify,request

class UserApi(Resource):

    def get(self,username):
        user=User.query.filter_by(username=username).first()
        if user:
            return jsonify({"username":user.username,"email":user.email})
        else:
            return jsonify({"msg":"no user found"})

    def post(self,username):
        request_data=request.get_json()
        user=User(email=request_data['email'],password=request_data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"username":user.username})
