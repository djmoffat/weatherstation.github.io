#!/usr/bin/python3

import Adafruit_DHT
import datetime


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
if humidity is not None and temperature is not None:
    print("{},{},{}".format(datetime.datetime.now(), temperature, humidity))
