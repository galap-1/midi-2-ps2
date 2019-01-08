


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


#the data in the following are sent least significant bit first

def SendTypingRelease():
	if 0 <= InputNote <= 24:
	#^ test if note is in relevant range. SendTypingKey inherently tests this.
		#we are sending 0xF0.
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x0
		print ( 1)
		print ( 1)
		print ( 1)
		print ( 1)
		# ^ 0xF
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit


def SendTypingKey():
	if InputNote == 0:
		# we are sending 0x1A typewriter Z piano C
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 1)
		# ^ 0xA
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit
	
	elif InputNote == 1:
		# we are sending 0x1B typewriter S piano C#
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 1)
		# ^ 0xB
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit
	
	
	elif InputNote == 2:
		# we are sending 0x22 typewriter X piano D
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit

	
	elif InputNote == 3:
		# we are sending 0x23 typewriter D piano D#
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit


	elif InputNote == 4:
		# we are sending 0x21 typewriter C piano E
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit

	
	elif InputNote == 5:
		# we are sending 0x2A typewriter V piano F
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 1)
		# ^ 0xA
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit
	
	
	elif InputNote == 6:
		# we are sending 0x34 typewriter G piano F#
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 0)
		print ( 1)
		print ( 0)
		# ^ 0x4
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit

	
	elif InputNote == 7:
		# we are sending 0x32 typewriter B piano G
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit


	elif InputNote == 8:
		# we are sending 0x33 typewriter H piano G#
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit

	elif InputNote == 9:
		# we are sending 0x31 typewriter N piano A
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit

	elif InputNote == 10:
		# we are sending 0x3B typewriter J piano A#
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 1)
		# ^ 0xB
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit


	elif InputNote == 11:
		# we are sending 0x3A typewriter M piano B
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 1)
		# ^ 0xa
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit
		
	elif InputNote == 12:
		# we are sending 0x15 typewriter Q piano C^
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 1)
		print ( 0)
		# ^ 0x5
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 1)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit
		

	elif InputNote == 13:
		# we are sending 0x1E typewriter 2 piano C#^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 1)
		print ( 1)
		# ^ 0xE
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 0)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit		
		
		
	elif InputNote == 14:
		# we are sending 0x1D typewriter W piano D^
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 1)
		print ( 1)
		# ^ 0xD
		print ( 1)
		print ( 0)
		print ( 0)
		print ( 0)
		# ^ 0x1
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit		
		
		
	elif InputNote == 15:
		# we are sending 0x26 typewriter 3 piano D#^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 1)
		print ( 0)
		# ^ 0x6
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit		
		

	elif InputNote == 16:
		# we are sending 0x24 typewriter E piano E^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 0)
		print ( 1)
		print ( 0)
		# ^ 0x4
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit
		
		
	elif InputNote == 17:
		# we are sending 0x2D typewriter R piano F^
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 1)
		print ( 1)
		# ^ 0xD
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit
		
	elif InputNote == 18:
		# we are sending 0x2E typewriter 5 piano F#^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 1)
		print ( 1)
		# ^ 0xE
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit		
		
		
	elif InputNote == 19:
		# we are sending 0x2C typewriter T piano G^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 0)
		print ( 1)
		print ( 1)
		# ^ 0xC
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit		
		
	elif InputNote == 20:
		# we are sending 0x36 typewriter 6 piano G#^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 1)
		print ( 1)
		print ( 0)
		# ^ 0x6
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit


	elif InputNote == 21:
		# we are sending 0x25 typewriter Y piano A^
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 1)
		print ( 0)
		# ^ 0x5
		print ( 0)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x2
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit


	elif InputNote == 22:
		# we are sending 0x3D typewriter 7 piano A#^
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 0)
		print ( 1)
		print ( 1)
		# ^ 0xD
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit		


	elif InputNote == 23:
		# we are sending 0x3C typewriter U piano B^
		print ( 0)
		# ^ start bit
		print ( 0)
		print ( 0)
		print ( 1)
		print ( 1)
		# ^ 0xC
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 1)
		# ^ we are even, so use odd parity bit
		print ( 1)
		# ^ stop bit		
		
		
	elif InputNote == 24:
		# we are sending 0x43 typewriter I piano C^^
		print ( 0)
		# ^ start bit
		print ( 1)
		print ( 1)
		print ( 0)
		print ( 0)
		# ^ 0x3
		print ( 0)
		print ( 0)
		print ( 1)
		print ( 0)
		# ^ 0x4
		print ( 0)
		# ^ we are odd, so use even parity bit
		print ( 1)
		# ^ stop bit
		
	else:
		print("note out of range")	




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



