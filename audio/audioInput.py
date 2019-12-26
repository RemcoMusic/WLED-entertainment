# This Python file uses the following encoding: utf-8
from PySide2.QtCore import qDebug
import pyaudio
import numpy as np
import struct
import matplotlib.pyplot as plt

class AudioInput():

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.CHUNK = 1024 * 4
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100

    def getAudioDeviceList(self):                                           #TODO needs to return a dictonary so it can be chosen from the UI
        for i in range(self.p.get_device_count()):
            qDebug(str(self.p.get_device_info_by_index(i)))
            qDebug(" ")

    def getAudioStream(self):
        stream=self.p.open(format=self.FORMAT,channels=self.CHANNELS,input_device_index=2, rate=self.RATE,input=True, frames_per_buffer=self.CHUNK)
        data = stream.read(self.CHUNK)
        data_int = struct.unpack(str(4 * self.CHUNK) + 'B', data)
        data_np = np.array(data_int, dtype=np.int16)[::4]
        return data_np

    def getXaxis(self):
        x = np.arange(0, 2 * self.CHUNK, 2)
        return x

    def testAudioFile(self):
        qDebug("Dit is de audio file")

#    fig, ax = plt.subplots(1, figsize=(15, 7))
#    x = np.arange(0, 2 * CHUNK, 2) Deze moet gebruikt worden!
#    line, = ax.plot(x, np.random.rand(CHUNK), '-',lw=2)
#    ax.set_title('AUDIO WAVEFORM')
#    ax.set_xlabel('samples')
#    ax.set_ylabel('volume')
#    ax.set_ylim(-400, 400)
#    ax.set_xlim(0, 2 * CHUNK)
#    plt.show(block=False)
#    line.set_ydata(data_np)
#    fig.canvas.draw()
#    fig.canvas.flush_events()
if __name__ == "__main__":
     qDebug("Unit Test Boy!" )
