from flask import Flask, request
import ujson as json

app = Flask(__name__)
big_track_resp = json.load(open('data/tracks.json'))
smaller_track_resp = json.load(open('data/smaller_tracks.json'))


@app.route('/<int:number>')
def index(number=1):
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


@app.route('/', methods=['POST'])
def post():
    number = request.form['fib']
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


@app.route('/smaller-tracks', methods=['GET'])
def get_smaller_tracks():
    return smaller_track_resp


@app.route('/bigger-tracks', methods=['GET'])
def get_bigger_tracks():
    return big_track_resp


@app.route('/tracks', methods=['POST'])
def post_tracks():
    tracks = request.get_json()
    return {'cam_track_count': len(tracks['camera_tracks'])}


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
