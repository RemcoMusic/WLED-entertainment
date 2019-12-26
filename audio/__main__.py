# This Python file uses the following encoding: utf-8
from audio.audioInput import AudioInput
from PySide2.QtCore import qDebug

class Test():

    def __init__(self):
        self.audioInput = AudioInput()

    def audioChunk(self):
        audioArray = self.audioInput.getAudioStream()
        return audioArray

    def xAxis(self):
        xArray = self.audioInput.getXaxis()
        return xArray

if __name__ == "__main__":
     print("Unit Test Boy!")
