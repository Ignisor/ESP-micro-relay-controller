import machine


ON = 1
OFF = 0

LED = machine.Pin(1, machine.Pin.OUT)
RELAY = machine.Pin(2, machine.Pin.OUT)  # D5 pin
RELAY.value(OFF)  # open relay initially

timer = machine.Timer(-1)


def open_relay(duration=5):
    if RELAY.value() == OFF:
        return False  # don't open if already opened

    RELAY.value(OFF)

    timer.init(period=duration * 1000, mode=machine.Timer.ONE_SHOT, callback=lambda t: RELAY.value(ON))

    return True

