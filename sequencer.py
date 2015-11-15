import numpy
import midi
import midi_util
import wave_gen

# midi has 7 bits (128 different notes)
class Sequencer:
	def __init__(self):
		# create the empty note event arrays
		self.noteActive = [False] * 128
		self.sampleRate = 44100
		self.output = numpy.zeros(5)
		self.tracks = []

	def generateAudio(self, duration):
		if duration == 0:
			return

		# generate the base empty sample
		bpm = 120
		ppq = 96 # resolution
		seconds = (60.0 / (bpm * ppq)) * duration
		length = int(seconds * self.sampleRate)
		sample = numpy.zeros(length)

		# add in any notes that are active
		#print "adding some samples in"
		for i in range(0, 128):
			if (self.noteActive[i]):
				print "note: " + str(i)
				frequency = midi_util.midiToFrequency(i)
				print "adding frequency " + str(frequency)
				sample += wave_gen.saw(frequency, seconds, self.sampleRate)

		# concatenate this to the output
		self.output = numpy.concatenate([self.output, sample])

	def parseMidiFile(self, filename):
		self.output = numpy.zeros(5)
		pattern = midi.read_midifile(filename)
		for track in pattern:
			# for now, assume only 1 track
			for event in track:
				#print repr(event)
				if type(event) is midi.events.NoteOnEvent:
					self.generateAudio(event.tick)
					note = event.pitch
					self.noteActive[note] = True
				elif type(event) is midi.events.NoteOffEvent:
					self.generateAudio(event.tick)
					note = event.pitch
					self.noteActive[note] = False

		return self.output

if __name__ == '__main__':
	seq = Sequencer()
	samples = seq.parseMidiFile('viva.mid')
	wave_gen.saveAudioBuffer('viva.wav', samples)
