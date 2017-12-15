# coding: utf-8
import random

class BME280SensorSimulator:

    def __init__(self):
        pass

    def read_temperature(self):
        return random.uniform(25, 31)

    def read_humidity(self):
        return random.uniform(60, 80)
    