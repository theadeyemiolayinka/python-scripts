import time
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("350x400")
win.title("Countdown Timer")
win.configure(background='#f2a06b')

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(win, width=3, font=("Ariel", 20, ""), fg='white', bg='#FF5733', textvariable=hour )
minuteEntry = Entry(win, width=3, font=("Ariel", 20, ""), fg='white', bg='#FF5733', textvariable=minute)
secondEntry = Entry(win, width=3, font=("Ariel", 20, ""), fg='white', bg='#FF5733', textvariable=second)

hourEntry.place(x=100, y=120)
minuteEntry.place(x=160, y=120)
secondEntry.place(x=220, y=120)

def submit():
    try:
        clockTime = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Incorrect values")

    while(clockTime > -1):
        
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if(totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hour.set("{0:2d}".format(totalHours))
        minute.set("{0:2d}".format(totalMinutes))
        second.set("{0:2d}".format(totalSeconds))

 
        win.update()
        time.sleep(1)

        if(clockTime == 0):
            messagebox.showinfo("Finished", "Time's Up!")

        clockTime -= 1


setTimeButton = Button(win, text='Set Time Countdown', bd='2',fg="white", bg="#FF5733", command=submit)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()
