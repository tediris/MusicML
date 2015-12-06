import math
import numpy
import scipy.io.wavfile as wavfile
from scipy import signal
import analyzer
import build_data
import sys
import wave_gen

def stereoToMono(audiodata):
    d = audiodata.sum(axis=1) / 2
    return d

def readWav(filename):
    rate, data = wavfile.read(filename)
    return rate, data

<<<<<<< HEAD
def extractFeatures(track, div):
    rate, data = wavfile.read(track + '.wav')
=======
def wavToFeatures(filename):
    rate, data = wavfile.read(filename)
>>>>>>> 27abc93283f1681e96e889f74280e895eeeac2f5
    if data.ndim > 1:
        data = stereoToMono(data)
    matrix = numpy.array([])
    vmatrix = numpy.array([])

<<<<<<< HEAD
    segSize = rate / div
    start = 0
    end = segSize
=======
    segDiv = 4 #1/10 of a second
    segSize = rate / segDiv
    start = 0
    end = segSize
    matrix = numpy.array([])
>>>>>>> 27abc93283f1681e96e889f74280e895eeeac2f5
    for i in range(0, data.size / segSize):
        data_seg = data[start:end]
        start += segSize
        end += segSize
<<<<<<< HEAD
        features = analyzer.getFrequencies(data_seg)[0:5000]
        matrix = build_data.addToFeatureMatrix(matrix, features)
        vmatrix = build_data.addToFeatureMatrix(vmatrix,
                             numpy.array([numpy.argmax(features)]))
    build_data.saveFile(track + '_seg.csv', matrix)
    build_data.saveFile(track + '_volume.csv', vmatrix)

=======
        features = analyzer.getFrequencies(data_seg)
        matrix = build_data.addToFeatureMatrix(matrix, features[0:2000])
    # build_data.saveFile('testdata.csv', matrix)
    return matrix

def extractFeatures(track, div):
    rate, data = wavfile.read(track + '.wav')
    if data.ndim > 1:
        data = stereoToMono(data)
    matrix = numpy.array([])
    vmatrix = numpy.array([])

    segSize = rate / div
    start = 0
    end = segSize
    for i in range(0, data.size / segSize):
        data_seg = data[start:end]
        start += segSize
        end += segSize
        features = analyzer.getFrequencies(data_seg)[0:5000]
        matrix = build_data.addToFeatureMatrix(matrix, features)
        vmatrix = build_data.addToFeatureMatrix(vmatrix,
                             numpy.array([numpy.argmax(features)]))
    build_data.saveFile(track + '_seg.csv', matrix)
    build_data.saveFile(track + '_volume.csv', vmatrix)
>>>>>>> 27abc93283f1681e96e889f74280e895eeeac2f5

if __name__ == '__main__':
    track = sys.argv[1]
    div = 10
    extractFeatures(track, div)
##    matrix = numpy.genfromtxt(track + '_seg.csv', delimiter=',')
##    wave_gen.writeWav(track + '_seg.wav', matrix, div)
##    vmatrix = numpy.genfromtxt(track + '_volume.csv', delimiter=',')
##    wave_gen.writeWav(track + '_volume.wav', vmatrix, div)
