from tkinter import Tk, Label, Canvas, PhotoImage, Button, messagebox
import math
import pygame
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load("./audio/alarm.wav")
    pygame.mixer.music.play()

# ---------------------- TIMER MECHANISM ----------------------  #
def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_dow(long_break_sec)
        title.config(text="Long Break", fg="red")
        messagebox.showinfo(message="Long Break")
        play_alarm()
    elif reps % 2 == 0:
        count_dow(short_break_sec)
        title.config(text="Short Break", fg="pink")
        messagebox.showinfo(message="Short Break")
        play_alarm()
    else:
        count_dow(work_sec)
        title.config(text="Work", fg="green")
        messagebox.showinfo(message="Work")
        play_alarm()

# ---------------------- RESET MECHANISM ----------------------  #

def reset_timer():
    start_button.config(state="active")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------- COUNTDOWN MECHANISM ----------------------  #
def count_dow(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_dow, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check_mark.config(text=mark)

# ---------------------- UI SETUP ----------------------  #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 30), fg="green", bg=YELLOW)
title.pack()

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="./images/tomato.png")
canvas.create_image(100, 112, image=tomato_img,)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW)
canvas.pack()

start_button = Button(text="Start", command=start_timer)
start_button.pack(side="left")

stop_button = Button(text="Reset", command=reset_timer)
stop_button.pack(side="right")

check_mark = Label(bg=YELLOW, font=(
    FONT_NAME, 20), fg="green", padx=7)
check_mark.pack()

window.mainloop()
