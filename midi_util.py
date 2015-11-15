import math

def midiToFrequency(note):
	return (math.pow(2, ((note - 69) / 12.0)) * 440)
