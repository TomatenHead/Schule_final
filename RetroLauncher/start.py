import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'


import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('pygame')
import pgzrun


from random import randint
from time import time
import time

WIDTH = 1535
HEIGHT = 790
music.play("start.mp3")
x = 0
f1 = 0


def intro1():
    global f1
    f1 += 10
    if f1 > 255:
        f1 = 255
        
    screen.draw.filled_rect((Rect((617,245),(300,300))),(f1,f1*0.75,0))
    screen.draw.text("R",center=(767,430), color=(0.2*f1,0,0.5*f1),fontsize=(300),fontname="minecraft")
    screen.draw.text("RetroLauncher",midtop=(767,545), color=(0.5*f1,0.5*f1,0.5*f1),fontsize=(60),fontname="minecraft")


def intro2():
    global f1
    
        
    
    
    #screen.draw.text("Y",center=(740,450), color=(0.5*f1,0.5*f1,0.5*f1),fontsize=(300),fontname="minecraft",angle = 25)
    screen.draw.filled_rect((Rect((657,245),(1000,1000))),(0,0,0))
    screen.draw.text("Y",center=(790,450), color=(0.5*min(255,f1),0.5*min(255,f1),0.5*min(255,f1)),fontsize=(300),fontname="minecraft",angle = 25)
    
    
    
        
    
    screen.draw.filled_rect((Rect((657,245),(60,300))),(0,0,0))
    screen.draw.text("Yanis Engine",midtop=(767,545), color=(0.5*min(255,f1),0.5*min(255,f1),0.5*min(255,f1)),fontsize=(60),fontname="minecraft")
    screen.draw.filled_rect((Rect((657,245),(10,300))),(0,min(255,f1)*0.75,min(255,f1)))
    screen.draw.filled_rect((Rect((707,245),(10,300))),(min(255,f1),min(255,f1)*0.75,0))
    
def draw():
    global f1, x
    screen.clear()
    screen.fill("black")
    screen.draw.text("press any button to continue",midtop=(767,145), color=(255,255,255),fontsize=(60),fontname="minecraft")

    if x == 1:
        intro1()
    if x == 0:
        intro2()
    
    
    

def update():
    global f1, x
    if f1 > 300:
        x +=1
        f1 = 0
    f1 += 2
    
    if x == 2:
        music.stop()
        file_path = "//GY100040/Yanise/Desktop/RetroLauncher/main.py"
        try:
            with open(file_path):
                os.system(f"python {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}. Playing alternative main.py")
            os.system(f"python main.py")
        quit()
def on_key_down(key):
    global x
    x += 1
def on_mouse_down():
    global x
    x += 1
    
pgzrun.go()
