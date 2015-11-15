import math
import numpy
import scipy.io.wavfile as wavfile
from scipy import signal

def sine(frequency, length, rate):
	length = int(length * rate)
	factor = float(frequency) * (math.pi * 2) / rate
	return numpy.sin(numpy.arange(length) * factor)

def square(frequency, length, rate):
	length = int(length * rate)
	factor = float(frequency) * (math.pi * 2) / rate
	return signal.square(numpy.arange(length) * factor)
	# t = numpy.linspace(0, length, rate, endpoint=False)
	# return signal.square(2 * numpy.pi * 5 * t)

def saw(frequency, length, rate):
	length = int(length * rate)
	factor = float(frequency) * (math.pi * 2) / rate
	return signal.sawtooth(numpy.arange(length) * factor)
	# t = numpy.linspace(0, length, rate, endpoint=False)
	# return signal.sawtooth(2 * numpy.pi * 5 * t)

def noise(length, rate):
	return numpy.random.uniform(-1, 1, length * rate)

def saveAudioBuffer(filename, data):
	scaled = numpy.int16(data/numpy.max(numpy.abs(data)) * 32767)
	wavfile.write(filename, 44100, scaled)

def generateAudio(frequency=440, length=1, rate=44100):
	chunks = []
	chunks.append(sine(frequency, length, rate))

	chunk = numpy.concatenate(chunks) * 0.25


if __name__ == '__main__':
	data = saw(440, 1, 44100)
	scaled = numpy.int16(data/numpy.max(numpy.abs(data)) * 32767)
	wavfile.write('test.wav', 44100, scaled)
