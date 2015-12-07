import numpy
import math

def saveFile(filename, data):
	numpy.savetxt(filename, data, delimiter=',', fmt='%.2f', newline = '\n')

def normalizeFFT(dirname):
    numFeatures = 2000

    #ds = SequentialDataSet(numFeatures, 1)

    tracks = glob.glob(os.path.join(dirname, '*.csv'))
    for t in tracks:
        track = os.path.splitext(t)[0]
        # load training data
        print "Reading %s..." % t
        data = numpy.genfromtxt(t, delimiter=",")
        numData = data.shape[0]

        # add the input to the dataset
        print "Adding to dataset..."
		windowSize = 4
        for i in range(numData - windowSize):
			meanDat = numpy.zeros(2000)
			for j in range(windowSize):
				meanDat = meanDat + data[i]
			meanDat = (1.0 / windowSize) * meanDat
			data[i] = data[i] - meanDat
			data[i][data[i] < 0] = 0
		saveFile('%s_norm.csv' %track, matrix)


if __name__ == '__main__':
	dirname = os.path.normpath(sys.argv[1])
	normalizeFFT(dirname)
