# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject
import threading
import logging

from audio.__main__ import MainAudio
from discovery.__main__ import discovery

class Main(QObject):

    def __init__(self):
        QObject.__init__(self)


    def startAudioVisualiser(self):
        audio = MainAudio()
        assert audio

    def startDevicesDiscovery(self):
        discovery()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

    dataToUI = Main()

    dataToUI.startDevicesDiscovery()

    audioThread = threading.Thread(target=dataToUI.startAudioVisualiser)
    audioThread.start()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("dataToUI", dataToUI)
    engine.load('ApplicationWindow.qml')
    engine.quit.connect(app.quit)
    logging.info("Program is running")

    sys.exit(app.exec_())
