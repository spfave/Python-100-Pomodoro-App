from tkinter import *
import datetime


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1  # 25
SHORT_BREAK_MIN = 1  # 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """ Reset pomodoro timer application """
    window.after_cancel(timer)

    global reps
    reps = 0
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label_checks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """ Initiates countdown timer start """
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """ Counts down time """

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(50, count_down, count-1)
    else:
        start_timer()
        work_sessions = reps // 2
        checks = work_sessions*"✔"
        label_checks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
label_timer = Label(text="Timer", font=(
    FONT_NAME, 48, "normal"), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# set highlightthickness=0 to remove canvas border
tomato_image = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Buttons
button_start = Button(text="Start", font=(FONT_NAME, 12),
                      command=start_timer, padx=10,)
button_start.grid(row=2, column=0, pady=5)

button_reset = Button(text="Reset", font=(FONT_NAME, 12),
                      command=reset_timer, padx=10)
button_reset.grid(row=2, column=2, pady=5)

# Working session checkmark count label
label_checks = Label(text="", font=(
    FONT_NAME, 18), bg=YELLOW, fg=GREEN)
label_checks.grid(row=3, column=0, columnspan=3, pady=5)
# Note: when column spanning with grid, 'column=' entry in grid() needs to be starting column

window.mainloop()
