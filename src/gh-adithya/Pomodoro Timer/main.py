from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = ""
timer_fn = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_fn)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    tick_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        countdown(short_break_secs)
        timer.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        countdown(long_break_secs)
        timer.config(text="Break", fg=RED)
    else:
        countdown(work_secs)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_fn
        timer_fn = window.after(1, countdown, count - 1)
    else:
        global ticks
        if reps % 2 != 0:
            ticks += "✔"
            tick_mark.config(text=f"{ticks}")

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
#Replace PhotoImage() input with correct image path.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="black")
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_mark = Label(bg=YELLOW, fg=GREEN)
tick_mark.grid(row=3, column=1)
window.mainloop()
