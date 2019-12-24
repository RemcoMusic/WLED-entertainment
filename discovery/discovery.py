# This Python file uses the following encoding: utf-8
from zeroconf import ServiceBrowser, Zeroconf
import socket
import time
import requests
import urllib.request, json

newDeviceList = []
wledList = []

class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

class WledDevice:
    def __init__(self, ip, info):
        self.ip = ip
        self.info = info

class MyListener:
    def add_service(self, zeroconf, type, name):
         info = zeroconf.get_service_info(type, name)
         device = Device(name, socket.inet_ntoa(info.address))
         globals()['newDeviceList'].append(device)

def sendAPIcall(device, call):
    apiCommand = "http://" + device.ip + call
    response = requests.get(apiCommand)
    return response

def jsonCall(device):
    jsonCommand = "http://" + device.ip + "/json"
    data = urllib.request.urlopen(jsonCommand).read()
    output = json.loads(data)
    return output

def scanMdns():
    #scan for all mdns devices on the local network and add them to newDeviceList
    newDeviceList.clear()
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(5)
    zeroconf.close()

def isNewDevice(info):
    deviceFound = False
    if(len(wledList) != 0):
        for x in range(len(wledList)):
            if(wledList[x].info["info"]["mac"] != info["info"]["mac"]):
                deviceFound = False
            else:
                return False
        return not deviceFound
    else:
        print("list empty adding new device")
        return True

def testIfWled():
    #loop trough newDeviceList and test if they are Wled devices or not
    for x in range(len(newDeviceList)):
        if (sendAPIcall(newDeviceList[x],"/win").status_code == 200):
            print("Wled device found at: %s" % (newDeviceList[x].ip))
            #get info about the current Wled
            info = jsonCall(newDeviceList[x])
            if(isNewDevice(info)):
                print("new device added")
                wledDevice = WledDevice(newDeviceList[x].ip, info)
                wledList.append(wledDevice)
            else:
                print("device already exists")

def wledDetection():
    scanMdns()
    print("Total devices found: %s" % (len(newDeviceList)))
    testIfWled()
    print("Total Wled devices found: %s" % (len(wledList)))
#    for x in range(len(wledList)):
#       print(wledList[x].info["info"]["mac"])

if __name__ == "__main__":
    print("Dit is de discoveryMain file")
