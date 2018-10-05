import machine


ON = 1
OFF = 0

LED = machine.Pin(1, machine.Pin.OUT)

timer = machine.Timer(-1)


class RelayController(object):
    OPEN = b'\xA0\x01\x00\xA1'
    CLOSE = b'\xA0\x01\x01\xA2'

    def __init__(self):
        self.opened = False
        self._relay = None

    def __lazy_init_uart(self):
        self._relay = machine.UART(0, 9600)
        self._relay.init(9600, bits=8, parity=None, stop=1, timeout=10)
        self._relay.write(self.OPEN)

    @property
    def relay(self):
        if self._relay is None:
            self.__lazy_init_uart()

        return self._relay

    def open(self):
        self.relay.write(self.OPEN)
        self.opened = True

    def close(self):
        self.relay.write(self.CLOSE)
        self.opened = False


RELAY = RelayController()


def open_relay(duration=5):
    if RELAY.opened:
        return False  # don't open if already opened

    RELAY.open()
    timer.init(period=duration * 1000, mode=machine.Timer.ONE_SHOT, callback=lambda t: RELAY.close())

    return True
