import tkinter as tk

# Global variables
running = False
counter = 0

def update_time():
    global counter
    if running:
        minutes = counter // 6000
        seconds = (counter // 100) % 60
        millis = counter % 100
        time_str = f"{minutes:02}:{seconds:02}:{millis:02}"
        label.config(text=time_str)
        counter += 1
        root.after(10, update_time)

def start():
    global running
    if not running:
        running = True
        update_time()

def pause():
    global running
    running = False

def reset():
    global counter, running
    running = False
    counter = 0
    label.config(text="00:00:00")

# GUI setup
root = tk.Tk()
root.title("Stopwatch")

label = tk.Label(root, text="00:00:00", font=("Courier", 40))
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

start_btn = tk.Button(frame, text="Start", width=10, command=start)
start_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(frame, text="Pause", width=10, command=pause)
pause_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(frame, text="Reset", width=10, command=reset)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()
