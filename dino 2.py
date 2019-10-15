import time
from PIL import ImageGrab
import pyautogui

def capture():
    screen = ImageGrab.grab()
    return screen

def enemy(screen):
    for x in range (248, 264):
        for y in range (229, 232):
            obstacle = screen.getpixel((x, y))
            bg_color = screen.getpixel((100, 110))
            if obstacle != bg_color:
                return True

def air(screen):
    for x in range (256, 263):
        for y in range (200, 205):
            air_enemy = screen.getpixel((x,y))
            bg_color = screen.getpixel((100, 110))
            if air_enemy != bg_color:
                return True

def lower():
    pyautogui.keyDown('down')
    time.sleep(0.4)
    pyautogui.keyUp('down')
    print("lower")
def jump():
    pyautogui.keyDown('up')
    time.sleep(0.2)
    pyautogui.keyUp('up')
    print("jump")
time.sleep(3)
while True:
    screen = capture()
    if enemy(screen):
        jump()
    if air(screen):
        lower()
        
