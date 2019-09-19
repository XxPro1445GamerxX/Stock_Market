import os, sys
import time
time2 = time.sleep(2)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import * 
path_os = os.path.dirname(os.path.abspath(__file__))
path_os = path_os + '\\BeepSound\\beep.WAV'
print('TROLL')
time2
try:
    while True:
        mixer.init()
        mixer.music.load(path_os)
        mixer.music.play()
except KeyboardInterrupt:
    sys.exit()
