from sanic import response, Sanic
from sanic.request import Request
import ujson as json

app = Sanic()

for k, v in app.config.items():
    print(k, v)

track_resp = json.load(open('../tracks.json'))

@app.route('/<number:int>')
async def index(request, number=1):
    return response.html("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.route('/', methods=['POST'])
async def post(request):
    data = request.form
    number = data['fib'][0]
    return response.html("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.route('/tracks/', methods=['POST'])
async def post_tracks(request: Request):
    tracks = request.json
    if tracks is not None:
        track_type = str(type(tracks))
        return response.html("We got some json " + track_type)
    else:
        return response.html("we did not get some json: " + str(request.content_type))

    # return {'cam_track_count': len(tracks['camera_tracks'])}


@app.route('/tracks/', methods=['GET'])
async def get_tracks(_):
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
