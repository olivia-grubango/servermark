from quart import Quart, request
import ujson as json

app = Quart(__name__)
track_resp = json.load(open('../tracks.json'))


@app.route('/<int:number>')
async def index(number=1):
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


@app.route('/', methods=['POST'])
async def post():
    data = await request.form
    number = data['fib']
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


@app.route('/tracks/', methods=['POST'])
async def post_tracks():
    tracks = await request.get_json()
    return {'cam_track_count': len(tracks['camera_tracks'])}


@app.route('/tracks/', methods=['GET'])
async def get_tracks():
    return track_resp


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
