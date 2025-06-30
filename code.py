import digitalio
import board
import time
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile
        
btn = digitalio.DigitalInOut(board.GP16)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.DOWN

tail1 = digitalio.DigitalInOut(board.GP0)
tail1.direction = digitalio.Direction.OUTPUT

tail2 = digitalio.DigitalInOut(board.GP1)
tail2.direction = digitalio.Direction.OUTPUT


mouth1 = digitalio.DigitalInOut(board.GP4)
mouth1.direction = digitalio.Direction.OUTPUT

mouth2 = digitalio.DigitalInOut(board.GP5)
mouth2.direction = digitalio.Direction.OUTPUT


def reset():
    tail1.value = False
    tail2.value = False
    mouth1.value = False
    mouth2.value = False
 
def mouthShut():
    mouth1.value = True
    mouth2.value = False
        
def mouthClose():
    mouth1.value = False
    mouth2.value = False
    
def mouthOpen():
    mouth1.value = False
    mouth2.value = True
    
def tailDown():
    if tail1.value == False and tail2.value == True:
        tail1.value = False
        tail2.value = True
    else:
        tail1.value = False
        tail2.value = False
    
def tailUp():
    tail1.value = True
    tail2.value = False


def imChuckBass():
    reset()
    mouthOpen()
    time.sleep(0.2)
    mouthShut()
    time.sleep(0.2)
    mouthOpen()
    time.sleep(0.2)
    mouthClose()		
    time.sleep(0.2)
    mouthOpen()
    time.sleep(0.2)
    mouthShut()
    
def tailBeat():
    tailUp()
    time.sleep(0.25)
    tailDown()
    
def intro():
    time.sleep(0.6)
    tailBeat()
    time.sleep(0.1)
    for n in range(3):
        tailBeat()
        time.sleep(0.6)
    for n in range(4):
        tailBeat()
        time.sleep(0.1)
    
def mid():
    tailUp()
    time.sleep(1)
    tailDown()
    time.sleep(1)
    tailUp()
    time.sleep(1)
    tailDown()
    time.sleep(1) 
    
def outro(): 
    for n in range(5):
        for n in range(3):
            tailBeat()
            time.sleep(0.1)
        time.sleep(0.3)
            
def ggRythem():
    reset()
    intro()
    mid()
    outro()
        
audio = AudioOut(board.GP15)
def playAudio():
    print("Playing Audio")
    with open("/gg.wav", "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            ggRythem()
            time.sleep(1)
            imChuckBass()
            time.sleep(1)

def main():
    while True:
        print(btn.value)
        time.sleep(0.2)

        #if(btn.value):
            #print("button pressed")
            #playAudio()
main()
