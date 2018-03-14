import sys
import machine

from data import conf
from utils.wifi import reset_if_not_connected
from server import server_app


def main_loop():
    return reset_if_not_connected()


try:
    server_app.activate_server(main_loop)
except Exception as e:
    # write exception to file and restart a machine in case of error
    with open(conf.ERROR_LOG_FILENAME, 'w') as err_file:
        sys.print_exception(e, err_file)
    machine.reset()
