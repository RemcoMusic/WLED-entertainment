# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal
from PySide2.QtQml import QJSValue, QJSEngine
import threading
import logging

from audio.__main__ import MainAudio
from discovery.__main__ import discovery

class Main(QObject):

    wledDevicesSignal = Signal(QJSValue, arguments= ['getWled'])

    def __init__(self):
        QObject.__init__(self)

    def startAudioVisualiser(self):
        audio = MainAudio()
        assert audio

    @Slot()
    def startDevicesDiscovery(self):
        devicesThread = threading.Thread(target=discovery)
        devicesThread.start()

    @Slot()
    def getWled(self):
        myEngine = QJSEngine()
        myObject = QJSValue()

        myObject = myEngine.newObject()

        myObject.setProperty("name", "Slaapkameraaaah")
        self.wledDevicesSignal.emit(myObject)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

    dataToUI = Main()

    audioThread = threading.Thread(target=dataToUI.startAudioVisualiser)
    audioThread.start()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("dataToUI", dataToUI)
    engine.load('QML/ApplicationWindow.qml')
    engine.quit.connect(app.quit)
    logging.info("Program is running")

    sys.exit(app.exec_())
