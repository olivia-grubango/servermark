from blacksheep import server, Request
from blacksheep.server.responses import html, json as json_resp
import ujson as json

app = server.Application()
track_resp = json.load(open('../tracks.json'))


@app.router.get('/:number')
async def fib_get(request: Request):
    number = request.route_values.get('number') or 10
    return html("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.router.post('/')
async def fib_post(request: Request):
    #data = request.f
    number = 10
    return html("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.router.post('/tracks')
async def post_tracks(request: Request):
    tracks = await request.json()
    return json_resp({'cam_track_count': len(tracks['camera_tracks'])})


@app.router.get('/tracks')
async def get_tracks():
    return json_resp(track_resp)


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)
