# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, qDebug, Signal, Slot, Property, QPointF
from PySide2.QtCharts import QtCharts
import random


from audio.__main__ import Test

class Main(QObject):

    testSignal = Signal()
    startSignal = Signal()

    def __init__(self):
        QObject.__init__(self)
        self.newY = 0
        self.newX = 0
        self.oldY = 0
        self.oldX = 0
        self.audioImport = Test()

    @Slot()
    def getAudioReady(self):

        audioArray = self.audioImport.audioChunk()
        xArray = self.audioImport.xAxis()
#        print(audioArray)
#        print(xArray)
        for x in range (len(audioArray)):
            if x == 0:
                self.oldX = 0
                self.oldY = 0
            else:
                self.oldX = xArray[x-1]
                self.oldY = audioArray[x-1]
            currentYPoint = audioArray[x]
            currentXPoint = xArray[x]
            self.newY = currentYPoint
            self.newX = currentXPoint
            self.testSignal.emit()
        self.startSignal.emit()

    @Slot(result=int)
    def setYPoint(self):
        return self.newY

    @Slot(result=int)
    def setXPoint(self):
        return self.newX

    @Slot(result=int)
    def getOldYPoint(self):
        return self.oldY

    @Slot(result=int)
    def getOldXPoint(self):
        return self.oldX


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dataToUI = Main()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("dataToUI", dataToUI)
    engine.load('ApplicationWindow.qml')
    engine.quit.connect(app.quit)

    sys.exit(app.exec_())
