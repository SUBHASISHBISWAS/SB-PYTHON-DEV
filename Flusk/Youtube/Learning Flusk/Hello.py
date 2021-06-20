from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/Hello/<name>')
def hello_world_name(name):
    return 'Hello %s!' % name


@app.route('/blog/<int:postId>')
def show_blog(postId):
    return 'Hello World : %d' % postId


@app.route('/blog/<float:revNo>')
def revision(revNo):
    return 'Hello World : %f' % revNo


if __name__ == '__main__':
    app.run()
