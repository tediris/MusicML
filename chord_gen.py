import midi
import random

def randBool(percent=50):
	return random.randrange(100) < percent

def generateRandomChords(chord):
	noteArray = []
	baseNote = random.randint(2,6) * 12 + chord[0]
	middleNote = random.randint(2,6) * 12 + chord[1]
	for i in range(2, 9):
		modifier = i * 12
		for note in chord:
			if randBool(30):
				noteArray.append(note + modifier)
	if not baseNote in noteArray:
		noteArray.append(baseNote)
	if not middleNote in noteArray:
		noteArray.append(middleNote)


	return noteArray


def createMajorChords(startNote):
	baseNote = startNote % 12
	notes = [baseNote, baseNote + 4, baseNote + 7]
	return generateRandomChords(notes)

def createMinorChords(startNote):
	baseNote = startNote % 12
	notes = [baseNote, baseNote + 3, baseNote + 7]
	return generateRandomChords(notes)

if __name__ == '__main__':
	noteList = createMajorChords(44)
	print noteList
