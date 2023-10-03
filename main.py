from tkinter import Tk, Label, Canvas, PhotoImage, Button

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def start_timer():
    pass
def reset_timer():
    pass


#---------------------- UI SETUP ----------------------  #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 30), fg="green", bg=YELLOW)
title.pack()

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="./images/tomato.png")
canvas.create_image(100, 112, image=tomato_img,)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW)
canvas.pack()

start_button = Button(text="Start", command=start_timer)
start_button.pack(side="left")

stop_button = Button(text="Reset", command=reset_timer)
stop_button.pack(side="right")

check_mark = Label(bg=YELLOW, font=(
    FONT_NAME, 20), fg="green", padx=7)

window.mainloop()