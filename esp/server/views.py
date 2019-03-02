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
    with open('data/local_conf.py', 'w') as local_conf:
        for var, value in request.body.items():
            line = '{} = {}\n'.format(var, repr(value))
            local_conf.write(line)

    return Response(200)


@srv.view('GET', '/error/')
def get_error(request):
    with open(conf.ERROR_LOG_FILENAME) as error_log:
        r = Response(200, error_log.read())

    return r
