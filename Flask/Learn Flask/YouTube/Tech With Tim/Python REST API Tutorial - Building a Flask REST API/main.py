from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return  f"Video(name={name},views={views},likes={likes})"


# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name os the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views os the Video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes os the Video", required=True)

videos = {}


def abort_if_video_does_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video id not Exist")


def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, message="Video id already Exist")


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        #abort_if_video_does_not_exist(video_id)
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video id")
        return result
        # return videos[video_id]

    def post(self):
        return {"POST", "SUBHASISH"}

    def put(self, video_id):
        #abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(404, message="Video Id Taken....")
        video = VideoModel(id=video_id,
                           name=args['name'],
                           views=args['views'],
                           likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        # videos[video_id] = args
        return video, 201

    def delete(self, video_id):
        abort_if_video_does_not_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
