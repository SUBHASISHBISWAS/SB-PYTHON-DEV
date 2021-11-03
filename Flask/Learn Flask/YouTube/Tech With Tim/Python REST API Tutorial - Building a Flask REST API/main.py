from flask import Flask,request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Video(Resource):
    def get(self, name, age):
        return {name:age}

    def post(self):
        return {"POST", "SUBHASISH"}

    def put(self,video_id):
        print(request.form['likes'])
        return {}


api.add_resource(Video, "/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
