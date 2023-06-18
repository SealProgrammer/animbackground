import ctypes, os
from time import sleep

numFrames = int(input('Number of frames: '))
fps = float(input('FPS: '))

if input('Run (Y/N): ').upper() != 'Y':
    raise RuntimeError('You don\'t actually want to run it')

print('Press CTRL+C to exit.')

def get_image(frame):
    return os.path.join(os.path.dirname(__file__), f'./background{frame % numFrames + 1}.png')

frame = 1

while True:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, get_image(frame), 0)
    sleep(1/fps)
    frame += 1