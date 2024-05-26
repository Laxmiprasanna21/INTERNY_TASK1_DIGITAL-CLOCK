import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%H:%M:%S %p')
    current_date = time.strftime('%A, %B %d, %Y')
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    set_greeting()
    clock_label.after(1000, time_update)  # Update the time every second

def set_greeting():
    hour = int(time.strftime('%H'))
    if 5 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    elif 18 <= hour < 22:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    greeting_label.config(text=greeting)

# Create the main window
root = tk.Tk()
root.title("Enhanced Digital Clock")

# Customize the window size and background color
root.geometry("500x300")
root.configure(bg="light blue")

# Create and style the clock label
clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
clock_label.pack(expand=True)

# Create and style the date label
date_label = tk.Label(root, font=("Helvetica", 24), bg="black", fg="cyan")
date_label.pack(expand=True)

# Create and style the greeting label
greeting_label = tk.Label(root, font=("Helvetica", 16), bg="black", fg="cyan")
greeting_label.pack(expand=True)

# Call the time update function
time_update()

# Run the main loop
root.mainloop()
