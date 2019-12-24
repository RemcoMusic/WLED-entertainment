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

def jsonCall(device):
    output = {}
    jsonCommand = "http://" + device.ip + "/json"
    try:
        data = urllib.request.urlopen(jsonCommand).read()
        output = json.loads(data)
    except:
        print("request failed")
        output["status"] = "Failed"
    return output

def scanMdns():
    print("scan started")
    #scan for all mdns devices on the local network and add them to newDeviceList
    newDeviceList.clear()
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(5)
    print("Scan completed")
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
    for x in range(len(newDeviceList)):
        info = jsonCall(newDeviceList[x])
        try:
            wled = info["info"]["brand"]
        except:
            print("Not a WledDevice or connection lost")
            continue
        if(wled == "WLED"):
            print("Wled device found at: %s" % (newDeviceList[x].ip))
            #get info about the current Wled
            if(isNewDevice(info)):
                print("new device added")
                wledDevice = WledDevice(newDeviceList[x].ip, info)
                wledList.append(wledDevice)
            else:
                print("device already exists")

def startDiscovery():
    scanMdns()
    if(len(newDeviceList) > 0):
        print("Total devices found: %s" % (len(newDeviceList)))
        testIfWled()
    print("Total Wled devices found: %s" % (len(wledList)))
