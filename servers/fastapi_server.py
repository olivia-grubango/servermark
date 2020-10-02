from fastapi import FastAPI, Form, Request
import ujson as json

app = FastAPI()
big_track_resp = json.load(open('data/tracks.json'))
smaller_track_resp = json.load(open('data/smaller_tracks.json'))


@app.get("/")
@app.get("/{number:int}")
async def index(number):
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


@app.post('/')
async def post(fib: int = Form(...)):
    return "{}-fib({})={}".format(__file__, fib, _fib(int(fib)))


@app.get('/smaller-tracks')
async def get_smaller_tracks():
    return smaller_track_resp


@app.get('/bigger-tracks')
async def get_bigger_tracks():
    return big_track_resp


from pydantic import BaseModel

class JSON(BaseModel):
    value: dict

@app.post('/tracks')
async def post_tracks(request: Request):
    tracks = await request.json()
    return {'cam_track_count': len(tracks['camera_tracks'])}


@app.get("/ping/")
async def ping():
    return {"Ping": "Pong"}


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)
