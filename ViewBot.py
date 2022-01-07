import webbrowser
import os
import time
import keyboard
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def bot2():
    webbrowser.open_new(View)
    time.sleep(10)
    os.system("taskkill /im opera.exe /f")

View = 'https://youtu.be/bqop2QCxIyU'
x = 0
while True:
    bot2()
    Clear()
    x += 1
    print(x)



