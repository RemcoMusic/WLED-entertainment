from zeroconf import ServiceBrowser, Zeroconf
import socket
import urllib.request, json
from PySide2.QtCore import qDebug
import time

class WledDevice: #class to store info about the discovered Wled devices
    def __init__(self, ip, info):
        self.ip = ip
        self.info = info

class MyListener:
    def __init__(self):
        self.newDeviceIP = []

    def add_service(self, zeroconf, type, name):
         info = zeroconf.get_service_info(type, name)
         self.newDeviceIP.append(socket.inet_ntoa(info.address))
         print("new device found")

    def getIP(self):
        return self.newDeviceIP

class Devices():

    def __init__(self):
        self.wledList = []

    def continueDiscovery(self, zeroconf, listener):
        zeroconf.close()
        newDeviceIP = listener.getIP()

        print(newDeviceIP)
        if(len(newDeviceIP) > 0): #if new devices are found
            self.retrieveInfo(newDeviceIP)
        qDebug("Total Wled devices found: %s" % (len(self.wledList)))
        for x in range(len(self.wledList)):
            qDebug(self.wledList[x].info["info"]["name"])

    def startDiscovery(self):
        qDebug("scan started")  #scan for all mdns devices on the local network and add them to newDeviceList
        zeroconf = Zeroconf()
        listener = MyListener()
        ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
        time.sleep(3)
        zeroconf.close()
        newDeviceIP = listener.getIP()
        print(newDeviceIP)
        if(len(newDeviceIP) > 0): #if new devices are found
            self.retrieveInfo(newDeviceIP)
        qDebug("Total Wled devices found: %s" % (len(self.wledList)))
        for x in range(len(self.wledList)):
            qDebug(self.wledList[x].info["info"]["name"])

    def retrieveInfo(self, newDeviceIP): #try to retrieve info from device and check if they are Wled
        for x in range(len(newDeviceIP)):
            info = self.jsonCall(newDeviceIP[x]) #get info about the current Wled
            try:
                wled = info["info"]["brand"] #check if brand exists if not it's not a Wled
            except:
                continue
            if(wled == "WLED"):
                if(self.isNewDevice(info)): #check if the device is not already in the list
                    wledDevice = WledDevice(newDeviceIP[x], info) #create new wledDevice
                    self.wledList.append(wledDevice) #add Wled to list
                else:
                    qDebug("device already exists")

    def jsonCall(self, ip):
        output = {}
        try:
            data = urllib.request.urlopen("http://" + ip + "/json").read() #reads all info from the JSON api from Wled
            output = json.loads(data)
        except:
            output["status"] = "Failed"
        return output

    def isNewDevice(self, info):
        deviceFound = False
        if(len(self.wledList) != 0):
            for x in range(len(self.wledList)):
                if(self.wledList[x].info["info"]["mac"] != info["info"]["mac"]):
                    deviceFound = False
                else:
                    return False
            return not deviceFound
        else:
            return True
