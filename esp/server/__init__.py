from .core import Server
server_app = Server()

from . import views  # initialize views after server initialisation
