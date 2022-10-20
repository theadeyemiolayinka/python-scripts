
import time
import winsound
import pyglet

def play(hh, mm):
    not_alarmed = 1
    print('Wait...')

    while(not_alarmed):
        cur_time = list(time.localtime()) # get the time right now
        hour = cur_time[3] # find the hour
        minute = cur_time[4] # and the minute
        if hour == hh and minute == mm:
            song = pyglet.media.load('alarm.wav')
            song.play() # play the sound
            pyglet.app.run()
            not_alarmed = 0 # stop the loop
            break

def get_input(choice):
    if choice == 1:
        mins = input('How many minutes from now? ')
        hh_from_now = mins / 60 # if minutes > 60, this will adjust the hours
        mm_from_now = mins % 60 # and then the minutes
        cur_time = list(time.localtime()) # get the time right now
        hour = cur_time[3] # find the current hour
        minute = cur_time[4] # and the current minute
        hh = (hour + hh_from_now) % 24 # cycle through the clock if hh > 24
        mm = (minute + mm_from_now) % 60 # cycle through the clock if mm > 60
        play(hh, mm)
    elif choice == 2:
        hh = get_time(23, 'Hour(0-23)? ')
        mm = get_time(59, 'Minute (0-59)? ')
        play(hh, mm)
    else:
        get_input(int(input('Invalid option, Choose again: ')))

def get_time(max, text):
    val = int(input(text))
    if val > max or val < 0:
        return get_time(max, "Invalid value, try again: ")
    else:
        return val

if __name__ == '__main__':

    print ("""
    1. Play sound after X minutes
    2. Play sound at an exact time
    """)
    get_input(int(input('What do you want to do? ')))

    