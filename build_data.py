import chord_gen
import midi_util
import numpy
import wave_gen
import analyzer

def saveFile(filename, data):
	numpy.savetxt(filename, data, delimiter=',', fmt='%.2f', newline = '\n')

def addToFeatureMatrix(matrix, feature):
	feature = feature.reshape(1, feature.shape[0])
	if matrix.size is 0:
		matrix = feature;
	else:
		matrix = numpy.vstack((matrix, feature))
	return matrix

if __name__ == '__main__':
	matrix = numpy.array([])
	seconds = 1
	for note in range(0, 12):
		print "generating note " + str(note)
		for x in range(0, 100):
			notesToPlay = chord_gen.createMajorChords(note)
			length = int(seconds * 44100)
			sample = numpy.zeros(length)
			for i in range(0, len(notesToPlay)):
				freq = midi_util.midiToFrequency(notesToPlay[i])
				sample += wave_gen.saw(freq, seconds, 44100)
			features = analyzer.getFrequencies(sample)
			features = numpy.append(features[0:5000], note)
			#features = features.astype(numpy.int16)
			matrix = addToFeatureMatrix(matrix, features)

	saveFile('largedata.csv', matrix)
