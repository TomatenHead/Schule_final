import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'


import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('pygame')
import pgzrun

WIDTH = 1535
HEIGHT = 790

def draw():
    screen.clear()
    screen.draw.text("Game is getting programmed, nothing to see here!", center=(WIDTH/2, HEIGHT-HEIGHT/4), color="white", fontsize=60)
    screen.draw.text("Comming soon!!!", center=(WIDTH/2, HEIGHT/3), color="Yellow", fontsize=200, angle = 12)

def on_key_down(key):
    if key == keys.ESCAPE:
        os.system("taskkill /IM python.exe /F")
    else:
        file_path = "//GY100040/Yanise/Desktop/RetroLauncher/main.py"
        try:
            with open(file_path):
                os.system(f"python {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}. Playing alternative Brickbreaker.py")
            os.system(f"python main.py")
        
def on_mouse_down(pos, button):
    quit()
    
pgzrun.go()
