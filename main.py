# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import qDebug

from audio.__main__ import test
from discovery.__main__ import discovery



def runOther():
    qDebug("Program started")
    #test()
    discovery()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    #engine = QQmlApplicationEngine()
    #engine.load('ApplicationWindow.qml')
    #engine.quit.connect(app.quit)

    runOther()

    sys.exit(app.exec_())
