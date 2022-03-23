print('h for hiberation')
print('s for shutdown')
print('r for restart')
print('sl for sleep')
print('out for signout')

from pyautogui import click, hotkey, typewrite, press
from time import sleep

input_ = input('command: ').lower()  
time = input('time left: ')
sec = 0

for i in range(len(time)):
    if time[i] == 'h':
        pos = 1
        while True:
            if not time[i-pos].isdigit():
                pos = i-pos
                break
            pos += 1
        if pos<0:pos = 0
        sec += int(time[pos:i])*60*60
    
    elif time[i] == 'm':
        pos = 1
        while True:
            if not time[i-pos].isdigit():
                pos = i-pos
                break
            pos += 1
        if pos<0:pos = 0
        sec += int(time[pos:i])*60
    
    elif time[i] == 's':
        pos = 1
        while True:
            if not time[i-pos].isdigit():
                pos = i-pos
                break
            pos += 1
        if pos<0:pos = 0
        sec += int(time[pos:i])

try:
    sec += int(time)
except:
    pass

commands = ['h', 's', 'r', 'sl', 'out']

time_sec = 0


def the_box():
    global time_sec
    while True:
        sleep(1)
        time_sec += 1

        if time_sec >= sec:
            hotkey('win','d')
            sleep(0.5)
            hotkey('alt', 'f4')
            sleep(0.5)
            break

if input_ == 'h':
    print(sec,'sec left to Hibernate')
    the_box()
    press('up')

elif input_ == 'r':
    print(sec,'sec left to Restart')
    the_box()
    press('down')

elif input_ == 'sl':
    print(sec,'sec left to Sleep')
    the_box()
    press('up', presses=2)

elif input_ == 'out':
    print(sec,'sec left to Sign out')
    the_box()
    press('up', presses=3)
    
press('enter')