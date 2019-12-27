# This Python file uses the following encoding: utf-8
from PySide2.QtCore import qDebug
import pyaudio
import numpy as np
import struct
import matplotlib.pyplot as plt
from scipy.fftpack import fft

class AudioInput():

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.CHUNK = 1024 * 2
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.dataInt = 0
        self.stream = self.p.open(format=self.FORMAT,channels=self.CHANNELS,input_device_index=2, rate=self.RATE,input=True, frames_per_buffer=self.CHUNK)

    def getAudioDeviceList(self):                                           #TODO needs to return a dictonary so it can be chosen from the UI
        for i in range(self.p.get_device_count()):
            qDebug(str(self.p.get_device_info_by_index(i)))
            qDebug(" ")

    def getAudioStream(self):
        data = self.stream.read(self.CHUNK)
        data_int = struct.unpack(str(4 * self.CHUNK) + 'B', data)
        self.dataInt = data_int
        data_np = np.array(data_int, dtype=np.int16)[::4]
        return data_np

    def drawGraph(self):
        fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

        # Deze moet gebruikt worden!
        x = np.arange(0, 2 * self.CHUNK, 2)
        # frequencies (spectrum)
        xf = np.linspace(0, self.RATE, self.CHUNK)

        # Wordt tijdelijk gevuld met random data
        line, = ax1.plot(x, np.random.rand(self.CHUNK), '-',lw=2)
        line_fft, = ax2.semilogx(xf, np.random.rand(self.CHUNK), '-', lw=2)

        ax1.set_title('AUDIO WAVEFORM')
        ax1.set_xlabel('samples')
        ax1.set_ylabel('volume')
        ax1.set_ylim(0, 255)
        ax1.set_xlim(0, 2 * self.CHUNK)
        plt.setp(ax1, xticks=[0, self.CHUNK, 2 * self.CHUNK], yticks=[0, 128, 255])

        ax2.set_xlim(20, self.RATE / 2)

        plt.show(block=False)

        while True:
            data = self.getAudioStream()
            line.set_ydata(data)

            yf = fft(self.dataInt)
            line_fft.set_ydata(np.abs(yf[0:self.CHUNK])  / (128 * self.CHUNK))

            fig.canvas.draw()
            fig.canvas.flush_events()


if __name__ == "__main__":
     qDebug("Unit Test Boy!" )
