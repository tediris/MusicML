import math
import numpy
import scipy.io.wavfile as wavfile
from scipy import signal
import analyzer

if __name__ == '__main__':
	rate, data = wavfile.read('tak_instrumental.wav')
	start = 0
	end = data.size / 800
	data_seg = data[start:end]
	analyzer.plotFourierTransform(data_seg)
