import esp; esp.osdebug(None)

import gc

from utils import wifi
from utils.pins import LED, RELAY


wifi.toggle_wifi(True)
is_connected = wifi.connect()

LED.value(not is_connected)  # 'not' because 0 - is enable for led

if is_connected:
    RELAY.close()

gc.collect()
