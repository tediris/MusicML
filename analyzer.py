import numpy
import math
import scipy.fftpack
import matplotlib.pyplot as plt
import wave_gen

def getFrequencies(sample):
	fourierTrans = numpy.abs(numpy.fft.fft(sample, 44100))
	maxVal = numpy.max(fourierTrans)
	if (maxVal != 0):
		fourierTrans = (fourierTrans / maxVal)
	# return only the positive frequencies
	return fourierTrans[0:(fourierTrans.size / 2)]

def plotFourierTransform(sample):
	fourierTrans = numpy.abs(numpy.fft.fft(sample))
	fourierTrans = fourierTrans[0:(fourierTrans.size / 2)]
	fig, ax = plt.subplots()
	ax.plot(fourierTrans)
	plt.show()

def plotSample(sample):
	fig, ax = plt.subplots()
	ax.plot(sample)
	plt.show()

if __name__ == '__main__':
	# create a sine wave at the desired frequency
	sineWave = wave_gen.saw(440, 1, 44100) #+ wave_gen.sine(1000, 1, 44100)
	#sineWave = sineWave + (wave_gen.noise(1, 44100) * 10)
	# create the plot
	fig, ax = plt.subplots()

	# get the fourier transform
	sineFreq = numpy.abs(numpy.fft.fft(sineWave))

	# we only care about the positive frequencies
	sineFreq = sineFreq[0:(sineFreq.size / 2)]
	print numpy.max(sineFreq)

	# plot our fourier transform
	#saw = wave_gen.saw(440, 1, 44100)
	print sineWave[0]
	ax.plot(sineFreq)
	plt.show()
