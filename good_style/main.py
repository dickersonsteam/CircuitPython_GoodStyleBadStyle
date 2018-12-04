#
# Good Style Using Loops & Lists
#

import audioio
import board
import digitalio

# list all samples here
samples = [audioio.WaveFile(open("kick.wav", "rb")),
           audioio.WaveFile(open("snare.wav", "rb")),
           audioio.WaveFile(open("hihat.wav", "rb")),
           audioio.WaveFile(open("crash.wav", "rb")),
           audioio.WaveFile(open("shaker.wav", "rb")),
           audioio.WaveFile(open("whistle.wav", "rb")),
           audioio.WaveFile(open("clap.wav", "rb")),
           audioio.WaveFile(open("what.wav", "rb"))]

# list all input buttons here
buttons = [digitalio.DigitalInOut(board.D3),
           digitalio.DigitalInOut(board.D6), 
           digitalio.DigitalInOut(board.D5),
           digitalio.DigitalInOut(board.D4),
           digitalio.DigitalInOut(board.A1),
           digitalio.DigitalInOut(board.A2),
           digitalio.DigitalInOut(board.A3),
           digitalio.DigitalInOut(board.A4)]
   
# initialize all buttons in the list   
for i in buttons:
    i.switch_to_input(pull=digitalio.Pull.UP)

# test all buttons
print("Test Buttons")

for index, button in enumerate(buttons):
    print("Push Button " + str(index))
    while button.value:
        pass
    print(str(i))
    print("Button " + str(index) + " works.")
    
print("All buttons work.")