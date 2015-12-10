import analyzer
import wave_reader
import glob
import numpy
import build_data
import sys
import math
import os
import scipy

def analyzeSong(filename):
	# generate the average fourier transform of a kick
	snare = numpy.genfromtxt('snaredata.csv', delimiter=",")
	kick = numpy.genfromtxt('kickdata.csv', delimiter=",")
	meanSnare, covar = analyzeSoundType(snare)
	meanKick, covar = analyzeSoundType(kick)
	dataMat = readSong(filename)
	matrix = numpy.array([])
	for i in range(0, len(dataMat), 5):
		dist = numpy.zeros(len(dataMat))
		for j in range(0, 4):
			dist[j] = numpy.dot(meanVec, dataMat[i + j])
		minDistIndex = numpy.argmin(dist)
		matrix = build_data.addToFeatureMatrix(matrix, dataMat[i + minDistIndex])
	build_data.saveFile(filename + '.csv', matrix)

def readSong(filename, segTime = 0.05):
	# read in the input song
	rate, data = wave_reader.readWav(filename)
	data = wave_reader.stereoToMono(data)
	# sample every 0.1 seconds by default
	segSize = segTime * rate
	matrix = numpy.array([])
	print 'reading in song...'
	start = 0
	end = segSize
	for i in range(0, int(math.floor(len(data)/segSize))):
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

def createSnareFft():
	# read in the snare drum sample
	files = glob.glob('./snare_samples/*.wav')
	matrix = numpy.array([])
	for filename in files:
		print filename
		rate, data = wave_reader.readWav(filename)
		data = wave_reader.stereoToMono(data)
		features = analyzer.getFrequencies(data)
		matrix = build_data.addToFeatureMatrix(matrix, features[0:2000])
	build_data.saveFile('snaredata.csv', matrix)

def analyzeSoundType(data = None):
	print 'building model...'
	if data is not None:
		data = numpy.genfromtxt('kickdata.csv', delimiter=",")
	meanVec = numpy.mean(data, axis=0)
	covar = numpy.cov(data, rowvar=0)
	return meanVec, covar

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == 'kick':
			print "generating kick data"
			print "--------------------"
			createKickFft()
		elif sys.argv[1] == 'snare':
			print "generating snare data"
			print "--------------------"
			createSnareFft()
		elif sys.argv[1] == 'analyze' and len(sys.argv) > 2:
			analyzeSong(sys.argv[2])
		elif sys.argv[1] == 'analyze' and len(sys.argv) == 2:
			analyzeSoundType()
