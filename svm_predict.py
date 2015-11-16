import numpy
from sklearn import svm

# read the training file
print "Reading in training file..."
raw_data = numpy.genfromtxt('largedata.csv', delimiter=",")
numFeatures = raw_data[0].size
numData = raw_data.size / numFeatures


X = raw_data[:, 0:numFeatures - 1]
y = raw_data[:, numFeatures - 1]
labels = numpy.copy(y)
features = numpy.copy(X)
clf = svm.SVC()
print "Fitting the data"
clf.fit(X, y)

predictions = clf.predict(features)

errors = 0
print "Predictions: "
for i in range(0, numData):
	if predictions[i] != labels[i]:
		errors += 1
		print "guessed: " + str(predictions[i]) + ", actual: " + str(labels[i])

print "error rate: " + str(errors * 1.0 / numData)

print "Trying real audio"
testdata = numpy.genfromtxt('testdata.csv', delimiter=",")
print clf.predict(testdata)
