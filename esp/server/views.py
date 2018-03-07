from utils.pins import open_relay
from . import server_app as srv
from .core import JSONResponse


@srv.view('POST', '/')
def process_post(request):
    return JSONResponse(200, {"status": open_relay()})

