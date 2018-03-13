from utils.pins import open_relay
from data import conf
from . import server_app as srv
from .core import JSONResponse, Response


@srv.view('POST', '/')
def process_post(request):
    return JSONResponse(200, {"status": open_relay()})


@srv.view('GET', '/config/')
def get_config(request):
    conf_dict = {}
    for var in dir(conf):
        if var.startswith('__'):
            continue  # skip system variables

        conf_dict[var] = getattr(conf, var)

    return JSONResponse(200, conf_dict)


@srv.view('POST', '/config/')
def update_config(request):
    return Response(200, request.body)
