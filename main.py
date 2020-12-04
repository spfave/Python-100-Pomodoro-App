from tkinter import *
import datetime


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 4

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """ Initiates countdown timer start """
    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """ Counts down time """

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", font=(
    FONT_NAME, 48, "normal"), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(
    FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

button_start = Button(text="Start", font=(FONT_NAME, 12),
                      command=start_timer, padx=10)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=(FONT_NAME, 12), padx=10)
button_reset.grid(row=2, column=2)

label_checks = Label(text="✔", font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
label_checks.grid(row=3, column=1)

window.mainloop()
