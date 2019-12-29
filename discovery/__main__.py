# This Python file uses the following encoding: utf-8
from discovery.wled import Devices

class MainDiscovery:
    def __init__(self):             
        self.devices = Devices()
        self.devices.startDiscovery()


