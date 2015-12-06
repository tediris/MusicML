import analyzer
import wave_reader
import glob
import numpy
import build_data
import sys
import math
import os

def analyzeSong(filename):
	# generate the average fourier transform of a kick
	kick = numpy.genfromtxt('kickdata.csv', delimiter=",")
	avgKick = kick.mean(axis=0)
	dataMat = readSong(filename)

def readSong(filename, segTime = 0.1):
	# read in the input song
	rate, data = wave_reader.readWav(filename)
	data = wave_reader.stereoToMono(data)

	# sample every 0.1 seconds by default
	segSize = segTime * rate
	matrix = numpy.array([])
	for i in range(0, math.floor(len(data)/segSize):
		data_seg = data[start:end]
		start += segSize
		end += segSize
		features = analyzer.getFrequencies(data_seg)
		matrix = build_data.addToFeatureMatrix(matrix, features[0:2000])
	outfile = os.path.splitext(filename)[0] + '.csv'
	build_data.saveFile(outfile, matrix)
	return matrix

def createKickFft():
	# read in the kick drum sample
	files = glob.glob('./kick_samples/*.wav')
	matrix = numpy.array([])
	for filename in files:
		print filename
		rate, data = wave_reader.readWav(filename)
		data = wave_reader.stereoToMono(data)
		features = analyzer.getFrequencies(data)
		matrix = build_data.addToFeatureMatrix(matrix, features[0:2000])
	build_data.saveFile('kickdata.csv', matrix)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == 'kick':
			print "generating kick data"
			print "--------------------"
			createKickFft()
