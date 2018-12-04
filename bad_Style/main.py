#
# Bad Style Using Copy & Paste
#

import audioio
import board
import digitalio

# list all samples here
sampleA = audioio.WaveFile(open("kick.wav", "rb"))
sampleB = audioio.WaveFile(open("snare.wav", "rb"))
sampleC = audioio.WaveFile(open("hihat.wav", "rb"))
sampleD = audioio.WaveFile(open("crash.wav", "rb"))
sampleE = audioio.WaveFile(open("shaker.wav", "rb"))
sampleF = audioio.WaveFile(open("whistle.wav", "rb"))
sampleG = audioio.WaveFile(open("clap.wav", "rb"))
sampleH = audioio.WaveFile(open("what.wav", "rb"))

# list all input buttons here
buttonA = digitalio.DigitalInOut(board.D3)
buttonB = digitalio.DigitalInOut(board.D6)
buttonC = digitalio.DigitalInOut(board.D5)
buttonD = digitalio.DigitalInOut(board.D4)
buttonE = digitalio.DigitalInOut(board.A1)
buttonF = digitalio.DigitalInOut(board.A2)
buttonG = digitalio.DigitalInOut(board.A3)
buttonH = digitalio.DigitalInOut(board.A4)

# set all buttons to input (default to output)
buttonA.switch_to_input(pull=digitalio.Pull.UP)
buttonB.switch_to_input(pull=digitalio.Pull.UP)
buttonC.switch_to_input(pull=digitalio.Pull.UP)
buttonD.switch_to_input(pull=digitalio.Pull.UP)
buttonE.switch_to_input(pull=digitalio.Pull.UP)
buttonF.switch_to_input(pull=digitalio.Pull.UP)
buttonG.switch_to_input(pull=digitalio.Pull.UP)
buttonH.switch_to_input(pull=digitalio.Pull.UP)

# test all buttons
print("Test Buttons")

print("Push Button A.")
while buttonA.value:
    pass
print("Button A Works.")

print("Push Button B.")
while buttonB.value:
    pass
print("Button B Works.")

print("Push Button C.")
while buttonC.value:
    pass
print("Button C Works.")

print("Push Button D.")
while buttonD.value:
    pass
print("Button D Works.")

print("Push Button E.")
while buttonE.value:
    pass
print("Button E Works.")

print("Push Button F.")
while buttonF.value:
    pass
print("Button F Works.")

print("Push Button G.")
while buttonG.value:
    pass
print("Button G Works.")

print("Push Button H.")
while buttonH.value:
    pass
print("Button H Works.")

print("All buttons work.")