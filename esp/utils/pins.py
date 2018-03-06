import machine
import time


ON = 1
OFF = 0

LED = machine.Pin(2, machine.Pin.OUT)
BUTTON = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # D2 pin
RELAY = machine.Pin(14, machine.Pin.OUT)  # D5 pin
RELAY.value(OFF)  # open relay initially


def open_relay(duration=5):
    RELAY.value(OFF)
    time.sleep(duration)
    RELAY.value(ON)

    return True


def check_button():
    if BUTTON.value() == OFF:  # returns 0 when pressed
        open_relay()
