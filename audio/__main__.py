# This Python file uses the following encoding: utf-8
from audio.audioInput import AudioInput
from PySide2.QtCore import qDebug

class MainAudio():

    def __init__(self):
        self.audioInput = AudioInput()
        self.audioInput.drawGraph()

if __name__ == "__main__":
     qDebug("Unit Test Boy!")
