import machine
import ubinascii
from umqtt.simple import MQTTClient

from data import conf
from utils.pins import open_relay


CLIENT_ID = ubinascii.hexlify(machine.unique_id())


def main_loop(msg):
    if msg.decode() == 'down':
        open_relay()


mqtt = MQTTClient(CLIENT_ID, conf.MQTT_SERVER)
mqtt.set_callback(main_loop)
mqtt.connect()
mqtt.subscribe('button/pressed/+')


while True:
    try:
        mqtt.wait_msg()
    except Exception as e:
        with open(conf.ERROR_LOG_FILENAME, 'w') as err_log:
            err_log.write(e)
            err_log.write('\n')

        mqtt.publish('errors/{}'.format(CLIENT_ID).encode(), str(e).encode())
        mqtt.disconnect()
        machine.reset()
