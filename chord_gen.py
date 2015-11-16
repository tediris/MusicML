import midi
import random

def randBool(percent=50):
	return random.randrange(100) < percent

def generateRandomChords(chord):
	noteArray = []
	for i in range(2, 9):
		modifier = i * 12
		for note in chord:
			if randBool(30):
				noteArray.append(note + modifier)
	return noteArray


def createMajorChords(startNote):
	baseNote = startNote % 12
	notes = [baseNote, baseNote + 4, baseNote + 7]
	return generateRandomChords(notes)

if __name__ == '__main__':
	noteList = createMajorChords(44)
	print noteList
