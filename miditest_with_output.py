


import sys
import time

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


#the data in the following are used for bitbanging the ps/2 data line. first bit is 0, then data sent least significant bit first, then a parity bit to ensure the message has even parity once the ending by (1) is sent

TypingReleaseTable = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

TypingKeyTable = [
				[0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
				[0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
				[0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
				[0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
				[0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
				[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
				[0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
				[0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
				[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
				[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
				[0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
				[0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
				[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				[0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
				[0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
				[0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
				[0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
				[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
				[0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
				[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
				[0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
				[0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
				[0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
				[0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
				[0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]

def SendTypingKey():
	if 0 <= InputNote <= 24:
		for i in range(0, 10):
			print(TypingKeyTable[InputNote][i], end = " ")
		print("\n")								#^ don't start a new line every time
		#^ move the cursor to the next line
	else: 
		print("Note not in range")
	
	
def SendTypingRelease():
	if 0 <= InputNote <= 24:
		for i in range(0, 10):
			print(TypingReleaseTable[i], end = " ")
		print("\n")						#^ don't start a new line every time
		#^ move the cursor to the next line




from rtmidi.midiutil import open_midiinput




# Prompts user for MIDI input port, unless a valid port number or name
# is given as the first argument on the command line.
# API backend defaults to ALSA on Linux.
port = sys.argv[1] if len(sys.argv) > 1 else None

try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Entering main loop. Press Control-C to exit.")
try:
	timer = time.time()
	while True:
			RawMessage = midiin.get_message()

			if RawMessage:
				MidiMessage, deltatime = RawMessage
				InputNote = MidiMessage[1] - PianoOffset
				if MidiMessage[0] == 144:
					NoteOn = True
					NoteOff = False
					print ('Key On ' + str(InputNote) + ' Note: ' + str(PianoKeyNoteTable[InputNote]) + ' Character: ' + 
						str(TypingKeyLetterTable[InputNote]) + ' Command: ' + str(hex(TypingKeyCommandTable[InputNote])))
					SendTypingKey()
				if MidiMessage[0] == 128:
					NoteOn = False
					NoteOff =True
					print ('Key Off ' + str(InputNote) + ' Note: ' + str(PianoKeyNoteTable[InputNote]) + ' Character: ' + 
						str(TypingKeyLetterTable[InputNote]) + ' Command: ' + str(hex(0xF0)) + ' ' + str(hex(TypingKeyCommandTable[InputNote])))
					SendTypingRelease()
					SendTypingKey()
                        

	time.sleep(0.01)
	
except KeyboardInterrupt:
	print('')
finally:
	print("Exit.")
	midiin.close_port()
del midiin



