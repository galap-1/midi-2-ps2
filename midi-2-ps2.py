import random

PianoOffset = 60
#This is what note the low C is on the piano keyboard

PianoKeyNoteTable = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C^', 'C#^','D^', 'D#^', 'E^', 'F^', 
		'F#^', 'G^', 'G#^', 'A^', 'A#^', 'B^', 'C^^']
#the relevant 25 notes in order

TypingKeyLetterTable = ['Z', 'S', 'X', 'D', 'C', 'V', 'G', 'B', 'H', 'N', 'J', 'M', 'Q', '2', 'W', '3', 'E', 'R', '5', 'T', 
		'6', 'Y', '7', 'U', 'I']
#the typing keyboard letters associated with the corresponding note in KeyNoteTable

TypingKeyCommandTable = [0x1A, 0x1B, 0x22, 0x23, 0x21, 0x2A, 
		0x34, 0x32, 0x33, 0x31, 0x3B, 0x3A, 0x15, 0x1E, 0x1D, 0x26, 0x24, 0x2D, 0x2E, 0x2C, 0x36, 0x25, 0x3D, 0x3C, 0x43]
#the hex ps/2 key command

TypingReleaseCommandHex = 0xF0
#the hex ps/2 key release command

MidiNote = random.randint(60,84)

InputNote = MidiNote - PianoOffset
#align the midi input to the beginning of the 25 note output range

print ('Key On ' + str(MidiNote) + ' Note: ' + str(PianoKeyNoteTable[InputNote]) + ' Character: ' + 
	str(TypingKeyLetterTable[InputNote]) + ' Command: ' + str(hex(TypingKeyCommandTable[InputNote])))

print ('Key Off ' + str(MidiNote) + ' Note: ' + str(PianoKeyNoteTable[InputNote]) + ' Character: ' + 
	str(TypingKeyLetterTable[InputNote]) + ' Command: ' + str(hex(0xF0)) + ' ' + str(hex(TypingKeyCommandTable[InputNote])))