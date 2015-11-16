import numpy
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def saveNetwork(filename, net):
	fileObject = open(filename, 'w')
	pickle.dump(net, fileObject)
	fileObject.close()

def loadNetwork(filename):
	fileObject = open(filename,'r')
	return pickle.load(fileObject)

if __name__ == '__main__':
	# read the training file
	print "Reading in training file..."
	raw_data = numpy.genfromtxt('mydata.csv', delimiter=",")
	numFeatures = raw_data[0].size
	numData = raw_data.size / numFeatures

	# initialize the neural network
	print "Initializing neural network..."
	net = buildNetwork(numFeatures - 1, numFeatures - 1, 2, bias=True)
	ds = SupervisedDataSet(numFeatures - 1, 2)

	# add the input to the dataset
	print "Loading the dataset"
	for i in range(0, numData):
		data = raw_data[i]
		features = tuple(data[0:numFeatures - 1])
		label = int(data[numFeatures - 1])
		ds.addSample(features, (label,))

	# train the network on the dataset
	print "Training neural net"
	trainer = BackpropTrainer(net, ds)
	for i in range(0, 10):
		print "error: " + str(trainer.train())

	# save the network
	saveNetwork('mynet', net)

	# predict on some of the training examples
	print "Predicting on training set"
	for i in range(0, 10):
		data = raw_data[i]
		features = list(data[0:numFeatures - 1])
		label = int(data[numFeatures - 1])
		print net.activate(features)
