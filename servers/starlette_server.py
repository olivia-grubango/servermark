from starlette.applications import Starlette
from starlette.responses import PlainTextResponse

app = Starlette()


@app.route("/")
@app.route('/{number:int}')
async def index(request):
    number = request.path_params.get("number", 1)
    return PlainTextResponse("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.route('/', methods=['POST'])
async def post(request):
    number = (await request.form())['fib']
    return PlainTextResponse("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.route("/ping/")
async def ping():
    return "Pong"


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)
