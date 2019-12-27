from zeroconf import ServiceBrowser, Zeroconf
import socket
import urllib.request, json
from threading import Timer
from PySide2.QtCore import qDebug

newDeviceIP = []
wledList = []

class WledDevice: #class to store info about the discovered Wled devices
    def __init__(self, ip, info):
        self.ip = ip
        self.info = info

class MyListener:
    def add_service(self, zeroconf, type, name):
         info = zeroconf.get_service_info(type, name)
         globals()['newDeviceIP'].append(socket.inet_ntoa(info.address))

def startDiscovery():
    qDebug("scan started")  #scan for all mdns devices on the local network and add them to newDeviceList
    newDeviceIP.clear()
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    waitForlistener = Timer(5.0, continueDiscovery, {zeroconf}) #wait, to allow devices to be discovered
    waitForlistener.start()

def continueDiscovery(zeroconf):
    zeroconf.close()
    if(len(newDeviceIP) > 0): #if new devices are found
        retrieveInfo()
    qDebug("Total Wled devices found: %s" % (len(wledList)))

def retrieveInfo(): #try to retrieve info from device and check if they are Wled
    for x in range(len(newDeviceIP)):
        info = jsonCall(newDeviceIP[x]) #get info about the current Wled
        try:
            wled = info["info"]["brand"] #check if brand exists if not it's not a Wled
        except:
            continue
        if(wled == "WLED"):
            if(isNewDevice(info)): #check if the device is not already in the list
                wledDevice = WledDevice(newDeviceIP[x], info) #create new wledDevice
                wledList.append(wledDevice) #add Wled to list
            else:
                qDebug("device already exists")

def jsonCall(ip):
    output = {}
    try:
        data = urllib.request.urlopen("http://" + ip + "/json").read() #reads all info from the JSON api from Wled
        output = json.loads(data)
    except:
        output["status"] = "Failed"
    return output

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
        return True
