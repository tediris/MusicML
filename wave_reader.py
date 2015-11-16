import math
import numpy
import scipy.io.wavfile as wavfile
from scipy import signal
import analyzer
import build_data

def stereoToMono(audiodata):
	d = audiodata.sum(axis=1) / 2
	return d

def readWav(filename):
	rate, data = wavfile.read(filename)
	return rate, data

if __name__ == '__main__':
	rate, data = wavfile.read('basic_prog.wav')
	data = stereoToMono(data)
	start = 0
	end = data.size / 4
	segSize = data.size / 4
	matrix = numpy.array([])
	for i in range(0, 4):
		data_seg = data[start:end]
		start += segSize
		end += segSize
		features = analyzer.getFrequencies(data_seg)
		matrix = build_data.addToFeatureMatrix(matrix, features[0:5000])

	build_data.saveFile('testdata.csv', matrix)
