from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, name, age):
        return {name:age}

    def post(self):
        return {"POST", "SUBHASISH"}


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")
if __name__ == "__main__":
    app.run(debug=True)
