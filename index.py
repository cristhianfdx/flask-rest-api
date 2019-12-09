from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__)
# Api
api = Api(app)
ma = Marshmallow(app)
# Db Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/flask_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class User(db.Model):

    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<User %r>' % self.name

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'created_at')        

# Init Schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)

# Routes

class ApiIndex(Resource):
    def get(self):
        return {"welcome" : "This is an RESTful API"}

api.add_resource(ApiIndex, '/api')


class SimpleUsers(Resource):
    # All Users
    def get(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result.data)
    
    # Create User
    def post(self):
        data = request.get_json()
        user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {
            "status" :True,
            "message" : "User saved succesfully"
        }, 201


class ParamsUsers(Resource):
    # Get One User
    def get(self, user_id):
        # Search the user
        user = User.query.get(user_id)
        one_user = User.query.get(user_id)
        result = user_schema.dump(one_user)
        return jsonify(result.data)

    def put(self, user_id):
        data = request.get_json()
        # Search the user to update
        user = User.query.get(user_id)

        user.name = data['name']
        user.email = data['email']
        user.password = data['password']

        db.session.commit()

        return {
            "status" :True,
            "message" : "User updated succesfully"
        }

    def delete(self, user_id):
        # Search the user to delete
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()   

        return {
            "status" :True,
            "message" : "User removed succesfully"
        }
    

api.add_resource(ParamsUsers, '/api/users/<string:user_id>')
api.add_resource(SimpleUsers, '/api/users')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
