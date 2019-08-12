from flask import Flask
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "fluffer"
    },
    {
        "name": "Shubert",
        "age": 102,
        "occupation": "wanker"
    },
    {
        "name": "Jass",
        "age": 27,
        "occupation": "bunny"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
    def put(self, name):
        return "Not implemented", 404
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

@app.route('/userlist')
def userlist():
    return str(users), 200


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
